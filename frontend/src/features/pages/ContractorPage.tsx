import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

function ContractorsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Contractors"
        description="Manage, track, and monitor contractors."
      />

      {/* KPI Section (6 cards across top) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-6">
        <SectionCard title="Active Contractors" subtitle="Currently available">
          <div className="text-3xl font-bold">32</div>
        </SectionCard>

        <SectionCard title="Average Rating" subtitle="Across all contractors">
          <div className="text-3xl font-bold">4.6</div>
        </SectionCard>

        <SectionCard title="In Progress" subtitle="On site">
          <div className="text-3xl font-bold">21</div>
        </SectionCard>

        <SectionCard title="Jobs Completed" subtitle="This month">
          <div className="text-3xl font-bold">45</div>
        </SectionCard>

        <SectionCard title="Possible Fraud" subtitle="Needs attention">
          <div className="text-3xl font-bold">3</div>
        </SectionCard>

        <SectionCard title="On-Time Completion" subtitle="Across all contractors">
          <div className="text-3xl font-bold">93%</div>
        </SectionCard>
      </div>

      {/* Charts Section (side-by-side) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">

        {/* On-Time Completion Chart */}
        <SectionCard title="On-Time Completion">
          <EmptyState
            title="Chart coming soon"
            description="This section will display on-time completion trends."
          />
        </SectionCard>

        {/* Jobs Per Contractor Chart */}
        <SectionCard title="Jobs Per Contractor">
          <EmptyState
            title="Chart coming soon"
            description="Job distribution across contractors will appear here."
          />
        </SectionCard>
      </div>

      {/* Contractors Section (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Contractors">
          <EmptyState
            title="No contractor data"
            description="Contractor performance details will appear here."
          />
        </SectionCard>
      </div>

      {/* Bottom Row: Map + Accounts Payable (side-by-side) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">

        {/* Map Section */}
        <SectionCard title="Map for Current Contractor Location">
          <EmptyState
            title="Map coming soon"
            description="Contractor location data will appear here."
          />
        </SectionCard>

        {/* Accounts Payable Section */}
        <SectionCard title="Accounts Payable Table">
          <EmptyState
            title="No payable data"
            description="Accounts payable details will appear here."
          />
        </SectionCard>
      </div>

    </AppLayout>
  );
}

export default ContractorsPage;
