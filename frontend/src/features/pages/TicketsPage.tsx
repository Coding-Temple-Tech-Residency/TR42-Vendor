import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";

export default function TicketsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Tickets"
        description="Monitor contractor tickets and job activity."
      />

      {/* KPI Cards */}
      <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
        <KPICard
          title="Active"
          value={12}
          subtitle="Tickets"
          colorVariant="orange"
          badge={{ type: "text", value: "Currently Open" }}
        />

        <KPICard
          title="On-Time"
          value="92%"
          subtitle="Jobs Completed"
          colorVariant="blue"
          badge={{ type: "text", value: "On Schedule" }}
        />

        <KPICard
          title="Flagged"
          value={3}
          subtitle="Tickets"
          colorVariant="yellow"
          badge={{ type: "text", value: "Anomalies Detected" }}
        />

        <KPICard
          title="Completed Today"
          value={14}
          subtitle="Tickets"
          colorVariant="green"
          badge={{ type: "text", value: "As of 10:45 AM" }}
        />

        <KPICard
          title="Decline Rate"
          value="6%"
          subtitle="Jobs"
          colorVariant="red"
          badge={{ type: "text", value: "Declined by Contractors" }}
        />

        <KPICard
          title="Avg. Duration"
          value="1.8 days"
          subtitle="This month"
          colorVariant="purple"
          badge={{
            type: "trend",
            value: "0.5 days slower",
            trendDirection: "up",
          }}
        />
      </div>
    </AppLayout>
  );
}
