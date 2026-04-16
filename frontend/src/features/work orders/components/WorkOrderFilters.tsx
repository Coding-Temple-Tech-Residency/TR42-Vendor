import type {
  PriorityStatus,
  WorkOrderSortOptions,
  WorkOrderStatus,
} from "../types/workOrder.types";

interface WorkOrderFilterProps {
  searchTerm: string;
  statusFilter: string;
  priorityFilter: WorkOrderStatus | "all";
  assignmentFilter: "all" | "assigned" | "unassigned";
  sortBy: WorkOrderSortOptions;
  onSearchChange: (value: string) => void;
  onStatusChange: (value: WorkOrderStatus | "all") => void;
  onPriorityChange: (value: PriorityStatus | "all") => void;
  onAssignmentChange: (value: "all" | "assigned" | "unassigned") => void;
  onSortChange: (value: WorkOrderSortOptions) => void;
  onReset: () => void;
}

export const WorkOrderFilters = ({
  searchTerm,
  statusFilter,
  priorityFilter,
  assignmentFilter,
  sortBy,
  onSearchChange,
  onStatusChange,
  onPriorityChange,
  onAssignmentChange,
  onSortChange,
  onReset,
}: WorkOrderFilterProps) => {
  return (
    <section className="rounded-xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg font-medium text-[#2F4F75]">
          Filter Work Orders
        </h3>
        <p className="text-sm text-[#4A6C8A]">
          Search, sort, and narrow results based on work order details.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md sm:col-span-2 xl:col-span-3">
          <label
            htmlFor="work-order-search"
            className="text--s font-medium uppercase tracking-wide text-[#2F4F75]"
          >
            Search
          </label>
          <input
            id="work-order-search"
            type="text"
            value={searchTerm}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder="Search by ID, description, comments, vendor, well..."
            className="mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none"
          />
        </div>

        <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
          <label
            htmlFor="status-filter"
            className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]"
          >
            Status
          </label>
          <select
            id="status-filter"
            value={statusFilter}
            onChange={(e) =>
              onStatusChange(e.target.value as WorkOrderStatus | "all")
            }
            className="mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none"
          >
            <option value="all">All Statuses</option>
            <option value="pending">Pending</option>
            <option value="assigned">Assigned</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
            <option value="cancelled">Cancelled</option>
          </select>
        </div>

        <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
          <label
            htmlFor="priority-filter"
            className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]"
          >
            Priority
          </label>
          <select
            id="priority-filter"
            value={priorityFilter}
            onChange={(e) =>
              onPriorityChange(e.target.value as PriorityStatus | "all")
            }
            className="mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none"
          >
            <option value="all">All Priority</option>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
            <option value="urgent">Urgent</option>
          </select>
        </div>

        <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
          <label
            htmlFor="assigned-filter"
            className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]"
          >
            Assignment
          </label>
          <select
            id="assignment-filter"
            value={assignmentFilter}
            onChange={(e) =>
              onAssignmentChange(
                e.target.value as "all" | "assignment" | "unassigned",
              )
            }
            className="mt-2 w-full rounded border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none"
          >
            <option value="all">All</option>
            <option value="assigned">Assigned</option>
            <option value="unassigned">Unassigned</option>
          </select>
        </div>

        <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md sm:col-span-2 xl:col-span-2">
          <label
            htmlFor="sort-by"
            className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]"
          >
            Sort
          </label>
          <select
            id="sort-by"
            value={sortBy}
            onChange={(e) =>
              onSortChange(e.target.value as WorkOrderSortOptions)
            }
          >
            <option value="created_at_desc">Newest Created</option>
            <option value="due_date_asc">Due Date: Soonest First</option>
            <option value="due_date_desc">Due Date: Lasest First</option>
            <option value="priority_desc">Priority: Highest First</option>
            <option value="status_asc">Status A-Z</option>
            <option value="location_asc"> Location A-Z</option>
          </select>
        </div>
      </div>

      <div className="mt-6 flex justify-end">
        <button 
            type="button"
            onClick={onReset}
            className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white transition hover:gb-[#4A6C8A]"
        >
            Reset Filters
        </button>
      </div>
    </section>
  );
};
