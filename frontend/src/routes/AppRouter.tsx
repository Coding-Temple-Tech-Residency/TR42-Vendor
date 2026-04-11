import { Routes, Route, Outlet } from "react-router-dom";
import RegisterPage from "../features/auth/pages/RegisterPage";
import ProfileSetupPage from "../features/auth/pages/ProfileSetupPage";
import SuccessPage from "../features/auth/pages/SuccessPage";
import DashboardPage from "../features/dashboard/pages/DashboardPage";
import WorkOrdersPage from "../features/pages/WorkOrdersPage";
import TicketsPage from "../features/pages/TicketsPage";
import ContractorsPage from "../features/pages/ContractorPage";
import InvoicesPage from "../features/pages/InvoicesPage";
import ReportsPage from "../features/pages/ReportsPage";
import FraudRisksPage from "../features/pages/FraudRisks";
import MessagesPage from "../features/pages/MessagesPage";
import AdminPage from "../features/pages/AdminPage";
import SettingsPage from "../features/pages/SettingsPage";
import LoginPage from "../features/auth/pages/LoginPage";
import ForgotPasswordPage from "../features/auth/pages/ForgotPasswordPage";

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

        {/*App*/}
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


      </Route>
    </Routes>
  );
}