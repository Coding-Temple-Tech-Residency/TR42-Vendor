import logo from "../../../assets/logo.svg";

function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center px-4"
      style={{
        background:
          "linear-gradient(to top, #243041 0%, #465366 40%, #e5e8ed 100%)",
      }}
    >
      {/* GLOBAL HEADER (used by ALL pages) */}
      <div className="w-full max-w-2xl">
        <div className="bg-gradient-to-r from-gray-200 to-gray-100 py-6 px-8 rounded-t-xl border-b flex items-center justify-center">
          <img
            src={logo}
            alt="Field Force Logo"
            className="h-16 w-auto object-contain"
          />
        </div>
      </div>

      {/* PAGE CONTENT */}
      <div className="w-full max-w-2xl">
        {children}
      </div>
    </div>
  );
}

export default AuthLayout;
