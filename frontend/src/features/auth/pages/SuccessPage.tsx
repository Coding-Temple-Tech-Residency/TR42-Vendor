import { Link } from "react-router-dom";
import AuthLayout from "../components/AuthLayout";
import AuthCard from "../components/AuthCard";
import AuthButton from "../components/AuthButton";

function SuccessPage() {
  return (
    <AuthLayout>
      {/* <AuthLayout showHeader={false}> */}
      <AuthCard>

        <h2 className="text-2xl font-semibold text-gray-800 text-center">
          Vendor Profile Activated
        </h2>

        <p className="text-gray-600 text-center">
          Your account has been created successfully and is now ready for platform access.
        </p>

        <Link to="/vendor/login">
          <AuthButton>
            Go to Login
          </AuthButton>
        </Link>

      </AuthCard>
    </AuthLayout>
  );
}

export default SuccessPage;