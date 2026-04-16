import AuthCard from "../components/AuthCard";
import AuthHeader from "../components/AuthHeader";
import AuthLayout from "../components/AuthLayout";
import RegisterUserForm from "../forms/RegisterUserForm";
import AuthFooterLink from "../components/AuthFooterLink";

function RegisterPage() {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Step 1 of 2: Create Your Account"
          subtitle="Enter your personal details to get started."
        />

        <RegisterUserForm />
       

        {/* Footer Link */}
        <AuthFooterLink
          text="Already have an account?"
          linkText="Login"
          to="/vendor/login"
        />
        
      </AuthCard>
    </AuthLayout>
  );
}

export default RegisterPage;
