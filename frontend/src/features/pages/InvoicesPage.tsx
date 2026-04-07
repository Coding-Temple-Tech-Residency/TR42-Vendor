import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";


export default function InvoicesPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <PageHeader
        title="Invoices"
        description="View, pay, and manage invoices."
      />


    </AppLayout>
  );
}