import AuthCard from "../components/AuthCard";
import AuthFooterLink from "../components/AuthFooterLink";
import AuthHeader from "../components/AuthHeader";
import AuthLayout from "../components/AuthLayout";
import RegisterVendorForm from "../forms/RegisterVendorForm";

function ProfileSetupPage() {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Step 2 of 2: Company Information"
          subtitle="Enter your company details to finish creating your account."
        />

        <RegisterVendorForm />

        {/* Back link (using shared component) */}
        <AuthFooterLink
          text="Need to go back?"
          linkText="Back to Step 1"
          to="/vendor/register"
        />
      </AuthCard>
    </AuthLayout>
  );
}

export default ProfileSetupPage;
