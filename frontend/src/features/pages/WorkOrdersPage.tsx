import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";

import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

// Reusable UI components
import DonutChart from "../components/UI/DonutChart";
import OpenWorkOrdersTable from "../components/UI/OpenWorkOrdersTable";
import AssignContractorTable from "../components/UI/AssignContractorTable";
import FraudReviewTable from "../components/UI/FraudReviewTable";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function WorkOrdersPage() {
  const kpiData = {
    overdue: 5,
    unassigned: 12,
    assigned: 8,
    inProgress: 21,
    completed: 45,
    avgCompletion: "2.4 days",
  };

  const statusChartData = [
    { name: "Overdue", value: 5, color: "#EF4444" },
    { name: "Unassigned", value: 12, color: "#F59E0B" },
    { name: "Assigned", value: 8, color: "#3B82F6" },
    { name: "In Progress", value: 21, color: "#1E3A5F" },
    { name: "Completed", value: 45, color: "#10B981" },
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

  const unassignedWorkOrders = [];
  const assignedWorkOrders = [];
  const inProgressWorkOrders = [];
  const recentlyCompleted = [];

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
          <div className="text-3xl font-bold">{kpiData.overdue}</div>
        </SectionCard>

        <SectionCard title="Unassigned" subtitle="Needs assignment">
          <div className="text-3xl font-bold">{kpiData.unassigned}</div>
        </SectionCard>

        <SectionCard title="Assigned" subtitle="Not started">
          <div className="text-3xl font-bold">{kpiData.assigned}</div>
        </SectionCard>

        <SectionCard title="In Progress" subtitle="On site">
          <div className="text-3xl font-bold">{kpiData.inProgress}</div>
        </SectionCard>

        <SectionCard title="Completed" subtitle="This week">
          <div className="text-3xl font-bold">{kpiData.completed}</div>
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
                  const total = statusChartData.reduce((sum, i) => sum + i.value, 0);
                  const percentage = Math.round((item.value / total) * 100);

                  return (
                    <div key={item.name} className="flex items-center gap-3 text-sm">
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
            <OpenWorkOrdersTable />
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
            <AssignContractorTable />
          )}
        </SectionCard>

        <SectionCard title="In Progress">
          {inProgressWorkOrders.length === 0 ? (
            <EmptyState
              title="No active work orders"
              description="Work orders currently in progress will appear here."
            />
          ) : (
            <OpenWorkOrdersTable />
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
            <FraudReviewTable />
          )}
        </SectionCard>
      </div>
    </AppLayout>
  );
}

export default WorkOrdersPage;