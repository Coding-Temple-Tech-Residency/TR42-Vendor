import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";
import KpiCard from "../components/UI/KPICard";

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
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-6">
        <KpiCard
          title="Pending"
          value={23}
          subtitle="Awaiting Payment"
          colorVariant="gray"
          badge={{ type: "text", value: "Due This Week"}}
        />

        <KpiCard
          title="Completed"
          value="$84,320"
          subtitle="This Month"
          colorVariant="green"
          badge={{ type: "trend", value: "8% from last month", trendDirection: "up" }}
        />

        <KpiCard
          title="Overdue Invoices"
          value={7}
          subtitle="Past Due Date"
          colorVariant="red"
          badge={{ type: "text", value: "Needs Attention" }}
        />

        <KpiCard
          title="Total Outstanding"
          value="$41,580"
          subtitle="Unpaid Balance"
          colorVariant="purple"
          badge={{ type: "text", value: "Across Open Invoices" }}
        />

        <KpiCard
          title="Avg. Payment Time"
          value="18 days"
          subtitle="Payment Time"
          colorVariant="blue"
          badge={{ type: "trend", value: "2 days faster", trendDirection: "down" }}
        />

        <KpiCard
          title="Invoices Created"
          value={64}
          subtitle="This Month"
          colorVariant="orange"
          badge={{ type: "trend", value: "12 from last month", trendDirection: "up", }}
        />
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