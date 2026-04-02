import LoginForm from "../auth/LoginForm";
import AuthLayout from "../auth/components/AuthLayout";
import AuthCard from "../auth/components/AuthCard";
import AuthHeader from "../auth/components/AuthHeader";

<AuthLayout>
  <AuthCard>
    <AuthHeader title="Welcome Back" subtitle="Login to your account" />
    <LoginForm />
  </AuthCard>
</AuthLayout>;
