import { Link } from "react-router-dom";
import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/Sidebar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import ContractorForm from "../components/ContractorForm";

export default function ContractorCreatePage() {
  const handleCreate = async (data: any) => {
    console.log("Create contractor", data);
  };

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader
          title="Create Contractor"
          description="Add a new contractor to your vendor account."
        />

        <Link
          to="/vendor/contractors"
          className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
        >
          Back to Contractors
        </Link>

        <ContractorForm mode="create" onSave={handleCreate} />
      </div>
    </AppLayout>
  );
}
