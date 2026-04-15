import DataTable from "../../components/UI/DataTable";

type Props = {
  data: any[];
};

function AssignContractorTable({ data }: Props) {
  // Dummy data (backend will replace this later)
  const columns = [
    { key: "ticketId", label: "Ticket ID" },
    { key: "issue", label: "Issue" },
    { key: "priority", label: "Priority" },
    { key: "assignedTo", label: "Assigned To" },
    { key: "status", label: "Status" },
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