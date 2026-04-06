import DashboardLayout from "../../../layouts/DashboardLayout";

function DashboardPage() {
  // Dummy data (temp until backend)
  const stats = [
    { label: "Unassigned Work Orders", value: 3 },
    { label: "Pending Jobs", value: 2 },
    { label: "Open Invoices", value: 12 },
  ];

  const workOrders = [
    { id: "WO-12345", status: "Pending" },
    { id: "WO-12346", status: "In Progress" },
    { id: "WO-12347", status: "Completed" },
  ];

  return (
    <DashboardLayout>
      <h1>Vendor Dashboard</h1>

      {/* KPI Cards */}
      <div style={{ display: "flex", gap: "10px", marginTop: "20px" }}>
        {stats.map((stat, index) => (
          <div
            key={index}
            style={{
              border: "1px solid #ccc",
              padding: "15px",
              borderRadius: "8px",
              width: "200px",
            }}
          >
            <p>{stat.label}</p>
            <h2>{stat.value}</h2>
          </div>
        ))}
      </div>

      {/* Chart Placeholder */}
      <div style={{ marginTop: "30px" }}>
        <h2>Work Orders (Last 30 Days)</h2>
        <div
          style={{
            height: "150px",
            border: "1px dashed gray",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          Chart goes here
        </div>
      </div>

      {/* Work Orders Table */}
      <div style={{ marginTop: "30px" }}>
        <h2>Open Work Orders</h2>

        {workOrders.map((order, index) => (
          <div
            key={index}
            style={{
              borderBottom: "1px solid #ddd",
              padding: "10px 0",
            }}
          >
            <strong>{order.id}</strong> — {order.status}
          </div>
        ))}
      </div>
    </DashboardLayout>
  );
}

export default DashboardPage;