// import DashboardLayout from "../../../layouts/DashboardLayout";

// function DashboardPage() {
//   // Temporary data (until backend is connected)
//   const stats = [
//     { label: "Unassigned Work Orders", value: 3 },
//     { label: "Pending Jobs", value: 2 },
//     { label: "Open Invoices", value: 12 },
//   ];

//   const workOrders = [
//     { id: "WO-12345", status: "Pending" },
//     { id: "WO-12346", status: "In Progress" },
//     { id: "WO-12347", status: "Completed" },
//   ];

//   return (
//     <DashboardLayout>
//       <div style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
        
//         {/* Page Title */}
//         <h1 style={{ fontSize: "24px", fontWeight: "bold" }}>
//           Vendor Dashboard
//         </h1>

//         {/* KPI Cards */}
//         <div style={{ display: "flex", gap: "16px" }}>
//           {stats.map((stat, index) => (
//             <div
//               key={index}
//               style={{
//                 flex: 1,
//                 backgroundColor: "white",
//                 padding: "16px",
//                 borderRadius: "10px",
//                 boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
//               }}
//             >
//               <p style={{ fontSize: "14px", color: "#6b7280" }}>
//                 {stat.label}
//               </p>
//               <h2 style={{ fontSize: "20px", fontWeight: "bold" }}>
//                 {stat.value}
//               </h2>
//             </div>
//           ))}
//         </div>

//         {/* Main Section (Chart + Side Card) */}
//         <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: "20px" }}>
          
//           {/* Chart Placeholder */}
//           <div
//             style={{
//               backgroundColor: "white",
//               padding: "20px",
//               borderRadius: "10px",
//               boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
//             }}
//           >
//             <h2 style={{ marginBottom: "10px" }}>
//               Work Orders (Last 30 Days)
//             </h2>

//             <div
//               style={{
//                 height: "200px",
//                 border: "1px dashed #ccc",
//                 display: "flex",
//                 alignItems: "center",
//                 justifyContent: "center",
//                 color: "#999",
//               }}
//             >
//               Chart goes here
//             </div>
//           </div>

//           {/* Side Info */}
//           <div
//             style={{
//               backgroundColor: "white",
//               padding: "20px",
//               borderRadius: "10px",
//               boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
//             }}
//           >
//             <h2>Quick Stats</h2>
//             <p style={{ color: "#6b7280", marginTop: "10px" }}>
//               Additional information will go here.
//             </p>
//           </div>
//         </div>

//         {/* Work Orders List */}
//         <div
//           style={{
//             backgroundColor: "white",
//             padding: "20px",
//             borderRadius: "10px",
//             boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
//           }}
//         >
//           <h2 style={{ marginBottom: "10px" }}>
//             Open Work Orders
//           </h2>

//           {workOrders.map((order, index) => (
//             <div
//               key={index}
//               style={{
//                 borderBottom: "1px solid #eee",
//                 padding: "10px 0",
//               }}
//             >
//               <strong>{order.id}</strong> — {order.status}
//             </div>
//           ))}
//         </div>

//       </div>
//     </DashboardLayout>
//   );
// }

// export default DashboardPage;

import DashboardLayout from "../../../layouts/DashboardLayout";
import KpiCard from "../components/dashboard/KpiCard";
import SectionCard from "../components/dashboard/SectionCard";

function DashboardPage() {
  const stats = [
    { label: "Unassigned Work Orders", value: 3 },
    { label: "Pending Jobs", value: 2 },
    { label: "Open Invoices", value: 12 },
  ];

  return (
    <DashboardLayout>
      <div className="flex flex-col gap-6">
        
        {/* Header */}
        <h1 className="text-2xl font-bold">Vendor Dashboard</h1>

        {/* KPI Cards */}
        <div className="flex gap-4">
          {stats.map((stat, index) => (
            <KpiCard key={index} {...stat} />
          ))}
        </div>

        {/* Grid */}
        <div className="grid grid-cols-3 gap-6">
          
          {/* Chart */}
          <div className="col-span-2">
            <SectionCard title="Work Orders (Last 30 Days)">
              <div className="h-40 border border-dashed flex items-center justify-center text-gray-400">
                Chart goes here
              </div>
            </SectionCard>
          </div>

          {/* 🔥 Pending Invoices (Figma-style) */}
          <SectionCard title="Pending Invoices">
            <div className="flex flex-col gap-3">
              
              <div className="flex justify-between text-sm">
                <span>Needs Review</span>
                <span className="font-semibold">50%</span>
              </div>

              <div className="flex justify-between text-sm">
                <span>Submitted</span>
                <span className="font-semibold">33.3%</span>
              </div>

              <div className="flex justify-between text-sm">
                <span>Rejected</span>
                <span className="font-semibold">16.7%</span>
              </div>

              {/* fake donut placeholder */}
              <div className="h-24 flex items-center justify-center text-gray-400 border rounded mt-3">
                Chart
              </div>
            </div>
          </SectionCard>

        </div>

      </div>
    </DashboardLayout>
  );
}

export default DashboardPage;