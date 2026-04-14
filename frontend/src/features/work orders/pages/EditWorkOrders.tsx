import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/SideBar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import CreateWorkOrderForm from "../components/WorkOrderForm";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";


export default function EditWorkOrderPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
        <div className="space-y-6">
    
            <PageHeader
            title="Work Orders"
            description="Add a new work order and assign operational details."
            />

            <CreateWorkOrderForm />

        </div>
    </AppLayout>
  );
}