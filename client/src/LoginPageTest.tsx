function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-sm">
        <h1 className="text-2xl font-bold mb-4 text-center text-blue-600">
          Login Page
        </h1>

        <form className="flex flex-col gap-4">
          <input
            type="email"
            placeholder="Email"
            className="border p-2 rounded"
          />

          <input
            type="password"
            placeholder="Password"
            className="border p-2 rounded"
          />

          <button
            type="button"
            className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
          >
            Login
          </button>
        </form>
      </div>

    </div>
  );
}

export default LoginPage;
