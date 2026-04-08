import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";

import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

// import {
//   UserPlusIcon,
//   TruckIcon,
//   DocumentTextIcon,
// } from "@heroicons/react/24/outline";

// Reusable UI components
import DonutChart from "../components/UI/DonutChart";
import FraudGauge from "../components/UI/FraudGauge";
import OpenWorkOrdersTable from "../components/UI/OpenWorkOrdersTable";
import AssignContractorTable from "../components/UI/AssignContractorTable";
import FraudReviewTable from "../components/UI/FraudReviewTable";
import LineChart from "../components/UI/LineChart";

function DashboardPage() {

  // KPI DATA (dummy for now)
  const kpiData = {
    unassigned: 3,
    pending: 2,
    openInvoices: 12,
  };

  // WORK ORDERS (LAST 30 DAYS) CHART DATA
  const workOrdersLast30Days = [
    { day: "Week 1", new: 8, completed: 10 },
    { day: "Week 2", new: 9, completed: 6 },
    { day: "Week 3", new: 6, completed: 8 },
    { day: "Week 4", new: 12, completed: 11 },
  ];

  // INVOICE DONUT CHART DATA
  const invoiceChartData = [
    { name: "Needs Review", value: 6, color: "#1E3A5F" },
    { name: "Submitted", value: 4, color: "#64748B" },
    { name: "Rejected", value: 2, color: "#CBD5F5" },
  ];

  // FRAUD RISK GAUGE VALUE
  const fraudRiskValue = 57;

  // EMPTY ARRAYS (backend will replace later)
  const openWorkOrders = [];
  const contractors = [];
  const pendingInvoices = [];
  const fraudReview = [];

  // KPI COLOR HELPER
  const getKpiColor = (value) => {
    if (value === 0) return "text-green-600";
    if (value < 5) return "text-yellow-600";
    return "text-red-600";
  };

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Dashboard" userName="Katty" />}
    >
      {/* PAGE HEADER */}
      <PageHeader
        title="Vendor Dashboard"
        description="Monitor performance, work orders, and account activity."
      />

      {/* KPI SECTION (3 CARDS ACROSS TOP) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-3">
        <SectionCard
          title="Unassigned Work Orders"
          subtitle="Jobs needing assignment"
        >
          {/* <div className={`text-3xl font-bold ${getKpiColor(kpiData.unassigned)}`}> */}
          <div className="text-3xl font-bold text-red-600">
            {kpiData.unassigned}
          </div>
        </SectionCard>

        <SectionCard title="Pending Jobs" subtitle="Jobs awaiting action">
          {/* <div className={`text-3xl font-bold ${getKpiColor(kpiData.pending)}`}> */}
          <div className="text-3xl font-bold text-yellow-600">
            {kpiData.pending}
          </div>
        </SectionCard>

        <SectionCard title="Open Invoices" subtitle="Invoices requiring review">
          {/* <div className={`text-3xl font-bold ${getKpiColor(kpiData.openInvoices)}`}> */}
          <div className="text-3xl font-bold text-green-600">
            {kpiData.openInvoices}
          </div>
        </SectionCard>
      </div>

      {/* MAIN DASH CONTENT (2-COLUMN LAYOUT) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
        {/* LEFT COLUMN */}
        <div className="flex flex-col gap-6">
          {/* Work Orders (Last 30 Days) Chart */}
          <SectionCard title="Work Orders (Last 30 Days)">
            {workOrdersLast30Days.length === 0 ? (
              <EmptyState
                title="Chart coming soon"
                description="This section will display work order trends."
              />
            ) : (
              <LineChart data={workOrdersLast30Days} />
            )}
          </SectionCard>

          {/* Open Work Orders Table */}
          <SectionCard title="Open Work Orders">
            {openWorkOrders.length === 0 ? (
              <EmptyState
                title="No work orders yet"
                description="Work order details will appear here."
              />
            ) : (
              <OpenWorkOrdersTable />
            )}
          </SectionCard>

          {/* Assign Contractor Table */}
          <SectionCard title="Assign Contractor">
            {contractors.length === 0 ? (
              <EmptyState
                title="No contractors available"
                description="Contractor availability will appear here."
              />
            ) : (
              <AssignContractorTable />
            )}
          </SectionCard>
        </div>

        {/* RIGHT COLUMN */}
        <div className="flex flex-col gap-6">
          {/* Invoice Insights + Fraud Review */}
          <SectionCard title="Invoice Insights & Risk Review">
            {/* Pending Invoices */}
            <div className="mb-6">
              <h3 className="text-sm font-semibold text-gray-700 mb-2">
                Pending Invoices
              </h3>

              {/* Temporarily Force UI To Show */}
              {true ? (
                <div className="bg-white rounded-xl shadow-sm p-4 flex items-center justify-center gap-10">
                  
                  <div className="relative h-48 w-48 flex-shrink-0">
                    <DonutChart data={invoiceChartData} />

                    <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
                      <span className="text-xs text-gray-500">Pending</span>
                      <span className="text-lg font-semibold text-gray-900">
                        $15,306
                      </span>
                    </div>
                  </div>

                  <div className="space-y-5 ml-8 flex-1">
                    {invoiceChartData.map((item) => {
                      const total = invoiceChartData.reduce((sum, i) => sum + i.value, 0);
                      const percentage = ((item.value / total) * 100).toFixed(1);

                      return (
                        <div key={item.name} className="flex items-center gap-4">
                          <div className="flex items-center gap-2 min-w-[140px]">
                            <span
                              className="h-3 w-3 rounded"
                              style={{ backgroundColor: item.color }}
                            />
                            <div className="text-sm text-gray-600">
                              <div>{item.name}</div>
                              <div className="text-xs text-gray-400">
                                {item.value} {item.name.toLowerCase()}
                              </div>
                            </div>
                          </div>

                          <div className="text-lg font-semibold text-gray-700">
                            {percentage}%
                          </div>
                        </div>
                      );
                    })}
                  </div>

                </div>
              ) : (
                <EmptyState
                  title="No invoices yet"
                  description="Invoice review details will appear here."
                />
              )}
            </div>

            <hr className="my-4" />

            {/* Fraud Review */}
            <div>
              <h3 className="text-sm font-semibold text-gray-700 mb-2">
                Fraud Review
              </h3>

              {fraudReview.length === 0 ? (
                <EmptyState
                  title="No invoices flagged for review"
                  description="Invoices that need fraud review will appear here."
                />
              ) : (
                <FraudReviewTable />
              )}
            </div>
          </SectionCard>

          {/* Fraud Risk Analysis */}
          <SectionCard title="Fraud Risk Analysis">
            <FraudGauge value={fraudRiskValue} />
          </SectionCard>
        </div>
      </div>
    </AppLayout>
  );
}

export default DashboardPage;
