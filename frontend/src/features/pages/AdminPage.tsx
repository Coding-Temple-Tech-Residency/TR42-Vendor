import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";


export default function AdminPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Admin Features"
        description="Manage employees and roles."
      />


    </AppLayout>
  );
}