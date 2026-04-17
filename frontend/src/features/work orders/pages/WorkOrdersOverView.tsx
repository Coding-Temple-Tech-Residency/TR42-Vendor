import { useState, useMemo } from "react";
import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/Sidebar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import SectionCard from "../../components/UI/SectionCard";
import { WorkOrderFilters } from "../components/WorkOrderFilters";
import { WorkOrdersTable } from "../components/WorkOrderTable";
import { useFilteredWorkOrders } from "../hooks/useFilteredWorkOrders";
import { useWorkOrders } from "../hooks/useWorkOrders";
import { useSearchParams } from "react-router-dom";
import type {
  PriorityStatus,
  WorkOrder,
  WorkOrderSortOption,
  WorkOrderStatus,
} from "../types/workOrder.types";
import type { WorkOrderRow } from "../../auth/services/workOrderService";

const STATUS_MAP: Record<string, WorkOrderStatus> = {
  Pending: "pending",
  Assigned: "assigned",
  "In Progress": "in_progress",
  Completed: "completed",
  Cancelled: "cancelled",
};

const PRIORITY_MAP: Record<string, PriorityStatus> = {
  Low: "low",
  Medium: "medium",
  High: "high",
  Urgent: "urgent",
};

function toWorkOrder(row: WorkOrderRow): WorkOrder {
  return {
    id: row.id,
    assigned_vendor: row.assignedVendorId,
    completed_at: row.completedAt,
    description: row.description,
    due_date: row.estimatedEndDate,
    estimated_start_date: row.estimatedStartDate,
    estimated_end_date: row.estimatedEndDate,
    current_status: STATUS_MAP[row.currentStatus] ?? "pending",
    priority: PRIORITY_MAP[row.priority] ?? "low",
    comments: row.comments,
    location: row.location,
    estimated_cost: null,
    estimated_duration: null,
    well_id: null,
    updated_by: "",
    created_at: row.createdAt,
    updated_at: null,
  };
}

export default function WorkOrderOverviewPage() {
  const [searchParams, setSearchParams] = useSearchParams();
  const initialOpenWorkOrderId = searchParams.get("openWorkOrderId");

  const { workOrders: rawWorkOrders, loading, error } = useWorkOrders({
    page: 1,
    perPage: 100,
    status: "all",
    scope: "vendor",
  });

  const workOrders = useMemo(
    () => rawWorkOrders.map(toWorkOrder),
    [rawWorkOrders],
  );

  const [searchTerm, setSearchTerm] = useState("");
  const [statusFilter, setStatusFilter] = useState<WorkOrderStatus | "all">("all");
  const [priorityFilter, setPriorityFilter] = useState<PriorityStatus | "all">("all");
  const [assignmentFilter, setAssignmentFilter] = useState<"all" | "assigned" | "unassigned">("all");
  const [sortBy, setSortBy] = useState<WorkOrderSortOption>("created_at_desc");

  const filteredWorkOrders = useFilteredWorkOrders({
    workOrders,
    searchTerm,
    statusFilter,
    priorityFilter,
    assignmentFilter,
    sortBy,
  });

  const handleResetFilters = () => {
    setSearchTerm("");
    setStatusFilter("all");
    setPriorityFilter("all");
    setAssignmentFilter("all");
    setSortBy("created_at_desc");
  };

  const handleInitialOpenHandled = () => {
    const next = new URLSearchParams(searchParams);
    next.delete("openWorkOrderId");
    setSearchParams(next, { replace: true });
  };

  if (loading) {
    return (
      <AppLayout sidebar={<Sidebar />} topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}>
        <div className="p-6 text-slate-600">Loading work orders...</div>
      </AppLayout>
    );
  }

  if (error) {
    return (
      <AppLayout sidebar={<Sidebar />} topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}>
        <div className="p-6 text-red-500">{error}</div>
      </AppLayout>
    );
  }

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader
          title="Work Orders Overview"
          description="View all current and past Work Orders."
        />

        <div className="grid grid-cols-1">
          <SectionCard title="All Work Orders">
            <div className="space-y-6">
              <WorkOrderFilters
                searchTerm={searchTerm}
                statusFilter={statusFilter}
                priorityFilter={priorityFilter}
                assignmentFilter={assignmentFilter}
                sortBy={sortBy}
                onSearchChange={setSearchTerm}
                onStatusChange={setStatusFilter}
                onPriorityChange={setPriorityFilter}
                onAssignmentChange={setAssignmentFilter}
                onSortChange={setSortBy}
                onReset={handleResetFilters}
              />

              <div className="text-sm text-[#4A6C8A]">
                Showing{" "}
                <span className="font-semibold text-[#2F4F75]">
                  {filteredWorkOrders.length}
                </span>{" "}
                of{" "}
                <span className="font-semibold text-[#2F4F75]">
                  {workOrders.length}
                </span>{" "}
                work orders
              </div>

              <WorkOrdersTable
                workOrders={filteredWorkOrders}
                initialOpenWorkOrderId={initialOpenWorkOrderId}
                onInitialOpenHandled={handleInitialOpenHandled}
              />
            </div>
          </SectionCard>
        </div>
      </div>
    </AppLayout>
  );
}
