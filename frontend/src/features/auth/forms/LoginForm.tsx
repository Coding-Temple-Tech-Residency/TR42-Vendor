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
    identifier: "",
    password: "",
  });

  // Error state
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));

    setError(null);
  };

  // Handle form submit
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.identifier || !formData.password) {
      setError("Please enter login infomation.");
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
        credentials: "include",
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || result.message || "Login failed.");
      }

      console.log("Login successful!");

      navigate("/vendor/dashboard");
    } catch (err: any) {
      console.log("Login error:", err);
      setError(err.message || "Login failed.");

      setFormData({
        identifier: "",
        password: "",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      <TextInput
        label="Email / Username"
        name="identifier"
        type="text"
        value={formData.identifier}
        onChange={handleChange}
        placeholder="Enter your email or username"
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
