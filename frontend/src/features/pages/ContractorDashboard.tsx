import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import { Link } from "react-router-dom";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";


export default function ContractorsPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader
          title="Contractors"
          description="Manage, track, and monitor contractors."
          />

          <Link
            to="/vendor/contractors/profile"
            className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
            >
              Veiw Profile
          </Link>

        </div>
    </AppLayout>
  );
}