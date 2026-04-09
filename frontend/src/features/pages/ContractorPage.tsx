import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";

export default function ContractorsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Contractors"
        description="Manage, track, and monitor contractors."
      />

      {/* KPI Cards */}
      <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
        <KPICard
          title="Active Contractors"
          value={32}
          subtitle="Currently Available"
          colorVariant="orange"
          badge={{ type: "text", value: "Active in system" }}
        />

        <KPICard
          title="Average Rating"
          value="4.6"
          subtitle="Out of 5"
          colorVariant="gray"
        />

        <KPICard
          title="In Progress"
          value={21}
          subtitle="Across All Contractors"
          colorVariant="blue"
          badge={{ type: "text", value: "On Site" }}
        />

        <KPICard
          title="Jobs Completed"
          value={45}
          subtitle="Month"
          colorVariant="green"
          badge={{ type: "trend", value: "+12%", trendDirection: "up" }}
        />

        <KPICard
          title="Possible Fraud"
          value={3}
          subtitle="Across All Contractors"
          colorVariant="red"
          badge={{ type: "text", value: "Needs Attention" }}
        />

        <KPICard
          title="On Time Completion"
          value="93%"
          subtitle="Across All Contractors"
          colorVariant="purple"
          badge={{ type: "trend", value: "+0.5%", trendDirection: "up" }}
        />
      </div>
    </AppLayout>
  );
}
