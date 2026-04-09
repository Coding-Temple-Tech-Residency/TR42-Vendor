import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";

export default function InvoicesPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Invoices"
        description="View, pay, and manage invoices."
      />

      {/* KPI Cards */}
      <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
        <KPICard
          title="Pending"
          value={23}
          subtitle="Awaiting Payment"
          colorVariant="gray"
          badge={{ type: "text", value: "Due This Week" }}
        />

        <KPICard
          title="Completed"
          value="$84,320"
          subtitle="This Month"
          colorVariant="green"
          badge={{
            type: "trend",
            value: "8% from last month",
            trendDirection: "up",
          }}
        />

        <KPICard
          title="Overdue Invoices"
          value={7}
          subtitle="Past Due Date"
          colorVariant="red"
          badge={{ type: "text", value: "Needs Attention" }}
        />

        <KPICard
          title="Total Outstanding"
          value="$41,580"
          subtitle="Unpaid Balance"
          colorVariant="purple"
          badge={{ type: "text", value: "Across 23 Invoices" }}
        />

        <KPICard
          title="Avg. Payment Time"
          value="18 days"
          subtitle="Payment Time"
          colorVariant="blue"
          badge={{
            type: "trend",
            value: "2 days faster",
            trendDirection: "down",
          }}
        />

        <KPICard
          title="Invoices Created"
          value="64"
          subtitle="This month"
          colorVariant="orange"
          badge={{
            type: "text",
            value: "+ 12 from last month",
          }}
        />
      </div>
    </AppLayout>
  );
}
