function SuccessPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-800 to-blue-900">
      <div className="bg-white p-10 rounded-xl shadow-2xl w-full max-w-md text-center">

        <h2 className="text-2xl font-semibold mb-4">Account Created!</h2>

        <p className="text-gray-600 mb-6">
          Your vendor account has been created successfully.
        </p>

        <a
          href="/register"
          className="btn-primary inline-block"
        >
          Go Back to Login
        </a>

      </div>
    </div>
  );
}

export default SuccessPage;
