import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

function InvoicesPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Invoices"
        description="View, pay, and manage invoices."
      />

      {/* KPI Section (6 cards across top) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-6">
        <SectionCard title="Pending" subtitle="Awaiting payment">
          <div className="text-3xl font-bold">23</div>
        </SectionCard>

        <SectionCard title="Completed" subtitle="This month">
          <div className="text-3xl font-bold">$84,320</div>
        </SectionCard>

        <SectionCard title="Overdue Invoices" subtitle="Needs attention">
          <div className="text-3xl font-bold">7</div>
        </SectionCard>

        <SectionCard title="Total Outstanding" subtitle="Unpaid balance">
          <div className="text-3xl font-bold">$41,580</div>
        </SectionCard>

        <SectionCard title="Avg. Payment Time" subtitle="This month">
          <div className="text-3xl font-bold">18 days</div>
        </SectionCard>

        <SectionCard title="Invoices Created" subtitle="This month">
          <div className="text-3xl font-bold">64</div>
        </SectionCard>
      </div>

      {/* Charts Section (side-by-side) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">

        {/* Open Invoice Status Chart */}
        <SectionCard title="Open Invoice Status">
          <EmptyState
            title="Chart coming soon"
            description="This section will display invoice status distribution."
          />
        </SectionCard>

        {/* Invoices Per Month Chart */}
        <SectionCard title="Invoices Per Month">
          <EmptyState
            title="Chart coming soon"
            description="Monthly invoice trends will appear here."
          />
        </SectionCard>
      </div>

      {/* Open Invoices Table (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Open Invoices">
          <EmptyState
            title="No open invoices"
            description="Open invoice details will appear here."
          />
        </SectionCard>
      </div>

      {/* High Fraud Risk – Needs Review (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="High Fraud Risk – Needs Review">
          <EmptyState
            title="No high-risk invoices"
            description="Invoices requiring fraud review will appear here."
          />
        </SectionCard>
      </div>

      {/* Recently Completed (full width) */}
      <div className="mt-6 grid grid-cols-1 mb-10">
        <SectionCard title="Recently Completed">
          <EmptyState
            title="No completed invoices"
            description="Recently paid invoices will appear here."
          />
        </SectionCard>
      </div>

    </AppLayout>
  );
}
export default InvoicesPage;