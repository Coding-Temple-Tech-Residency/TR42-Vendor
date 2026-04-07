import { Link } from "react-router-dom";

function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-gray-100">
      
      {/* Sidebar */}
      <div className="w-60 bg-slate-800 text-white p-5 flex flex-col">
        
        {/* App Title */}
        <div className="mb-8">
          <h2 className="text-lg font-semibold">Field Force</h2>
        </div>

        {/* Navigation Links */}
        <nav className="flex flex-col gap-2 text-sm">
          <Link to="/dashboard" className="hover:bg-slate-700 p-2 rounded transition">
            Home
          </Link>
          <Link to="/work-orders" className="hover:bg-slate-700 p-2 rounded transition">
            Work Orders
          </Link>
          <Link to="/tickets" className="hover:bg-slate-700 p-2 rounded transition">
            Tickets
          </Link>
          <Link to="/contractors" className="hover:bg-slate-700 p-2 rounded transition">
            Contractors
          </Link>
          <Link to="/invoices" className="hover:bg-slate-700 p-2 rounded transition">
            Invoices
          </Link>
          <Link to="/reports" className="hover:bg-slate-700 p-2 rounded transition">
            Reports
          </Link>
          <Link to="/fraud-risk" className="hover:bg-slate-700 p-2 rounded transition">
            Fraud Risk
          </Link>
          <Link to="/messages" className="hover:bg-slate-700 p-2 rounded transition">
            Messages
          </Link>
        </nav>

        {/* Bottom Section (e.g., Settings) */}
        <div className="mt-auto pt-6 text-xs text-gray-400">
          Settings
        </div>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 p-6">
        {children}
      </div>
    </div>
  );
}

export default DashboardLayout;