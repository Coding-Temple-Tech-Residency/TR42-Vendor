import DataTable from "../../components/UI/DataTable";
import { useNavigate } from "react-router-dom";
import type { WorkOrderRow } from "../../auth/services/workOrderService";

type Props = {
  data: WorkOrderRow[];
};

function OpenWorkOrdersTable({ data }: Props) {
  const navigate = useNavigate();
  const columns = [
    { key: "id", label: "Work Order ID" },
    { key: "serviceType", label: "Service" },
    { key: "locationSummary", label: "Location" },
    { key: "currentStatus", label: "Status" },
    { key: "assignmentLabel", label: "Assignment" },
    { key: "scheduleWindow", label: "Schedule" },
    { key: "priority", label: "Priority" },
  ];

  const handleRowClick = (row: WorkOrderRow) => {
    navigate(`/vendor/work-orders/${row.id}`);
  };
  
  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={data}
        emptyMessage="No active work orders found"
        onRowClick={handleRowClick}
      />
    </div>
  );
}

export default OpenWorkOrdersTable;