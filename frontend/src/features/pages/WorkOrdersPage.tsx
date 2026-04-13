import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";

import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

// Reusable UI components
import DonutChart from "../components/UI/DonutChart";
import OpenWorkOrdersTable from "../dashboard/components/OpenWorkOrdersTable";
import AssignContractorTable from "../dashboard/components/AssignContractorTable";
import FraudReviewTable from "../dashboard/components/FraudReviewTable";

import { Link } from "react-router-dom";

//Reusable hooks
import { useWorkOrders } from "../hooks/useWorkOrders";

/* 
  Questions:
  - Do we want to the bar graph to show work orders created or completed? Or both as separate charts?
  - Do we want the work order rows to be clickable to navigate to a work order details page? I created a placeholder route in the frontend for this already
  - How do we want to format Work Order IDs?
  - Is the Assigned - Not Started table necessary? I think it would be more efficient to just have one table for all non-completed work orders with a status column instead of splitting into unassigned vs assigned. We can also add a filter on the table to filter by status if needed.
  - Is the Fraud Review Table supposed to be on this page? 
  - In regards to a work order being "assigned", do we mean its assigned to a contractor? 
    If so this might not make sense since we're assigning tickets to contractors. What should "Assigned To" show?
  - Should we add a table for overdue work orders? Or just show the count of overdue work orders without the details since they can be filtered in the main work orders page? Should the date in due date change to OVERDUE?
*/


import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import CompletedWorkOrdersTable from "../components/misc/CompletedWorkOrderTable";

function WorkOrdersPage() {
  const kpiData = {
    // overdue: 5,
    // unassigned: 12,
    // assigned: 8,
    // inProgress: 21,
    // completed: 45,
    avgCompletion: "2.4 days",
  };

  const {
    loading,
    unassignedCount,
    error,
    inProgressCount,
    assignedCount,
    completedInWeekCount,
    completedCount,
    unassignedWorkOrders,
    assignedWorkOrders,
    inProgressWorkOrders,
    recentlyCompleted,
    overDueCount,
  } = useWorkOrders({ page: 1, perPage: 50, current_status: "all" });

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

  // const openWorkOrders = workOrders;
  const statusChartData = [
    { name: "Overdue", value: overDueCount, color: "#EF4444" },
    { name: "Unassigned", value: unassignedCount, color: "#F59E0B" },
    { name: "Assigned", value: assignedCount, color: "#3B82F6" },
    { name: "In Progress", value: inProgressCount, color: "#1E3A5F" },
    { name: "Completed", value: completedCount, color: "#10B981" },
  ];

  const workOrdersCreated = [
    { week: "Week 1", count: 14 },
    { week: "Week 2", count: 19 },
    { week: "Week 3", count: 23 },
    { week: "Week 4", count: 17 },
  ];

  // BarChart
  const SimpleBarChart = ({ data }) => {
    return (
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <XAxis dataKey="week" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" radius={[6, 6, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    );
  };

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Work Orders"
        description="Manage, track, and assign work orders."
      />

      {/* KPI cards */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-6">
        <SectionCard title="Overdue" subtitle="Needs attention">
          <div className="text-3xl font-bold">{overDueCount}</div>
        </SectionCard>

        <SectionCard title="Unassigned" subtitle="Needs assignment">
          <Link
            to="/vendor/work-orders"
            className="text-3xl hover:opacity-75 transition-opacity font-bold cursor-pointer"
          >
            <div>{unassignedCount}</div>
          </Link>
        </SectionCard>

        <SectionCard title="Assigned" subtitle="Not started">
          <div className="text-3xl font-bold">{assignedCount}</div>
        </SectionCard>

        <SectionCard title="In Progress" subtitle="On site">
          <div className="text-3xl font-bold">{inProgressCount}</div>
        </SectionCard>

        <SectionCard title="Completed" subtitle="This week">
          <div className="text-3xl font-bold">{completedInWeekCount}</div>
        </SectionCard>

        <SectionCard title="Avg. Completion" subtitle="This month">
          <div className="text-3xl font-bold">{kpiData.avgCompletion}</div>
        </SectionCard>
      </div>

      {/* Charts Section */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
        {/* Donut + Legend */}
        <SectionCard title="Work Order by Status">
          <div className="flex items-center justify-between">
            <div className="flex-1 flex justify-center">
              <div className="space-y-3">
                {statusChartData.map((item) => {
                  const total = statusChartData.reduce(
                    (sum, i) => sum + i.value,
                    0,
                  );
                  const percentage = Math.round((item.value / total) * 100);

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

            <div className="flex-1 flex justify-center">
              <div className="h-56 w-56">
                <DonutChart data={statusChartData} />
              </div>
            </div>
          </div>
        </SectionCard>

        <SectionCard title="Work Orders Created (per week)">
          <SimpleBarChart data={workOrdersCreated} />
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
            <AssignContractorTable data={assignedWorkOrders}/>
          )}
        </SectionCard>

        <SectionCard title="In Progress">
          {inProgressWorkOrders.length === 0 ? (
            <EmptyState
              title="No active work orders"
              description="Work orders currently in progress will appear here."
            />
          ) : (
            <OpenWorkOrdersTable data={inProgressWorkOrders}/>
          )}
        </SectionCard>
      </div>

      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Recently Completed">
          {recentlyCompleted.length === 0 ? (
            <EmptyState
              title="No completed work orders"
              description="Completed work orders will appear here."
            />
          ) : (
            // <FraudReviewTable />
            <CompletedWorkOrdersTable data={recentlyCompleted}/>
          )}
        </SectionCard>
      </div>
    </AppLayout>
  );
}

export default WorkOrdersPage;
