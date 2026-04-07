import LoginForm from "../forms/LoginForm";
import AuthLayout from "../components/AuthLayout";
import AuthCard from "../components/AuthCard";
import AuthHeader from "../components/AuthHeader";

export default function LoginPage() {
  return (
  <AuthLayout>
    <AuthCard>
      <AuthHeader title="Welcome Back" subtitle="Login to your account" />
      <LoginForm />
    </AuthCard>
  </AuthLayout>
  )
};