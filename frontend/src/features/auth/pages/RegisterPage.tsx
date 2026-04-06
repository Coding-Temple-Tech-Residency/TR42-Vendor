import AuthLayout from "../components/AuthLayout";
import AuthCard from "../components/AuthCard";
import AuthHeader from "../components/AuthHeader";
import RegisterForm from "../forms/RegisterForm";

function RegisterPage() {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Step 1 of 2: Create Your Account"
          subtitle="Enter your personal details to get started."
        />

        <RegisterForm />
      </AuthCard>
    </AuthLayout>
  );
}

export default RegisterPage;