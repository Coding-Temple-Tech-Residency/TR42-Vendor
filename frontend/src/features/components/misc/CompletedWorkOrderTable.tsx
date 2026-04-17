import DataTable from "../UI/DataTable";
import { useNavigate } from "react-router-dom";
import type { WorkOrderRow } from "../../auth/services/workOrderService";

type Props = {
  data: WorkOrderRow[];
};

function CompletedWorkOrdersTable({ data }: Props) {
  const navigate = useNavigate();
  // Dummy data for now (backend will replace this later)
  const columns = [
    { key: "id", label: "Work Order ID" },
    { key: "serviceType", label: "Service" },
    { key: "locationSummary", label: "Location" },
    { key: "quantityLabel", label: "Quantity" },
    { key: "recurrenceLabel", label: "Recurrence" },
    { key: "completedAtLabel", label: "Completed At" },
  ];

  const handleRowClick = (row: WorkOrderRow) => {
    const params = new URLSearchParams({ openWorkOrderId: row.id });
    navigate(`/vendor/work-orders/overview?${params.toString()}`);
  };

  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={data}
        emptyMessage="No recently completed work orders found"
        onRowClick={handleRowClick}
      />
    </div>
  );
}

export default CompletedWorkOrdersTable;
