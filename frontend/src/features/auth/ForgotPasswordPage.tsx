import ForgotPasswordForm from "../auth/ForgotPasswordForm";
import AuthLayout from "../auth/components/AuthLayout";
import AuthCard from "../auth/components/AuthCard";
import AuthHeader from "../auth/components/AuthHeader";

<AuthLayout>
  <AuthCard>
    <AuthHeader
      title="Forgot Password"
      subtitle="Enter your email to reset your password"
    />
    <ForgotPasswordForm />
  </AuthCard>
</AuthLayout>;
