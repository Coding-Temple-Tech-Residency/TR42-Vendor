import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/SideBar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import ContractorBasicInfoForm from "../components/ContractorBasicInfoForm";
import { Link } from "react-router-dom";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";


export default function ContractorEditPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
        <div className="space-y-6">
    
            <PageHeader
            title="Contractors"
            description="View current and upcoming work orders and see contractors current location."
            />

            <Link
                    to={`/vendor/contractors/profile/`}
                    className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
                    >
                    Back to Profile
            </Link>

            <ContractorBasicInfoForm />

        </div>
    </AppLayout>
  );
}