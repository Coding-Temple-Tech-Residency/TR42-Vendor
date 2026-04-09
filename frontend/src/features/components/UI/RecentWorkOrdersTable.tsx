import StatusBadge from "../workorders/StatusBadge";

const data = [
  {
    id: "#1023",
    title: "Pipeline Inspection",
    customer: "Exxon Mobil",
    date: "2026-04-01",
    status: "In Progress",
  },
  {
    id: "#1024",
    title: "Valve Replacement",
    customer: "Chevron",
    date: "2026-04-02",
    status: "Pending",
  },
  {
    id: "#1025",
    title: "Leak Repair",
    customer: "Shell",
    date: "2026-04-03",
    status: "Completed",
  },
];

const RecentWorkOrders = () => {
  return (
    <div className="bg-white rounded-2xl shadow-sm border p-4">
      {/* Header */}
      <div className="flex justify-between items-center mb-4">
        <h3 className="font-semibold">Recent Work Orders</h3>
        <button className="text-sm text-blue-600 hover:underline">
          View All
        </button>
      </div>

      {/* Table */}
      <table className="w-full text-sm">
        <thead className="text-gray-500">
          <tr>
            <th className="text-left py-2">ID</th>
            <th className="text-left py-2">Title</th>
            <th className="text-left py-2">Customer</th>
            <th className="text-left py-2">Date</th>
            <th className="text-left py-2">Status</th>
          </tr>
        </thead>

        <tbody>
          {data.map((order, i) => (
            <tr key={i} className="border-t hover:bg-gray-50 cursor-pointer">
              <td className="py-2">{order.id}</td>
              <td className="py-2">{order.title}</td>
              <td className="py-2">{order.customer}</td>
              <td className="py-2">{order.date}</td>
              <td className="py-2">
                <StatusBadge status={order.status as any} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RecentWorkOrders;
