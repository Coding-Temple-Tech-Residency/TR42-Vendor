import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

function DashboardPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Vendor Dashboard"
        description="Monitor performance, work orders, and account activity."
      />

      {/* KPI Section (3 cards across top) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-3">
        <SectionCard title="Unassigned Work Orders" subtitle="Jobs needing assignment">
          <div className="text-3xl font-bold text-slate-900">3</div>
        </SectionCard>

        <SectionCard title="Pending Jobs" subtitle="Jobs awaiting action">
          <div className="text-3xl font-bold text-slate-900">2</div>
        </SectionCard>

        <SectionCard title="Open Invoices" subtitle="Invoices requiring review">
          <div className="text-3xl font-bold text-slate-900">12</div>
        </SectionCard>
      </div>

      {/* Main dashboard content (2-column layout) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">

        {/* LEFT COLUMN: Work Orders + Open Work Orders + Assign Contractor */}
        <div className="flex flex-col gap-6">

          {/* Work Orders (Last 30 Days) Chart */}
          <SectionCard title="Work Orders (Last 30 Days)">
            {/* Replace this with a static chart image if desired */}
            <EmptyState
              title="Chart coming soon"
              description="This section will display work order trends."
            />
          </SectionCard>

          {/* Open Work Orders Table */}
          <SectionCard title="Open Work Orders">
            <EmptyState
              title="No work orders yet"
              description="Work order details will appear here."
            />
          </SectionCard>

          {/* Assign Contractor Table */}
          <SectionCard title="Assign Contractor">
            <EmptyState
              title="No contractors available"
              description="Contractor availability will appear here."
            />
          </SectionCard>
        </div>

        {/* RIGHT COLUMN: Pending Invoices + Fraud Review (combined) + Fraud Risk Analysis */}
        <div className="flex flex-col gap-6">

          {/* Combined Pending Invoices + Fraud Review Section */}
<SectionCard title="Invoice Insights & Risk Review">

  {/* Pending Invoices subsection */}
  <div className="mb-6">
    <h3 className="text-sm font-semibold text-gray-700 mb-2">Pending Invoices</h3>
    <EmptyState
      title="No invoices yet"
      description="Invoice review details will appear here."
    />
  </div>

  <hr className="my-4" />

  {/* Fraud Review subsection */}
  <div>
    <h3 className="text-sm font-semibold text-gray-700 mb-2">Fraud Review</h3>
    <EmptyState
      title="No invoices flagged for review"
      description="Invoices that need fraud review will appear here."
    />
  </div>

</SectionCard>


          {/* Fraud Risk Analysis Section */}
          <SectionCard title="Fraud Risk Analysis">
            {/* Replace with static pie chart image if desired */}
            <EmptyState
              title="No fraud data yet"
              description="Fraud risk insights will appear here."
            />
          </SectionCard>
        </div>
      </div>
    </AppLayout>
  );
}

export default DashboardPage;
