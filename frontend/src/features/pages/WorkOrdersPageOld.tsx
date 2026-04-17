import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";

import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

import DonutChart from "../components/UI/DonutChart";
import OpenWorkOrdersTable from "../dashboard/components/OpenWorkOrdersTable";
import CompletedWorkOrdersTable from "../components/misc/CompletedWorkOrderTable";

import { Link } from "react-router-dom";

// DONT DELETE THIS YET PLEASE
//MIGHT NEED TO REFERENCE THIS IN THE FUTURE FOR HOOKS OR SOMETHING

//Reusable hooks
import { useWorkOrders } from "../work orders/hooks/useWorkOrders";

type StatusChartPoint = {
  name: string;
  value: number;
  color: string;
};

function WorkOrdersPage() {
  const {
    // activeWorkOrders,
    loading,
    unassignedCount,
    error,
    inProgressCount,
    assignedCount,
    completedInWeekCount,
    completedCount,
    // recurringCount,
    avgCompletion,
    unassignedWorkOrders,
    assignedWorkOrders,
    inProgressWorkOrders,
    recentlyCompleted,
    overDueCount,
    // overDueWorkOrders,
  } = useWorkOrders({ page: 1, perPage: 100, status: "all", scope: "vendor" });

  if (loading) {
    return (
      <AppLayout
        sidebar={<Sidebar />}
        topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
      >
        <div className="p-6 text-gray-600">Loading work orders...</div>
      </AppLayout>
    );
  }

  if (error) {
    return (
      <AppLayout
        sidebar={<Sidebar />}
        topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
      >
        <div className="p-6 text-red-500">{error}</div>
      </AppLayout>
    );
  }

  const statusChartData: StatusChartPoint[] = [
    { name: "Overdue", value: overDueCount, color: "#EF4444" },
    { name: "Unassigned", value: unassignedCount, color: "#F59E0B" },
    { name: "Assigned", value: assignedCount, color: "#3B82F6" },
    { name: "In Progress", value: inProgressCount, color: "#1E3A5F" },
    { name: "Completed", value: completedCount, color: "#10B981" },
  ];

  const totalStatusCount = statusChartData.reduce(
    (sum, item) => sum + item.value,
    0,
  );

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Work Orders"
        description="Manage, track, and assign work orders."
      />

      <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3">
        <SectionCard title="Unassigned" subtitle="Needs assignment">
          <Link
            to="/vendor/work-orders"
            className="text-3xl hover:opacity-75 transition-opacity font-bold cursor-pointer"
          >
            {unassignedCount}
          </Link>
        </SectionCard>

        <SectionCard title="Assigned" subtitle="Ready to start">
          <div className="text-3xl font-bold text-slate-900">
            {assignedCount}
          </div>
        </SectionCard>

        <SectionCard title="Overdue" subtitle="Past estimated end">
          <div className="text-3xl font-bold text-red-600">{overDueCount}</div>
        </SectionCard>

        <SectionCard title="In Progress" subtitle="On site">
          <div className="text-3xl font-bold">{inProgressCount}</div>
        </SectionCard>

        <SectionCard title="Completed" subtitle={`Total: ${completedCount}`}>
          <div className="text-3xl font-bold">{completedInWeekCount}</div>
        </SectionCard>

        <SectionCard title="Avg. Completion" subtitle="Completed orders">
          <div className="text-3xl font-bold text-slate-900">
            {avgCompletion}
          </div>
        </SectionCard>
      </div>

      {/* Charts Section */}
      <div className="mt-6 grid grid-cols-1 gap-6 lg:grid-cols-2">
        {/* Donut + Legend */}
        <SectionCard title="Work Order by Status">
          <div className="flex flex-col gap-6 xl:flex-row xl:items-center xl:justify-between">
            <div className="flex flex-1 justify-center">
              <div className="space-y-3">
                {statusChartData.map((item) => {
                  const percentage = totalStatusCount
                    ? Math.round((item.value / totalStatusCount) * 100)
                    : 0;

                  return (
                    <div
                      key={item.name}
                      className="flex items-center gap-3 text-sm"
                    >
                      <span
                        className="h-2.5 w-2.5 rounded-full"
                        style={{ backgroundColor: item.color }}
                      />
                      <span className="text-gray-600 w-24">{item.name}</span>
                      <span className="font-medium text-gray-900">
                        {item.value} ({percentage}%)
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="flex flex-1 justify-center">
              <div className="h-56 w-56">
                {totalStatusCount === 0 ? (
                  <EmptyState
                    title="No status data"
                    description="Status chart will appear once work orders are available."
                  />
                ) : (
                  <DonutChart data={statusChartData} />
                )}
              </div>
            </div>
          </div>
        </SectionCard>

        <SectionCard title="Work Order Timeline">
          <EmptyState
            title="Trend chart disabled"
            description="Weekly work order trend reporting is not wired in yet."
          />
        </SectionCard>
      </div>

      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Unassigned Work Orders">
          {unassignedWorkOrders.length === 0 ? (
            <EmptyState
              title="No unassigned work orders"
              description="Work orders needing assignment will appear here."
            />
          ) : (
            <OpenWorkOrdersTable data={unassignedWorkOrders} />
          )}
        </SectionCard>
      </div>

      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
        <SectionCard title="Assigned – Not Started">
          {assignedWorkOrders.length === 0 ? (
            <EmptyState
              title="No assigned work orders"
              description="Assigned work orders will appear here."
            />
          ) : (
            <OpenWorkOrdersTable data={assignedWorkOrders} />
          )}
        </SectionCard>

        <SectionCard title="In Progress">
          {inProgressWorkOrders.length === 0 ? (
            <EmptyState
              title="No active work orders"
              description="Work orders currently in progress will appear here."
            />
          ) : (
            <OpenWorkOrdersTable data={inProgressWorkOrders} />
          )}
        </SectionCard>
      </div>

      <div className="mt-6 grid grid-cols-1">
        <SectionCard
          title="Recently Completed"
          subtitle="Latest completed work orders"
        >
          {recentlyCompleted.length === 0 ? (
            <EmptyState
              title="No completed work orders"
              description="Completed work orders will appear here."
            />
          ) : (
            <CompletedWorkOrdersTable data={recentlyCompleted} />
          )}
        </SectionCard>
      </div>
    </AppLayout>
  );
}

export default WorkOrdersPage;
