import { Routes, Route, Outlet } from "react-router-dom";
import RegisterPage from "../features/auth/pages/RegisterPage";
import ProfileSetupPage from "../features/auth/pages/ProfileSetupPage";
import SuccessPage from "../features/auth/pages/SuccessPage";
import DashboardPage from "../features/pages/DashboardPage";
import WorkOrdersPage from "../features/pages/WorkOrdersDashboard";
import TicketsPage from "../features/pages/TicketsDashboard";
import ContractorsPage from "../features/pages/ContractorDashboard";
import InvoicesPage from "../features/pages/InvoicesDashboard";
import ReportsPage from "../features/pages/ReportsDashboard";
import FraudRisksPage from "../features/pages/FraudRisksDashboard";
import MessagesPage from "../features/pages/MessagesDashboard";
import AdminPage from "../features/pages/AdminDashboard";
import SettingsPage from "../features/pages/SettingsDashboard";
import LoginPage from "../features/auth/pages/LoginPage";
import ForgotPasswordPage from "../features/auth/pages/ForgotPasswordPage";
import ContractorProfilePage from "../features/contractors/pages/ContractorProfile";
import ContractorJobsPage from "../features/contractors/pages/ContractorJobs";
import ContractorEditPage from "../features/contractors/pages/ContractorEditPage";

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
        <Route path="contractors/profile" element={<ContractorProfilePage />} />
        <Route path="contractors/jobs" element={<ContractorJobsPage />} />
        <Route path="contractors/profile/edit" element={<ContractorEditPage />} />

      </Route>
    </Routes>
  );
}