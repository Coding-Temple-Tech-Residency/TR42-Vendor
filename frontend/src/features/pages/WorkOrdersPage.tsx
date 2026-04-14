import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
import { Link } from "react-router-dom";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";
import DonutChart from "../components/UI/DonutChart";

import OpenWorkOrdersTable from "../dashboard/components/OpenWorkOrdersTable";
import CompletedWorkOrdersTable from "../components/misc/CompletedWorkOrderTable";
import { useWorkOrders } from "../hooks/useWorkOrders";

type StatusChartPoint = {
  name: string;
  value: number;
  color: string;
};

export default function WorkOrdersPage() {
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
    // avgCompletion,
    unassignedWorkOrders,
    // assignedWorkOrders,
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
      <div className="space-y-6">
        <PageHeader
          title="Work Orders"
          description="Manage, track, and assign work orders."
        />

        <div className="flex gap-4">
          <Link
            to="/vendor/work-orders/overview"
            className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            View All Work Orders
          </Link>

          <Link
            to="/vendor/work-orders/edit"
            className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            Edit Work Order
          </Link>
        </div>

        {/* KPI Cards */}
        <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
          <KPICard
            title="Overdue"
            value={overDueCount}
            subtitle="Work Orders"
            colorVariant="red"
            badge={{ type: "text", value: "Needs Attention" }}
          />

          <KPICard
            title="Unassigned"
            value={unassignedCount}
            subtitle="Work Orders"
            colorVariant="orange"
            badge={{
              type: "text",
              value: "Needs Assignment",
            }}
          />

          <KPICard
            title="Assigned"
            value={assignedCount}
            subtitle="Not Started"
            colorVariant="gray"
            badge={{ type: "text", value: "Scheduled" }}
          />

          <KPICard
            title="In Progress"
            value={inProgressCount}
            subtitle="Assigned Contractors"
            colorVariant="blue"
            badge={{ type: "text", value: "On Site" }}
          />

          <KPICard
            title="Completed"
            value={completedCount}
            subtitle="This Week"
            colorVariant="green"
            badge={{
              type: "trend",
              value: "12% from last week",
              trendDirection: "up",
            }}
          />

          <KPICard
            title="Invoices Created"
            value="2.4 days"
            subtitle="This month"
            colorVariant="purple"
            badge={{
              type: "trend",
              value: "0.5 days slower",
              trendDirection: "up",
            }}
          />
        </div>

        <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
          <SectionCard title="Work Order Status">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
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
                        <span className="w-24 text-gray-600">{item.name}</span>
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

          <SectionCard title="Work Orders Created">
            <EmptyState
              title="Chart coming soon"
              description="This section will display number of Work Orders created in a month in bar chart form."
            />
          </SectionCard>
        </div>
        <div className="mt-6 grid grid-cols-1">
          <SectionCard title="Unassigned Work Orders">
            {unassignedWorkOrders.length === 0 ? (
              <EmptyState
                title="No unassigned work orders"
                description="This section will contain a table of unassigned Work Orders."
              />
            ) : (
              <OpenWorkOrdersTable data={unassignedWorkOrders} />
            )}
          </SectionCard>
        </div>

        <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
          <SectionCard title="Assigned to Ticket">
            <EmptyState
              title="No Tickets Assigned Work Orders"
              description="This section will contain a table of assigned Work Orders."
            />
          </SectionCard>

          <SectionCard title="In Progress">
            {inProgressWorkOrders.length === 0 ? (
              <EmptyState
                title="No active work orders"
                description="This section will contain a table of in progress Work Orders."
              />
            ) : (
              <OpenWorkOrdersTable data={inProgressWorkOrders} />
            )}
          </SectionCard>
        </div>

        <div className="mt-6 grid grid-cols-1">
          <SectionCard title="Recently Completed">
            {recentlyCompleted.length === 0 ? (
              <EmptyState
                title="No recently completed work orders"
                description="This section will contain a table of recently completed Work Orders."
              />
            ) : (
              <CompletedWorkOrdersTable data={recentlyCompleted} />
            )}
          </SectionCard>
        </div>
      </div>
    </AppLayout>
  );
}
