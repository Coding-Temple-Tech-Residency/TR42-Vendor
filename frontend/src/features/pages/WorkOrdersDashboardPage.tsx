import React from "react";
import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KpiCard";
import SectionCard from "../components/UI/SectionCard";
import DataTable from "../components/UI/DataTable";
import DonutChart from "../components/UI/DonutChart";
import BarChart from "../components/UI/BarChart";

export default function WorkOrdersPage() {
  const workOrderStatusData = [
    { name: "Unassigned", value: 12, color: "#D98641" },
    { name: "Assigned", value: 8, color: "#8B8B8B" },
    { name: "In Progress", value: 21, color: "#3B71E3" },
    { name: "On Hold", value: 4, color: "#6021A1" },
    { name: "Completed", value: 45, color: "#6BA183" },
  ];

  const workOrdersBarData = [
    { label: "4/5-4/11", value: 14 },
    { label: "4/12-4/18", value: 22 },
    { label: "4/19-4/25", value: 16 },
    { label: "4/26-5/2", value: 26 },
    { label: "5/3-5/9", value: 22 },
    { label: "5/10-5/16", value: 22 },
  ];

  // Table Column
  const fullCols = [
    { key: "id", label: "Work Order #" },
    { key: "merchant", label: "Customer" },
    { key: "location", label: "Location (latitude, longitude)" },
    { key: "created", label: "Created" },
    { key: "due", label: "Due" },
    {
      key: "assign",
      label: "Assign To:",
      render: () => (
        <select className="border border-slate-200 rounded px-2 py-1 text-xs text-slate-500 bg-white outline-none">
          <option>Assign Contractor</option>
        </select>
      ),
    },
  ];

  const compactCols = [
    { key: "id", label: "Work Order #" },
    { key: "merchant", label: "Customer" },
    { key: "due", label: "Due" },
    { key: "assignedTo", label: "Assigned To" },
  ];

  const completedCols = [
    { key: "id", label: "Work Order #" },
    { key: "merchant", label: "Customer" },
    { key: "location", label: "Location (latitude, longitude)" },
    { key: "created", label: "Created" },
    { key: "completed", label: "Completed" },
    { key: "contractor", label: "Contractor" },
  ];

  const baseRow = {
    merchant: "A. B. Client",
    location: "32.7767, -96.7970",
    created: "2026-05-15",
    due: "2026-05-16, 14:00",
    completed: "2026-05-16, 14:00",
    assignedTo: "A. Edwards",
    contractor: "Assign Contractor",
  };

  const dummyData = Array(5)
    .fill(null)
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    .map((_) => ({ id: `WO-12345`, ...baseRow }));

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6 pb-10">
        <PageHeader
          title="Vendor Dashboard"
          description="Manage and monitor your service requests."
        />

        {/* KPI Cards */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
          <KPICard
            title="Overdue"
            value={5}
            subtitle="Work Orders"
            colorVariant="red"
            badge={{ type: "text", value: "Needs Attention" }}
          />
          <KPICard
            title="Unassigned"
            value={12}
            subtitle="Work Orders"
            colorVariant="orange"
            badge={{ type: "text", value: "Needs Assignment" }}
          />
          <KPICard
            title="Assigned"
            value={8}
            subtitle="Not Started"
            colorVariant="gray"
            badge={{ type: "text", value: "Scheduled" }}
          />
          <KPICard
            title="In Progress"
            value={21}
            subtitle="Assigned Contractors"
            colorVariant="blue"
            badge={{ type: "text", value: "On Site" }}
          />
          <KPICard
            title="Completed"
            value={45}
            subtitle="This Week"
            colorVariant="green"
            badge={{ type: "trend", value: "12%", trendDirection: "up" }}
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

        {/* Charts Section */}
        <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">
          <SectionCard title="Work Order by Status">
            <div className="flex h-64 items-center justify-center gap-16 px-2">
              <div className="grid grid-cols-[auto_1fr_auto_auto] items-center gap-x-4 gap-y-3 min-w-55">
                {workOrderStatusData.map((item) => (
                  <React.Fragment key={item.name}>
                    <span
                      className="h-3 w-3 rounded-full"
                      style={{ backgroundColor: item.color }}
                    />
                    <span className="text-[16px] text-slate-600 font-bold">
                      {item.name}
                    </span>
                    <span className="text-[16px] font-bold text-slate-800 text-right">
                      {item.value}
                    </span>
                    <span className="text-[16px] text-slate-400 font-normal">
                      ({Math.round((item.value / 90) * 100)}%)
                    </span>
                  </React.Fragment>
                ))}
              </div>
              <div className="relative h-100 w-55 shrink-0">
                <DonutChart data={workOrderStatusData} />
              </div>
            </div>
          </SectionCard>

          <SectionCard title="Work Orders Completed (per week)">
            <div className="h-64 flex flex-col justify-center px-6">
              <BarChart data={workOrdersBarData} maxValue={30} />
            </div>
          </SectionCard>
        </div>

        {/* Unassigned Table */}
        <SectionCard
          title={
            <div className="flex items-center gap-2">
              <span className="h-4 w-1 bg-purple-700 rounded-full" /> Unassigned
              Work Orders
            </div>
          }
        >
          <DataTable columns={fullCols} data={dummyData} />
        </SectionCard>

        {/* Split Tables Row: Assigned & In Progress */}
        <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">
          <SectionCard
            title={
              <div className="flex items-center gap-2">
                Assigned to Ticket{" "}
                <span className="text-slate-400 font-normal text-xs">
                  • Not Started
                </span>
              </div>
            }
          >
            <DataTable columns={compactCols} data={dummyData.slice(0, 2)} />
          </SectionCard>

          <SectionCard
            title={
              <div className="flex items-center gap-2">
                In Progress{" "}
                <span className="bg-blue-100 text-blue-600 px-2 py-0.5 rounded text-[10px] font-bold">
                  21 Active
                </span>
              </div>
            }
          >
            <DataTable columns={compactCols} data={dummyData.slice(0, 2)} />
          </SectionCard>
        </div>

        {/* Recently Completed Table */}
        <SectionCard
          title={
            <div className="flex items-center gap-2">
              Recently Completed{" "}
              <span className="bg-emerald-100 text-emerald-600 px-2 py-0.5 rounded text-[10px] font-bold">
                45 This Week
              </span>
            </div>
          }
        >
          <DataTable columns={completedCols} data={dummyData} />
        </SectionCard>
      </div>
    </AppLayout>
  );
}
