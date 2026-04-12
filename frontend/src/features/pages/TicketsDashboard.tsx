import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

function TicketsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Tickets"
        description="Monitor contractor tickets and job activity."
      />

      {/* KPI Section (6 cards across top) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-6">
        <SectionCard title="Active" subtitle="Currently open">
          <div className="text-3xl font-bold">12</div>
        </SectionCard>

        <SectionCard title="On-Time" subtitle="Jobs completed on schedule">
          <div className="text-3xl font-bold">92%</div>
        </SectionCard>

        <SectionCard title="Flagged" subtitle="Anomalies detected">
          <div className="text-3xl font-bold">3</div>
        </SectionCard>

        <SectionCard title="Completed Today" subtitle="As of 10:45 AM">
          <div className="text-3xl font-bold">14</div>
        </SectionCard>

        <SectionCard title="Decline Rate" subtitle="Jobs declined by contractors">
          <div className="text-3xl font-bold">6%</div>
        </SectionCard>

        <SectionCard title="Avg. Duration" subtitle="This month">
          <div className="text-3xl font-bold">1.8 days</div>
        </SectionCard>
      </div>

      {/* Charts Section (side-by-side) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">

        {/* Ticket Performance Overview Chart */}
        <SectionCard title="Ticket Performance Overview">
          <EmptyState
            title="Chart coming soon"
            description="This section will display ticket status distribution."
          />
        </SectionCard>

        {/* Tickets Completed Per Day Chart */}
        <SectionCard title="Tickets Completed Per Day">
          <EmptyState
            title="Chart coming soon"
            description="Daily ticket completion trends will appear here."
          />
        </SectionCard>
      </div>

      {/* In Progress Table (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="In Progress (Live Activity)">
          <EmptyState
            title="No active tickets"
            description="Live contractor activity will appear here."
          />
        </SectionCard>
      </div>

      {/* Flagged Tickets Table (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Flagged Tickets (Risk)">
          <EmptyState
            title="No flagged tickets"
            description="Tickets with anomalies will appear here."
          />
        </SectionCard>
      </div>

      {/* Completed Today Table (full width) */}
      <div className="mt-6 grid grid-cols-1 mb-10">
        <SectionCard title="Completed Today (Daily Output)">
          <EmptyState
            title="No completed tickets"
            description="Tickets completed today will appear here."
          />
        </SectionCard>
      </div>

    </AppLayout>
  );
}
export default TicketsPage;