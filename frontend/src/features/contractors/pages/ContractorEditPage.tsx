import { Link } from "react-router-dom";
import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/Sidebar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";

export default function ContractorEditPage() {
  const contractor = {
    first_name: "John",
    middle_name: "",
    last_name: "Smith",
    date_of_birth: "1990-01-01",
    ssn_last_four: "1234",
    email: "john@example.com",
    contact_number: "555-111-2222",
    alternate_number: "",
    username: "johnsmith",
    address: {
      street: "123 Main St",
      city: "Phoenix",
      state: "AZ",
      zip: "85001",
    },
    status: "ACTIVE",
    vendor_contractor_role: "WORKER",
    tickets_completed: 0,
    tickets_open: 0,
    biometric_enrolled: false,
    is_onboarded: false,
    is_subcontractor: false,
    is_fte: false,
    is_licensed: false,
    is_insured: false,
    is_certified: false,
    average_rating: 0,
    years_experience: 3,
  };

  const handleUpdate = async (data: any) => {
    console.log("Update contractor", data);
  };

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader
          title="Edit Contractor"
          description="Update contractor profile information."
        />

        <Link
          to="/vendor/contractors/profile"
          className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
        >
          Back to Profile
        </Link>

        <ContractorForm
          mode="edit"
          initialData={contractor}
          onSave={handleUpdate}
        />
      </div>
    </AppLayout>
  );
}
