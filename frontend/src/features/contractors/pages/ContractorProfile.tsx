import { Link } from "react-router-dom";
import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/SideBar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import ContractorBasicInfo from "../components/ContractorBasicInfo";
import ContractorComplianceSnapshot from "../components/ContractorCompliance";
import ContractorContactInfo from "../components/ContractorContactInfo";
import ContractorProfileSummary from "../components/ContractorProfileSummary";
// import SectionCard from "../components/SectionCard";
// import EmptyState from "../components/EmptyState";

export default function ContractorProfilePage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader title="Contractors" description="Contractor Profile." />

        <div className="flex gap-4">
          <Link
            to="/vendor/contractors/jobs"
            className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            View Jobs
          </Link>

          <Link
            to={`/vendor/contractors/profile/edit`}
            className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
          >
            Edit Contractor
          </Link>
        </div>

        <ContractorProfileSummary
          name="Katty"
          employeeNumber="EMP1234"
          role="Vendor Employed"
          status="Active"
          isFte={true}
          isSubcontractor={false}
          averageRating={5}
          yearsExperience={8}
        />

        <ContractorBasicInfo
          first_name="Katty"
          last_name="Baldridge"
          middle_name="Alice"
          date_of_birth="May 29, 1990"
          ssn_last_four="1234"
          address="123 Fake Ave, Philadelphia, PA"
        />

        <div className="grid md:grid-cols-2 gap-4">
          <ContractorContactInfo
            email="katty@yahoo.com"
            phone="(123)456-7890"
            region="West"
            address="123 Fake St, Philadelphia, PA"
          />

          <ContractorComplianceSnapshot
            isOnboarded={true}
            isLicensed={true}
            isInsured={true}
            isCertified={true}
            backgroundCheckPassed={false}
            drugPassedPassed={true}
          />
        </div>
      </div>
    </AppLayout>
  );
}
