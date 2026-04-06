import { Link } from "react-router-dom";

function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>
      
      {/* Sidebar */}
      <div style={{ width: "200px", background: "#1f2937", color: "white", padding: "20px" }}>
        <h2>Field Force</h2>

        <nav style={{ marginTop: "20px", display: "flex", flexDirection: "column", gap: "10px" }}>
          <Link to="/dashboard" style={{ color: "white" }}>Dashboard</Link>
          <Link to="/work-orders" style={{ color: "white" }}>Work Orders</Link>
          <Link to="/contractors" style={{ color: "white" }}>Contractors</Link>
        </nav>
      </div>

      {/* Main Content */}
      <div style={{ flex: 1, padding: "20px" }}>
        {children}
      </div>
    </div>
  );
}

export default DashboardLayout;