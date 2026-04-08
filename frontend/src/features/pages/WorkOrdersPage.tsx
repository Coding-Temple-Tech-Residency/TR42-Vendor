import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

function WorkOrdersPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Work Orders"
        description="Manage, track, and assign work orders."
      />

      {/* KPI cards (6 across top) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-6">
        <SectionCard title="Overdue" subtitle="Needs attention">
          <div className="text-3xl font-bold">5</div>
        </SectionCard>

        <SectionCard title="Unassigned" subtitle="Needs assignment">
          <div className="text-3xl font-bold">12</div>
        </SectionCard>

        <SectionCard title="Assigned" subtitle="Not started">
          <div className="text-3xl font-bold">8</div>
        </SectionCard>

        <SectionCard title="In Progress" subtitle="On site">
          <div className="text-3xl font-bold">21</div>
        </SectionCard>

        <SectionCard title="Completed" subtitle="This week">
          <div className="text-3xl font-bold">45</div>
        </SectionCard>

        <SectionCard title="Avg. Completion" subtitle="This month">
          <div className="text-3xl font-bold">2.4 days</div>
        </SectionCard>
      </div>

      {/* Work Order by Status + Work Orders Created Sections (side-by-side) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
        <SectionCard title="Work Order by Status">
          <EmptyState
            title="Chart coming soon"
            description="This section will display work order status distribution."
          />
        </SectionCard>

        <SectionCard title="Work Orders Created (per week)">
          <EmptyState
            title="Chart coming soon"
            description="Weekly work order trends will appear here."
          />
        </SectionCard>
      </div>

      {/* Unassigned Work Orders Section (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Unassigned Work Orders">
          <EmptyState
            title="No unassigned work orders"
            description="Work orders needing assignment will appear here."
          />
        </SectionCard>
      </div>

      {/* Assigned & In Progress Section (two side-by-side cards) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
        <SectionCard title="Assigned – Not Started">
          <EmptyState
            title="No assigned work orders"
            description="Assigned work orders will appear here."
          />
        </SectionCard>

        <SectionCard title="In Progress">
          <EmptyState
            title="No active work orders"
            description="Work orders currently in progress will appear here."
          />
        </SectionCard>
      </div>

      {/* Recently Completed Section (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Recently Completed">
          <EmptyState
            title="No completed work orders"
            description="Completed work orders will appear here."
          />
        </SectionCard>
      </div>
    </AppLayout>
  );
}

export default WorkOrdersPage;
