import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/SideBar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import SectionCard from "../../components/UI/SectionCard";
import { useState } from "react";
import { WorkOrderFilters } from "../components/WorkOrderFilters";
import { WorkOrdersTable } from "../components/WorkOrderTable";
import { useFilteredWorkOrders } from "../hooks/useFilteredWorkOrders";
import type {
  PriorityStatus,
  WorkOrder,
  WorkOrderSortOption,
  WorkOrderStatus,
} from "../types/workOrder.types";

export default function WorkOrderOverviewPage() {
  // 🔹 EMPTY DATA FOR NOW (safe for backend not ready)
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([]);

  const [searchTerm, setSearchTerm] = useState("");
  const [statusFilter, setStatusFilter] = useState<WorkOrderStatus | "all">(
    "all"
  );
  const [priorityFilter, setPriorityFilter] = useState<PriorityStatus | "all">(
    "all"
  );
  const [assignmentFilter, setAssignmentFilter] = useState<
    "all" | "assigned" | "unassigned"
  >("all");
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

              <WorkOrdersTable workOrders={filteredWorkOrders} />
            </div>
          </SectionCard>
        </div>
      </div>
    </AppLayout>
  );
}