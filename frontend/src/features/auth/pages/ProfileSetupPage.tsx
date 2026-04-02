import ProfileSetupForm from "../forms/ProfileSetupForm";
import Logo from "../../../assets/logo.svg";

function ProfileSetupPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-800 to-blue-900 flex items-center justify-center">

      {/* WRAPPER (same as RegisterPage) */}
      <div className="w-full max-w-2xl">

        {/* HEADER */}
        <div className="bg-gradient-to-r from-gray-200 to-gray-100 py-6 px-8 rounded-t-xl border-b flex items-center justify-center">
          <img
            src={Logo}
            alt="Field Force Logo"
            className="h-16 w-auto object-contain"
          />
        </div>

        {/* CARD */}
        <div className="bg-white rounded-b-xl shadow-2xl p-10">

          <h2 className="text-center text-xl font-semibold mb-2">
            Step 2 of 2: Company Information
          </h2>

          <p className="text-center text-sm text-gray-500 mb-6">
            Enter your company details to finish creating your account.
          </p>

          <ProfileSetupForm />

          {/* Back link */}
          <a
            href="/register"
            className="text-blue-600 underline text-sm mt-6 block text-center"
          >
            ← Back to Step 1
          </a>

        </div>

      </div>
    </div>
  );
}

export default ProfileSetupPage;