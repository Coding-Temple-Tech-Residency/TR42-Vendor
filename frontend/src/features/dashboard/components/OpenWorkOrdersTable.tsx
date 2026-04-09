import DataTable from "../../components/UI/DataTable";

function OpenWorkOrdersTable() {
  // Dummy data for now (backend will replace this later)
  const columns = [
    { key: "id", label: "Work Order ID" },
    { key: "location", label: "Location" },
    { key: "status", label: "Status" },
    { key: "assignedTo", label: "Assigned To" },
    { key: "dueDate", label: "Due Date" },
  ];

  const data = [
    {
      id: "WO-1023",
      location: "Dallas, TX",
      status: "In Progress",
      assignedTo: "John Smith",
      dueDate: "Apr 12, 2026",
    },
    {
      id: "WO-1024",
      location: "Fort Worth, TX",
      status: "Pending",
      assignedTo: "Unassigned",
      dueDate: "Apr 15, 2026",
    },
    {
      id: "WO-1025",
      location: "Plano, TX",
      status: "Completed",
      assignedTo: "Sarah Lee",
      dueDate: "Apr 10, 2026",
    },
  ];

  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={data}
        emptyMessage="No open work orders found"
      />
    </div>
  );
}
export default OpenWorkOrdersTable;