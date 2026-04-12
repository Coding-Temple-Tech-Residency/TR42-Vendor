import DataTable from "../../components/UI/DataTable";

type Props = {
  data: any[];
};

function OpenWorkOrdersTable({ data }: Props) {
  // Dummy data for now (backend will replace this later)
  const columns = [
    { key: "id", label: "Work Order ID" },
    { key: "location", label: "Location" },
    { key: "status", label: "Status" },
    { key: "assignedTo", label: "Assigned To" },
    { key: "dueDate", label: "Due Date" },
  ];

  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={data}
        emptyMessage="No active work orders found"
      />
    </div>
  );
}

export default OpenWorkOrdersTable;