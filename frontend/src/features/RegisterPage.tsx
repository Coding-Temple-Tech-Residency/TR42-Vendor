import RegisterForm from "./auth/forms/RegisterForm";

function RegisterPage() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-800 to-blue-900 flex flex-col items-center justify-center">

            {/* TOP HEADER */}
            {/* <div className="w-full max-w-2xl bg-gray-200 py-4 px-6 rounded-t-lg flex items-center gap-3">
        <div className="w-8 h-8 bg-gray-400 rounded-full" />
        <div>
          <h1 className="font-bold text-lg">Field Force</h1>
          <p className="text-xs text-gray-600">The Service Platform</p>
        </div>
      </div> */}
            <div className="w-full max-w-2xl bg-gradient-to-r from-gray-200 to-gray-100 py-4 px-6 rounded-t-xl flex items-center gap-3 border-b">

                <div className="w-10 h-10 bg-gray-400 rounded-full flex items-center justify-center text-white font-bold">
                    ⚙️
                </div>

                <div>
                    <h1 className="font-bold text-lg text-gray-800">Field Force</h1>
                    <p className="text-xs text-gray-500">The Service Platform</p>
                </div>

            </div>

            {/* CARD */}
            <div className="w-full max-w-2xl bg-white rounded-b-lg shadow-2xl p-10">

                <h2 className="text-center text-xl font-semibold mb-2">
                    Step 1 of 2: Create Your Account
                </h2>

                <p className="text-center text-sm text-gray-500 mb-6">
                    Enter your personal details to get started.
                </p>

                <RegisterForm />

            </div>
        </div>
    );
}

export default RegisterPage;