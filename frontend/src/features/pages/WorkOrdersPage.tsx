import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";

export default function WorkOrdersPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Work Orders"
        description="Manage, track, and assign work orders."
      />

      {/* KPI Cards */}
      <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
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
          badge={{
            type: "text",
            value: "Needs Assignment",
          }}
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
          badge={{
            type: "trend",
            value: "12% from last week",
            trendDirection: "up",
          }}
        />

        <KPICard
          title="Inovices Created"
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
    </AppLayout>
  );
}
