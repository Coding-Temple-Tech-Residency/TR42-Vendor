import DataTable from "../../components/UI/DataTable";

type Props = {
  data: any[];
};

function FraudReviewTable({ data }: Props) {
  // Dummy data — backend will replace this later
  const columns = [
    { key: "caseId", label: "Case ID" },
    { key: "vendor", label: "Vendor" },
    { key: "flag", label: "Flag Type" },
    { key: "score", label: "Risk Score" },
    { key: "status", label: "Status" },
  ];

  // Risk color logic
  const getRiskColor = (score: number) => {
    if (score < 33) return "text-green-600";
    if (score < 66) return "text-yellow-600";
    return "text-red-600";
  };

  // Transform data so DataTable can render styled cells
  const formattedData = data.map((row) => ({
    ...row,
    score: (
      <span className={`font-semibold ${getRiskColor(row.score)}`}>
        {row.score}%
      </span>
    ),
    status: (
      <span className={`font-semibold ${getRiskColor(row.score)}`}>
        {row.status}
      </span>
    ),
  }));

  return (
    <div className="w-full">
      <DataTable
        columns={columns}
        data={formattedData}
        emptyMessage="No fraud review cases available"
      />
    </div>
  );
}

export default FraudReviewTable;