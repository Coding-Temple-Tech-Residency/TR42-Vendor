import { useState } from "react";
import { useNavigate } from "react-router-dom";
import TextInput from "../components/TextInput";
import PasswordInput from "../components/PasswordInput";
import AuthButton from "../components/AuthButton";
import AuthFooterLink from "../components/AuthFooterLink";

const LoginForm = () => {
  const navigate = useNavigate();

  // Form state
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  // Error state
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
    setError(null);
  };

  // Handle form submit
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.email || !formData.password) {
      setError("Please enter both email and password.");
      return;
    }

    try {
      setLoading(true);
      setError(null);

      // TODO: Replace with real API call
      await new Promise((resolve) => setTimeout(resolve, 1000));

      if (
        formData.email !== "test@example.com" ||
        formData.password !== "123456"
      ) {
        throw new Error("Invalid email or password.");
      }

      console.log("Login successful!", formData);

      // Redirect to dashboard
      navigate("/vendor/dashboard");
    } catch (err: any) {
      setError(err.message || "Login failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      <TextInput
        label="Email"
        name="email"
        type="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="Enter your email"
      />

      <PasswordInput
        label="Password"
        name="password"
        value={formData.password}
        onChange={handleChange}
      />

      {error && <p className="mt-1 text-sm text-red-500">{error}</p>}

      <AuthButton type="submit" disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </AuthButton>

      <AuthFooterLink
        text="Forgot your password?"
        linkText="Reset it"
        to="/vendor/forgot-password"
      />

      <AuthFooterLink
        text="Don’t have an account?"
        linkText="Create one"
        to="/vendor/register"
      />
    </form>
  );
};

export default LoginForm;