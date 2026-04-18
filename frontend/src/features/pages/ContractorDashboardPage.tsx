import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import { Link } from "react-router-dom";
import SectionCard from "../components/UI/SectionCard";
import KpiCard from "../components/UI/KpiCard";
import DataTable from "../components/UI/DataTable";
import LineChart from "../components/UI/LineChart";
import BarChart from "../components/UI/BarChart";

function ContractorsPage() {
  // Expanded to 6 data points for the bar chart
  const jobsData = [
    { label: "4/5-4/11", value: 14 },
    { label: "4/12-4/18", value: 22 },
    { label: "4/19-4/25", value: 16 },
    { label: "4/26-5/2", value: 26 },
    { label: "5/3-5/9", value: 22 },
    { label: "5/10-5/16", value: 19 },
  ];

  const onTimeData = [
    { day: "4/12-4/18", value: 78 },
    { day: "4/19-4/25", value: 82 },
    { day: "4/26-5/2", value: 74 },
    { day: "5/3-5/9", value: 85 },
    { day: "5/10-5/16", value: 93 },
  ];

  const contractorCols = [
    { key: "name", label: "Name" },
    { key: "jobs", label: "Jobs in Progress" },
    { key: "onTime", label: "On Time %" },
    { key: "revenue", label: "Revenue" },
    {
      key: "risk",
      label: "Risk Level",
      render: (value: string) => (
        <span
          className={`px-4 py-0.5 rounded-full border text-[11px] font-bold ${
            value === "High"
              ? "bg-red-50 text-red-600 border-red-100"
              : value === "Medium"
                ? "bg-orange-50 text-orange-600 border-orange-100"
                : "bg-emerald-50 text-emerald-600 border-emerald-100"
          }`}
        >
          {value}
        </span>
      ),
    },
    {
      key: "assign",
      label: "Assign to Work Order",
      render: () => (
        <select className="border border-slate-200 rounded px-2 py-1 text-xs text-slate-500 bg-white outline-none focus:ring-1 focus:ring-blue-500">
          <option>Select Work Order</option>
          <option>WO-9921 - Oil</option>
          <option>WO-9922 - Gas</option>
        </select>
      ),
    },
  ];

  const contractorData = [
    {
      name: "Chad Michales",
      jobs: 1,
      onTime: "79.64",
      revenue: "$88,123",
      risk: "Low",
    },
    {
      name: "Marcus Wright",
      jobs: 0,
      onTime: "85.20",
      revenue: "$12,400",
      risk: "High",
    },
    {
      name: "Sarah Jenkins",
      jobs: 3,
      onTime: "92.15",
      revenue: "$45,600",
      risk: "Low",
    },
    {
      name: "Darryl Vance",
      jobs: 2,
      onTime: "64.50",
      revenue: "$28,900",
      risk: "Medium",
    },
    {
      name: "Elena Rodriguez",
      jobs: 1,
      onTime: "98.00",
      revenue: "$102,340",
      risk: "Low",
    },
    {
      name: "Kevin Smith",
      jobs: 0,
      onTime: "0.00",
      revenue: "$0",
      risk: "Low",
    },
  ];

  const accountsPayable = [
    { id: "INV-2026-01", amount: "$2,450.00", status: "Approved" },
    { id: "INV-2026-02", amount: "$1,120.00", status: "Pending" },
    { id: "INV-2026-03", amount: "$3,800.00", status: "Approved" },
    { id: "INV-2026-04", amount: "$945.00", status: "Processing" },
  ];

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6 pb-10">
        <PageHeader
          title="Contractors"
          description="Manage, track, and monitor contractors."
        />

        <Link
          to="/vendor/contractors/profile"
          className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm text-white hover:bg-[#1E3A5F] transition-colors"
        >
          View Profile
        </Link>

        {/* KPI Cards (Unchanged per request) */}
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-6">
          <KpiCard
            title="Active Contractors"
            value={32}
            subtitle="Currently Available"
            colorVariant="orange"
            badge={{ type: "text", value: "Active in system" }}
          />
          <KpiCard
            title="Average Rating"
            value={4.6}
            subtitle="Out of 5"
            colorVariant="gray"
          />
          <KpiCard
            title="In Progress"
            value={21}
            subtitle="Across All Contractors"
            colorVariant="blue"
            badge={{ type: "text", value: "On Site" }}
          />
          <KpiCard
            title="Jobs Completed"
            value={45}
            subtitle="Month"
            colorVariant="green"
            badge={{
              type: "trend",
              value: "12% from last month",
              trendDirection: "up",
            }}
          />
          <KpiCard
            title="Possible Fraud"
            value={3}
            subtitle="Across All Contractors"
            colorVariant="red"
            badge={{ type: "text", value: "Needs Attention" }}
          />
          <KpiCard
            title="On Time Completion"
            value="93%"
            subtitle="Across All Contractors"
            colorVariant="purple"
            badge={{
              type: "trend",
              value: "0.5% from last month",
              trendDirection: "up",
            }}
          />
        </div>

        {/* Interactive Charts */}
        <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">
          <SectionCard title="On-Time Completion">
            <div className="h-64">
              {/* Thicker line is controlled via the strokeWidth inside the LineChart component */}
              <LineChart data={onTimeData} />
            </div>
          </SectionCard>
          <SectionCard title="Jobs Per Contractor">
            <div className="h-64">
              <BarChart data={jobsData} maxValue={30} />
            </div>
          </SectionCard>
        </div>

        {/* Expanded Table Section */}
        <SectionCard title="Contractors List">
          <DataTable columns={contractorCols} data={contractorData} />
        </SectionCard>

        {/* Bottom Row */}
        <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">
          <SectionCard title="Map for Current Contractor Location">
            <div className="h-72 bg-slate-50 rounded-xl flex flex-col items-center justify-center border border-dashed border-slate-200">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                className="w-10 h-10 text-[#2F4F75] mb-2 animate-bounce"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
                />
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"
                />
              </svg>
              <span className="text-slate-400 font-bold text-xs uppercase tracking-widest">
                Live GPS Tracking
              </span>
            </div>
          </SectionCard>

          <SectionCard title="Accounts Payable Table">
            <div className="h-72 flex flex-col space-y-3 px-2 overflow-y-auto">
              {accountsPayable.map((invoice) => (
                <div
                  key={invoice.id}
                  className="flex justify-between p-3 border border-slate-100 rounded-lg bg-white shadow-sm hover:border-blue-100 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <svg
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      className="w-5 h-5 text-blue-500"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="m4.5 19.5 15-15m0 0H8.25m11.25 0v11.25"
                      />
                    </svg>
                    <div>
                      <p className="text-sm font-bold text-slate-700">
                        {invoice.id}
                      </p>
                      <p className="text-[10px] text-slate-400 uppercase font-bold tracking-tight">
                        {invoice.status}
                      </p>
                    </div>
                  </div>
                  <span className="font-bold text-slate-800 text-sm">
                    {invoice.amount}
                  </span>
                </div>
              ))}
              <button className="w-full py-2 mt-auto text-xs font-bold text-[#2F4F75] border border-[#2F4F75] rounded-lg hover:bg-slate-50 transition-colors">
                View All Payables
              </button>
            </div>
          </SectionCard>
        </div>
      </div>
    </AppLayout>
  );
}

export default ContractorsPage;
