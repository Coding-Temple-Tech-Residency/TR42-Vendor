import ForgotPasswordForm from "../forms/ForgotPasswordForm";
import AuthLayout from "../components/AuthLayout";
import AuthCard from "../components/AuthCard";
import AuthHeader from "../components/AuthHeader";


export default function ForgotPasswordPage(){
  return(
  <AuthLayout>
    <AuthCard>
      <AuthHeader
        title="Forgot Password"
        subtitle="Enter your email to reset your password"
      />
      <ForgotPasswordForm />
    </AuthCard>
  </AuthLayout>
  )
}