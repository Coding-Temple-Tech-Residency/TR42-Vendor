import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";
import KpiCard from "../components/UI/KPICard";
import { Link } from "react-router-dom";

function TicketsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >

      <div className="space-y-6">
        <PageHeader
          title="Tickets"
          description="Monitor contractor tickets and job activity."
        />
        <Link
          to="/vendor/tickets/details"
          className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            Ticket Details
        </Link>

        <Link
          to="/vendor/tickets/create"
          className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            Create Ticket
        </Link>
     </div>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-6">
        <KpiCard
          title="Active Tickets"
          value={12}
          subtitle="In Progress"
          colorVariant="blue"
          badge={{ type: "text", value: "Active in system"}}
        />

        <KpiCard
          title="On-Time Completion"
          value="92%"
          subtitle="Jobs Completed"
          colorVariant="green"
          badge={{ type: "text", value: "On-Time"}}
        />

        <KpiCard
          title="Flagged"
          value={3}
          subtitle="Tickets"
          colorVariant="red"
          badge={{ type: "text", value: "Anomalies Detected" }}
        />

        <KpiCard
          title="Completed Today"
          value={14}
          subtitle="Tickets Completed"
          colorVariant="gray"
          badge={{ type: "text", value: "As of 15:45" }}
        />

        <KpiCard
          title="Decline Rate"
          value="6%"
          subtitle="Tickets Rejected"
          colorVariant="orange"
          badge={{ type: "text", value: "Declined by Contractor" }}
        />

        <KpiCard
          title="Avg. Duration"
          value="1.8 days"
          subtitle="This Month"
          colorVariant="purple"
          badge={{ type: "trend", value: "0.5% days slower", trendDirection: "down" }}
        />
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