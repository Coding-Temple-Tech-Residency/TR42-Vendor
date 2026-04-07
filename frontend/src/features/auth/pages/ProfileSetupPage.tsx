import AuthLayout from "../components/AuthLayout";
import AuthCard from "../components/AuthCard";
import AuthHeader from "../components/AuthHeader";
import AuthFooterLink from "../components/AuthFooterLink";
import ProfileSetupForm from "../forms/ProfileSetupForm";

function ProfileSetupPage() {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Step 2 of 2: Company Information"
          subtitle="Enter your company details to finish creating your account."
        />

        <ProfileSetupForm />

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