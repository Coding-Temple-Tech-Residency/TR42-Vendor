import { Outlet, Route, Routes } from "react-router-dom";
import ForgotPasswordPage from "../features/auth/pages/ForgotPasswordPage";
import LoginPage from "../features/auth/pages/LoginPage";
import ProfileSetupPage from "../features/auth/pages/ProfileSetupPage";
import RegisterPage from "../features/auth/pages/RegisterPage";
import SuccessPage from "../features/auth/pages/SuccessPage";
import DashboardPage from "../features/dashboard/pages/DashboardPage";
import WorkOrdersPage from "../features/pages/WorkOrdersDashboardPage";
import TicketsPage from "../features/pages/TicketsDashboardPage";
import ContractorsPage from "../features/pages/ContractorDashboardPage";
import InvoicesPage from "../features/pages/InvoicesDashboardPage";
import ReportsPage from "../features/pages/ReportsDashboardPage";
import FraudRisksPage from "../features/pages/FraudRisksDashboardPage";
import MessagesPage from "../features/pages/MessagesDashboardPage";
import AdminPage from "../features/pages/AdminDashboardPage";
import SettingsPage from "../features/pages/SettingsDashboardPage";
import LoginPage from "../features/auth/pages/LoginPage";
import ForgotPasswordPage from "../features/auth/pages/ForgotPasswordPage";
import ContractorProfilePage from "../features/contractors/pages/ContractorProfile";
import ContractorJobsPage from "../features/contractors/pages/ContractorJobs";
import ContractorEditPage from "../features/contractors/pages/ContractorEditPage";
import WorkOrderOverviewPage from "../features/work orders/pages/WorkOrdersOverView";
import EditWorkOrderPage from "../features/work orders/pages/EditWorkOrders";

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

        {/*Work Orders Pages*/}
        <Route path="work-orders/overview" element={<WorkOrderOverviewPage />} />
        <Route path="work-orders/edit" element={<EditWorkOrderPage />} />

      </Route>
    </Routes>
  );
}
