import StatusBadge from "./StatusBadge";

interface WorkOrder {
  id: string;
  title: string;
  customer: string;
  location: string;
  date: string;
  priority: "High" | "Medium" | "Low";
  status: "Pending" | "In Progress" | "Completed";
  description?: string;
}

interface Props {
  order: WorkOrder;
  onClose?: () => void;
}

const WorkOrderDetails = ({ order, onClose }: Props) => {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-sm border space-y-4">
      {/* Header */}
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold">Work Order Details</h2>
        {onClose && (
          <button
            onClick={onClose}
            className="text-sm text-gray-500 hover:text-gray-700"
          >
            Close
          </button>
        )}
      </div>

      {/* Main Info */}
      <div className="grid grid-cols-2 gap-4 text-sm">
        <p>
          <strong>ID:</strong> {order.id}
        </p>
        <p>
          <strong>Customer:</strong> {order.customer}
        </p>
        <p>
          <strong>Location:</strong> {order.location}
        </p>
        <p>
          <strong>Date:</strong> {order.date}
        </p>
        <p>
          <strong>Status:</strong> <StatusBadge status={order.status} />
        </p>
        <p>
          <strong>Priority:</strong>{" "}
          <span
            className={`px-2 py-1 rounded-full text-xs ${
              order.priority === "High"
                ? "bg-red-100 text-red-700"
                : order.priority === "Medium"
                  ? "bg-yellow-100 text-yellow-700"
                  : "bg-green-100 text-green-700"
            }`}
          >
            {order.priority}
          </span>
        </p>
      </div>

      {/* Description */}
      <div>
        <h3 className="font-medium mb-1">Description</h3>
        <p className="text-gray-600 text-sm">
          {order.description || "No description provided."}
        </p>
      </div>
    </div>
  );
};

export default WorkOrderDetails;
