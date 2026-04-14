import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import { Link } from "react-router-dom";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";
import KpiCard from "../components/UI/KPICard";

function ContractorsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader
          title="Contractors"
          description="Manage, track, and monitor contractors."
        />

        <Link
          to="/vendor/contractors/profile"
          className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            Veiw Profile
        </Link>


        {/* KPI Cards */}
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-6">
          <KpiCard
            title="Active Contractors"
            value={32}
            subtitle="Currently Available"
            colorVariant="orange"
            badge={{ type: "text", value: "Active in system"}}
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
            badge={{ type: "trend", value: "12% from last month", trendDirection: "up", }}
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
            badge={{ type: "trend", value: "0.5% from last month", trendDirection: "up", }}
          />
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

      </div>
    </AppLayout>
  );
}

export default ContractorsPage;
