import { useState } from "react";
import TextInput from "../auth/components/TextInput";
import PasswordInput from "../auth/components/PasswordInput";
import AuthButton from "../auth/components/AuthButton";
import AuthFooterLink from "../auth/components/AuthFooterLink";

const LoginForm = () => {
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
    setError(null); // clear error when user types
  };

  // Handle form submit
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Basic front-end validation
    if (!formData.email || !formData.password) {
      setError("Please enter both email and password.");
      return;
    }

    try {
      setLoading(true);
      setError(null);

      // TODO: Replace with real API call
      // Example mock login:
      await new Promise((resolve) => setTimeout(resolve, 1000)); // simulate network delay
      if (
        formData.email !== "test@example.com" ||
        formData.password !== "123456"
      ) {
        throw new Error("Invalid email or password.");
      }

      // Success
      console.log("Login successful!", formData);
      // TODO: Redirect user or update global auth state
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

      {/* Display error message */}
      {error && <p className="text-red-500 text-sm mt-1">{error}</p>}

      <AuthButton type="submit" disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </AuthButton>

      <AuthFooterLink
        text="Forgot your password?"
        linkText="Reset it"
        to="/forgot-password"
      />

      <AuthFooterLink
        text="Don’t have an account?"
        linkText="Create one"
        to="/register"
      />
    </form>
  );
};

export default LoginForm;
