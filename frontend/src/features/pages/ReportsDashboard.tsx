import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";


export default function ReportsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Reports"
        description="View, manage, create reports and stats."
      />


    </AppLayout>
  );
}