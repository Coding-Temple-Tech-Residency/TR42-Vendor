import DataTable from "../UI/DataTable";
import { useNavigate } from "react-router-dom";

type Props = {
  data: any[];
};

function CompletedWorkOrdersTable({ data }: Props) {
  const navigate = useNavigate();
  // Dummy data for now (backend will replace this later)
  const columns = [
    { key: "id", label: "Work Order ID" },
    { key: "location", label: "Location" },
    { key: "current_status", label: "Status" },
    { key: "assignedTo", label: "Assigned To" },
    { key: "dueDate", label: "Due Date" },
    { key: "completed_at", label: "Completed At" },
  ];

  // Handle row click to navigate to work order details page when created in future
  const handleRowClick = (row: any) => {
    navigate(`/vendor/work-orders/${row.id}`);
  };
  
  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={data}
        emptyMessage="No recentl completed work orders found"
        onRowClick={handleRowClick}
      />
    </div>
  );
}

export default CompletedWorkOrdersTable;