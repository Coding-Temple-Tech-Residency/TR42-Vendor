import { useState } from "react";
import { useNavigate } from "react-router-dom";
import AuthButton from "../components/AuthButton";
import AuthFooterLink from "../components/AuthFooterLink";
import PasswordInput from "../components/PasswordInput";
import TextInput from "../components/TextInput";

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

      const response = await fetch("/api/users/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const result = await response.json();
      console.log(result);

      if (!response.ok) {
        throw result;
      }

      console.log("Login successful!");

      // Save auth context to localStorage for protected API calls
      localStorage.setItem("token", result.token);
      localStorage.setItem("user_id", result.user_id);
      // TODO: Backend should return vendor_id in login response, or we need separate endpoint
      // For now, this will be fetched/set by dashboard after auth

      navigate("/vendor/dashboard");
    } catch (err: any) {
      console.log("Login error:", err);
      setError(err.message);
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
