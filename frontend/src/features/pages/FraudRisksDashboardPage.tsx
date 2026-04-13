import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";

export default function FraudRisksPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Fruad Risk"
        description="View and investigate potential fraud risks."
      />

      {/* KPI Cards */}
      <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
        <KPICard
          title="High Risks"
          value={9}
          subtitle="Work Orders"
          colorVariant="red"
          badge={{ type: "text", value: "Requires Review" }}
        />

        <KPICard
          title="Flagged Contractors"
          value={4}
          subtitle="Under Monitoring"
          colorVariant="orange"
          badge={{ type: "text", value: "New This Week" }}
        />

        <KPICard
          title="Suspicious Inovices"
          value={6}
          subtitle="Flagged Transactions"
          colorVariant="purple"
          badge={{ type: "text", value: "Duplicate / Unusual $" }}
        />

        <KPICard
          title="Open Investigations"
          value={5}
          subtitle="Under Review"
          colorVariant="blue"
          badge={{ type: "text", value: "Assigned to Team" }}
        />

        <KPICard
          title="Resolved"
          value={18}
          subtitle="Closed Investigations"
          colorVariant="green"
          badge={{ type: "text", value: "Last 30 Days" }}
        />

        <KPICard
          title="Avg. Risk Score"
          value="21"
          subtitle="Across flagged Orders"
          colorVariant="gray"
          badge={{ type: "text", value: "Low Risk" }}
        />
      </div>
    </AppLayout>
  );
}
