import { useState } from "react";
import TextInput from "../components/TextInput";
import AuthButton from "../components/AuthButton";
import AuthFooterLink from "../components/AuthFooterLink";

const ForgotPasswordForm = () => {
  const [email, setEmail] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert(`Reset link sent to ${email}`);
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      <TextInput
        label="Email"
        name="email"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Enter your email"
      />

      <AuthButton type="submit">Reset Password</AuthButton>

      <AuthFooterLink
        text="Remember your password?"
        linkText="Back to login"
        to="/vendor/login"
      />
    </form>
  );
};

export default ForgotPasswordForm;
