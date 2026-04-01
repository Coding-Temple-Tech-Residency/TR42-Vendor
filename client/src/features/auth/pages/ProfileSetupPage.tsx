import ProfileSetupForm from "../forms/ProfileSetupForm";

function ProfileSetupPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-gray-200 to-blue-900">
      
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl shadow-xl p-8">

          <h2 className="text-center text-xl font-semibold mb-6">
            Step 2 of 2: Company Information
          </h2>

          <ProfileSetupForm />

        </div>
      </div>

    </div>
  );
}

export default ProfileSetupPage;