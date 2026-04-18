import { Outlet, Route, Routes } from "react-router-dom";
import ForgotPasswordPage from "../features/auth/pages/ForgotPasswordPage";
import LoginPage from "../features/auth/pages/LoginPage";
import ProfileSetupPage from "../features/auth/pages/ProfileSetupPage";
import RegisterPage from "../features/auth/pages/RegisterPage";
import SuccessPage from "../features/auth/pages/SuccessPage";
import ContractorEditPage from "../features/contractors/pages/ContractorEditPage";
import ContractorJobsPage from "../features/contractors/pages/ContractorJobs";
import ContractorProfilePage from "../features/contractors/pages/ContractorProfile";
import { CreateContractorFlow } from "../features/contractors/pages/CreateContractorFlow/CreateContractorFlow";
import { AddressStep } from "../features/contractors/pages/CreateContractorFlow/steps/AddressStep";
import { BackgroundStep } from "../features/contractors/pages/CreateContractorFlow/steps/BackgroundStep";
import { BasicInfoStep } from "../features/contractors/pages/CreateContractorFlow/steps/BasicInfoStep";
import { CertificationStep } from "../features/contractors/pages/CreateContractorFlow/steps/CertificationStep";
import { DrugTestStep } from "../features/contractors/pages/CreateContractorFlow/steps/DrugTestStep";
import { InsuranceStep } from "../features/contractors/pages/CreateContractorFlow/steps/InsuranceStep";
import { LicenseStep } from "../features/contractors/pages/CreateContractorFlow/steps/LicenseStep";
import { ReviewStep } from "../features/contractors/pages/CreateContractorFlow/steps/ReviewStep";
import DashboardPage from "../features/dashboard/pages/DashboardPage";
import AdminPage from "../features/pages/AdminDashboardPage";
import ContractorsPage from "../features/pages/ContractorDashboardPage";
import FraudRisksPage from "../features/pages/FraudRisksDashboardPage";
import InvoicesPage from "../features/pages/InvoicesDashboardPage";
import MessagesPage from "../features/pages/MessagesDashboardPage";
import ReportsPage from "../features/pages/ReportsDashboardPage";
import SettingsPage from "../features/pages/SettingsDashboardPage";
import TicketsPage from "../features/pages/TicketsDashboardPage";
import WorkOrdersPage from "../features/pages/WorkOrdersDashboardPage";
import EditWorkOrderPage from "../features/work orders/pages/EditWorkOrders";
import WorkOrderOverviewPage from "../features/work orders/pages/WorkOrdersOverView";

function VendorLayout() {
  return <Outlet />;
}

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/vendor" element={<VendorLayout />}>
        {/*Authentication*/}
        <Route path="register" element={<RegisterPage />} />
        <Route path="profile-setup" element={<ProfileSetupPage />} />
        <Route path="success" element={<SuccessPage />} />
        <Route path="login" element={<LoginPage />} />
        <Route path="forgot-password" element={<ForgotPasswordPage />} />
        {/*App Dashboards*/}
        <Route path="dashboard" element={<DashboardPage />} />
        <Route path="work-orders" element={<WorkOrdersPage />} />
        <Route path="tickets" element={<TicketsPage />} />
        <Route path="contractors" element={<ContractorsPage />} />
        <Route path="invoices" element={<InvoicesPage />} />
        <Route path="reports" element={<ReportsPage />} />
        <Route path="fraud-risks" element={<FraudRisksPage />} />
        <Route path="messages" element={<MessagesPage />} />
        <Route path="admin" element={<AdminPage />} />
        <Route path="settings" element={<SettingsPage />} />
        {/*Contractor Pages*/}
        <Route path="contractors/create" element={<CreateContractorFlow />}>
          <Route index element={<BasicInfoStep />} />
          <Route path="address" element={<AddressStep />} />
          <Route path="background-check" element={<BackgroundStep />} />{" "}
          <Route path="certification" element={<CertificationStep />} />
          <Route path="drug-test" element={<DrugTestStep />} />
          <Route path="insurance" element={<InsuranceStep />} />
          <Route path="license" element={<LicenseStep />} />
          <Route path="review" element={<ReviewStep />} />
        </Route>
        <Route path="contractors/profile" element={<ContractorProfilePage />} />
        <Route path="contractors/jobs" element={<ContractorJobsPage />} />
        <Route
          path="contractors/profile/edit"
          element={<ContractorEditPage />}
        />
        {/*Work Orders Pages*/}
        <Route
          path="work-orders/overview"
          element={<WorkOrderOverviewPage />}
        />
        <Route path="work-orders/edit" element={<EditWorkOrderPage />} />
      </Route>
    </Routes>
  );
}
