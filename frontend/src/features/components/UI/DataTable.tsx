import React from "react";

type Column<T> = {
  header: string;
  accessor: keyof T;
  render?: (value: T[keyof T], row: T) => React.ReactNode;
};

type DataTableProps<T> = {
  columns: Column<T>[];
  data: T[];
};

function DataTable<T extends Record<string, unknown>>({
  columns,
  data,
}: DataTableProps<T>) {
  return (
    <div className="w-full overflow-x-auto bg-white rounded-2xl shadow-sm border">
      <table className="w-full text-sm">
        <thead className="bg-gray-100 text-left">
          <tr>
            {columns.map((col, index) => (
              <th key={index} className="p-3 font-semibold">
                {col.header}
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {data.map((row, rowIndex) => (
            <tr key={rowIndex} className="border-t hover:bg-gray-50 transition">
              {columns.map((col, colIndex) => {
                const value = row[col.accessor];

                return (
                  <td key={colIndex} className="p-3">
                    {col.render ? col.render(value, row) : String(value)}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>

      {data.length === 0 && (
        <div className="p-4 text-center text-gray-500">No data available</div>
      )}
    </div>
  );
}

export default DataTable;
