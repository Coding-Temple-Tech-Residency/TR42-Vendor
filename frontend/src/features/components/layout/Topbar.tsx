import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

type TopbarProps = {
  title?: string;
  userName?: string;
  userRole?: string;
  rightContent?: React.ReactNode;
};

export default function Topbar({
  title = "Dashboard",
  userName = "Vendor User",
  userRole = "Accounting",
  rightContent,
}: TopbarProps) {
  const [menuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement | null>(null);
  const navigate = useNavigate();

  const handleSignOut = () => {
    //Remove whatever auth data your app stores
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    //Redirect login
    navigate("/vendor/login");
  };

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setMenuOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <div className="sticky flex min-h-24 items-center justify-between border-b border-[#1F2A44] px-4 sm:px-6 lg:px-8">
      <div>
        <p className="text-sm text-slate-500">Welcome back</p>
        <h2 className="text-xl font-semibold text-slate-900">{title}</h2>
      </div>

      <div className="flex items-center gap-4">
        {rightContent}

        <div
          ref={menuRef}
          className="relative flex items-center gap-4 rounded-full border border-slate-200 bg-slate-50 px-10 py-2"
        >
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-slate-800 text-sm font-semibold text-white">
            {userName.slice(0, 1).toUpperCase()}
          </div>
          <div className="hidden sm:flex items-baseline whitespace-nowrap gap-2">
            <p className="text-lg font-medium text-slate-900">{userName}</p>
            <p className="text-sm text-slate-500">{userRole}</p>
          </div>

          <button
            onClick={() => setMenuOpen((prev) => !prev)}
            className="rounded-md p-2 hover:bg-slate-100"
          >
            <svg
              className={`h-4 w-4 text-slate-500 transition ${menuOpen ? "rotate-180" : ""}`}
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M19 9l-7 7-7-7"
              />
            </svg>
          </button>

          {menuOpen && (
            <div className="absolute right-0 top-14 w-44 rounded-xl border border-slate-200 bg-white shadow-lg">
              <button
                onClick={handleSignOut}
                className="w-full px-4 py-3 text-left text-sm text-red-600 hover:bg-red-50 hover:rounded-xl"
              >
                Sign Out
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
