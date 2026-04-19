interface Column {
  key: string;
  label: string;
  render?: (value: any, row: any) => React.ReactNode; // Added this
}

interface DataTableProps {
  columns: Column[];
  data: any[];
  emptyMessage?: string;
  onRowClick?: (row: any) => void;
}

function DataTable({
  columns,
  data,
  emptyMessage,
  onRowClick,
}: DataTableProps) {
  return (
    <div className="overflow-x-auto rounded-lg border border-slate-200 bg-white">
      <table className="min-w-full text-sm">
        <thead className="bg-slate-50 text-slate-500 uppercase text-[11px] tracking-wider">
          <tr>
            {columns.map((col) => (
              <th
                key={col.key}
                className="px-4 py-3 text-left font-bold border-b border-slate-200"
              >
                {col.label}
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {data.length === 0 ? (
            <tr>
              <td
                colSpan={columns.length}
                className="px-4 py-10 text-center text-slate-400 italic"
              >
                {emptyMessage || "No data available"}
              </td>
            </tr>
          ) : (
            data.map((row, index) => (
              <tr
                key={index}
                className={`border-b border-slate-50 transition-colors ${onRowClick ? "cursor-pointer hover:bg-slate-50" : ""}`}
                onClick={() => onRowClick?.(row)}
              >
                {columns.map((col) => (
                  <td key={col.key} className="px-4 py-3 text-slate-600">
                    {/* KEY CHANGE: If render() exists, use it. Otherwise, use row[key] */}
                    {col.render ? col.render(row[col.key], row) : row[col.key]}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
export default DataTable;
