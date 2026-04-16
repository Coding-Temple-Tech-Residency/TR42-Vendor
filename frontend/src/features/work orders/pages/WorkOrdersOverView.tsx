import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/SideBar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import SectionCard from "../../components/UI/SectionCard";
import EmptyState from "../../components/UI/EmptyState";


export default function WorkOrderOverviewPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
        <div className="space-y-6">
            <PageHeader
            title="Work Orders Overview"
            description="View all current and past Work Orders."
            />

            <div className="mt-6 grid grid-cols-1">
                <SectionCard title="All Work Orders">
                <EmptyState
                    title="No Active Work Orders"
                    description="This section will contain a table of all Work Orders and their current status."
                />
                </SectionCard>
            </div>
            


        </div>
    </AppLayout>
  );
}