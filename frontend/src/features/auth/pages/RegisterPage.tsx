import RegisterForm from "../forms/RegisterForm";
import Logo from "../../../assets/logo.svg";

function RegisterPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-800 to-blue-900 flex items-center justify-center">

      {/* WRAPPER (this is the missing piece) */}
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
            Step 1 of 2: Create Your Account
          </h2>

          <p className="text-center text-sm text-gray-500 mb-6">
            Enter your personal details to get started.
          </p>

          <RegisterForm />
        </div>

      </div>
    </div>
  );
}

export default RegisterPage;
