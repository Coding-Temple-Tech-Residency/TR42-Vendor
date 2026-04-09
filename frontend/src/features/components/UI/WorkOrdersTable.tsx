import StatusBadge from "./StatusBadge";

interface WorkOrder {
  id: string;
  customer: string;
  location: string;
  created: string;
  due: string;
  status: "Completed" | "Pending" | "In Progress" | "Urgent";
}

const data: WorkOrder[] = [
  {
    id: "WO-12345",
    customer: "A.B. Client",
    location: "32.77, -96.79",
    created: "2026-05-15",
    due: "2026-05-16",
    status: "In Progress",
  },
];

const WorkOrdersTable = () => {
  return (
    <div className="bg-white rounded-2xl shadow-sm border">
      <table className="w-full text-sm">
        <thead className="bg-gray-50 text-gray-600">
          <tr>
            <th className="p-3">Work Order</th>
            <th className="p-3">Customer</th>
            <th className="p-3">Location</th>
            <th className="p-3">Created</th>
            <th className="p-3">Due</th>
            <th className="p-3">Status</th>
          </tr>
        </thead>

        <tbody>
          {data.map((order) => (
            <tr key={order.id} className="border-t hover:bg-gray-50">
              <td className="p-3 font-medium">{order.id}</td>
              <td className="p-3">{order.customer}</td>
              <td className="p-3">{order.location}</td>
              <td className="p-3">{order.created}</td>
              <td className="p-3">{order.due}</td>
              <td className="p-3">
                <StatusBadge status={order.status} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default WorkOrdersTable;
