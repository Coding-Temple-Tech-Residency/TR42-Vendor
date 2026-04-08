import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

function FraudRisksPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Fraud Risk"
        description="View and investigate potential fraud risks."
      />

      {/* KPI Section (6 cards across top) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-6">
        <SectionCard title="High Risk Orders" subtitle="Requires review">
          <div className="text-3xl font-bold">9</div>
        </SectionCard>

        <SectionCard title="Flagged Contractors" subtitle="Under monitoring">
          <div className="text-3xl font-bold">4</div>
        </SectionCard>

        <SectionCard title="Suspicious Invoices" subtitle="Duplicate / Unusual $">
          <div className="text-3xl font-bold">6</div>
        </SectionCard>

        <SectionCard title="Open Investigations" subtitle="Assigned to team">
          <div className="text-3xl font-bold">5</div>
        </SectionCard>

        <SectionCard title="Resolved" subtitle="Last 30 days">
          <div className="text-3xl font-bold">18</div>
        </SectionCard>

        <SectionCard title="Avg. Risk Score" subtitle="Across flagged orders">
          <div className="text-3xl font-bold">21</div>
        </SectionCard>
      </div>

      {/* Charts Section (side-by-side) */}
      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">

        {/* Potential Risk Chart */}
        <SectionCard title="Potential Risk">
          <EmptyState
            title="Chart coming soon"
            description="This section will display risk distribution across categories."
          />
        </SectionCard>

        {/* Fraud Over Time Chart */}
        <SectionCard title="Fraud Over Time">
          <EmptyState
            title="Chart coming soon"
            description="Monthly fraud trend data will appear here."
          />
        </SectionCard>
      </div>

      {/* Open Cases Table (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="Open Cases (Active Investigations)">
          <EmptyState
            title="No open cases"
            description="Active fraud investigations will appear here."
          />
        </SectionCard>
      </div>

      {/* High Risk Contractors Table (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="High Risk Contractors">
          <EmptyState
            title="No high-risk contractors"
            description="Contractors flagged for risk will appear here."
          />
        </SectionCard>
      </div>

      {/* High Risk Invoices Table (full width) */}
      <div className="mt-6 grid grid-cols-1">
        <SectionCard title="High Risk Invoices">
          <EmptyState
            title="No high-risk invoices"
            description="Invoices flagged for potential fraud will appear here."
          />
        </SectionCard>
      </div>

      {/* Recently Closed Section (full width) */}
      <div className="mt-6 grid grid-cols-1 mb-10">
        <SectionCard title="Recently Closed">
          <EmptyState
            title="No closed cases"
            description="Recently resolved investigations will appear here."
          />
        </SectionCard>
      </div>

    </AppLayout>
  );
}
export default FraudRisksPage;