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

      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-3">
        <SectionCard title="Open Work Orders" subtitle="Current active jobs">
          <div className="text-3xl font-bold text-slate-900">18</div>
        </SectionCard>

        <SectionCard title="Pending Invoices" subtitle="Awaiting review">
          <div className="text-3xl font-bold text-slate-900">6</div>
        </SectionCard>

        <SectionCard title="Completion Rate" subtitle="Last 30 days">
          <div className="text-3xl font-bold text-slate-900">92%</div>
        </SectionCard>
      </div>

      <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
        <SectionCard title="Recent Activity">
          <EmptyState
            title="No recent activity yet"
            description="Activity updates will appear here once users begin interacting with the system."
          />
        </SectionCard>

        <SectionCard title="Upcoming Tasks">
          <EmptyState
            title="No upcoming tasks"
            description="Assigned tasks and deadlines will show here."
          />
        </SectionCard>
      </div>
    </AppLayout>
  );
}

export default DashboardPage;
