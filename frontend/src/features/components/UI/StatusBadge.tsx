type Status = "Completed" | "Pending" | "In Progress" | "Urgent" | "Cancelled";

interface StatusBadgeProps {
  status: Status;
}

const StatusBadge = ({ status }: StatusBadgeProps) => {
  const baseStyles = "px-2 py-1 rounded-full text-xs font-medium";

  const statusStyles: Record<Status, string> = {
    Completed: "bg-green-100 text-green-700",
    Pending: "bg-yellow-100 text-yellow-700",
    "In Progress": "bg-blue-100 text-blue-700",
    Urgent: "bg-red-100 text-red-700",
    Cancelled: "bg-gray-200 text-gray-600",
  };

  return (
    <span className={`${baseStyles} ${statusStyles[status]}`}>{status}</span>
  );
};

export default StatusBadge;
