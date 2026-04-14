import type { WorkOrder } from "../types/workOrder.types";

interface WorkOrdersTableProps {
  workOrders: WorkOrder[];
}

const formatDate = (value?: string | null) => {
  if (!value) return "—";

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "—";

  return date.toLocaleDateString();
};

const formatLabel = (value: string) =>
  value.replace(/_/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());

const formatCurrency = (value?: number | string | null) => {
  if (value === null || value === undefined || value === "") return "—";

  const numericValue =
    typeof value === "number" ? value : Number.parseFloat(String(value));

  if (Number.isNaN(numericValue)) return String(value);

  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(numericValue);
};

const getVendorDisplay = (workOrder: WorkOrder) => {
  if (workOrder.vendor?.name) return workOrder.vendor.name;
  if (workOrder.assigned_vendor) return workOrder.assigned_vendor;
  return "Unassigned";
};

const getWellDisplay = (workOrder: WorkOrder) => {
  if (workOrder.well?.name) return workOrder.well.name;
  if (workOrder.well_id) return workOrder.well_id;
  return "—";
};

const getStatusBadgeStyles = (status: WorkOrder["current_status"]) => {
  switch (status) {
    case "pending":
      return "bg-[#E8EEF5] text-[#2F4F75] border border-[#2F4F75]";
    case "assigned":
      return "bg-[#DCE7F1] text-[#2F4F75] border border-[#2F4F75]";
    case "in_progress":
      return "bg-[#C9D8E6] text-[#2F4F75] border border-[#2F4F75]";
    case "completed":
      return "bg-[#D7E8D9] text-[#2E5A3B] border border-[#2E5A3B]";
    case "cancelled":
      return "bg-[#F3D6D6] text-[#7A2E2E] border border-[#7A2E2E]";
    default:
      return "bg-[#E8EEF5] text-[#2F4F75] border border-[#2F4F75]";
  }
};

const getPriorityBadgeStyles = (priority: WorkOrder["priority"]) => {
  switch (priority) {
    case "low":
      return "bg-[#E8EEF5] text-[#2F4F75] border border-[#2F4F75]";
    case "medium":
      return "bg-[#DCE7F1] text-[#2F4F75] border border-[#2F4F75]";
    case "high":
      return "bg-[#F6E3C7] text-[#8A5A12] border border-[#8A5A12]";
    case "urgent":
      return "bg-[#F3D6D6] text-[#7A2E2E] border border-[#7A2E2E]";
    default:
      return "bg-[#E8EEF5] text-[#2F4F75] border border-[#2F4F75]";
  }
};

export const WorkOrdersTable = ({ workOrders }: WorkOrdersTableProps) => {
  if (workOrders.length === 0) {
    return (
      <section className="rounded-2xl border border-[#2F4F75] bg-white p-8 text-center shadow-lg">
        <h3 className="text-lg font-medium text-[#2F4F75]">No Matching Work Orders</h3>
        <p className="mt-2 text-sm text-[#4A6C8A]">
          Try adjusting your search, filters, or sort options.
        </p>
      </section>
    );
  }

  return (
    <section className="rounded-2xl border border-[#2F4F75] bg-white shadow-lg">
      <div className="border-b border-[#2F4F75] px-6 py-4">
        <h3 className="text-lg font-medium text-[#2F4F75]">Work Order Results</h3>
        <p className="text-sm text-[#4A6C8A]">
          Review current work order details, assignment, and deadlines.
        </p>
      </div>

      <div className="overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead className="bg-[#C9D8E6] text-[#2F4F75]">
            <tr>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Work Order
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Status
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Priority
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Vendor
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Well
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Location
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Due Date
              </th>
              <th className="px-4 py-3 text-xs font-semibold uppercase tracking-wide">
                Estimated Cost
              </th>
            </tr>
          </thead>

          <tbody>
            {workOrders.map((workOrder, index) => (
              <tr
                key={workOrder.work_order_id}
                className={
                  index % 2 === 0
                    ? "border-t border-[#C9D8E6] bg-white align-top"
                    : "border-t border-[#C9D8E6] bg-[#F7FAFC] align-top"
                }
              >
                <td className="px-4 py-4">
                  <div className="font-semibold text-[#2F4F75]">
                    {workOrder.work_order_id}
                  </div>
                  <div className="mt-1 max-w-xs text-xs text-[#4A6C8A]">
                    {workOrder.description || "No description provided"}
                  </div>
                </td>

                <td className="px-4 py-4">
                  <span
                    className={`inline-flex rounded-full px-3 py-1 text-xs font-medium ${getStatusBadgeStyles(
                      workOrder.current_status
                    )}`}
                  >
                    {formatLabel(workOrder.current_status)}
                  </span>
                </td>

                <td className="px-4 py-4">
                  <span
                    className={`inline-flex rounded-full px-3 py-1 text-xs font-medium ${getPriorityBadgeStyles(
                      workOrder.priority
                    )}`}
                  >
                    {formatLabel(workOrder.priority)}
                  </span>
                </td>

                <td className="px-4 py-4 text-[#2F4F75]">
                  {getVendorDisplay(workOrder)}
                </td>

                <td className="px-4 py-4 text-[#2F4F75]">
                  {getWellDisplay(workOrder)}
                </td>

                <td className="px-4 py-4 text-[#2F4F75]">
                  {workOrder.location || "—"}
                </td>

                <td className="px-4 py-4 text-[#2F4F75]">
                  {formatDate(workOrder.due_date)}
                </td>

                <td className="px-4 py-4 text-[#2F4F75]">
                  {formatCurrency(workOrder.estimated_cost)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};