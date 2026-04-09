import DataTable from "../../components/UI/DataTable";

function AssignContractorTable() {
  // Dummy data (backend will replace this later)
  const columns = [
    { key: "ticketId", label: "Ticket ID" },
    { key: "issue", label: "Issue" },
    { key: "priority", label: "Priority" },
    { key: "assignedTo", label: "Assigned To" },
    { key: "status", label: "Status" },
  ];

  const data = [
    {
      ticketId: "TCK-2041",
      issue: "HVAC not cooling",
      priority: "High",
      assignedTo: "Unassigned",
      status: "Pending Assignment",
    },
    {
      ticketId: "TCK-2042",
      issue: "Leaking pipe",
      priority: "Medium",
      assignedTo: "Michael Brown",
      status: "In Progress",
    },
    {
      ticketId: "TCK-2043",
      issue: "Electrical outage",
      priority: "High",
      assignedTo: "Unassigned",
      status: "Pending Assignment",
    },
  ];

  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={data}
        emptyMessage="No contractor assignments available"
      />
    </div>
  );
}
export default AssignContractorTable;