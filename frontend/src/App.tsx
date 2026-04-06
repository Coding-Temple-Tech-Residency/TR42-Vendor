import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPageTest";
import RegisterPage from "./features/auth/pages/RegisterPage";
import ProfileSetupPage from "./features/auth/pages/ProfileSetupPage";
import SuccessPage from "./features/auth/pages/SuccessPage";

import DashboardPage from "./features/auth/pages/DashboardPage";
import WorkOrdersPage from "./features/auth/pages/WorkOrdersPage";
import ContractorsPage from "./features/auth/pages/ContractorsPage";
// import ProtectedRoute from "./ProtectedRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Login */}
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />

        {/* Registration Flow */}
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/profile-setup" element={<ProfileSetupPage />} />
        <Route path="/success" element={<SuccessPage />} />

        {/* Dashboard Pages (temporarily not protected for UI testing) */}
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/work-orders" element={<WorkOrdersPage />} />
        <Route path="/contractors" element={<ContractorsPage />} />

        {/* Protected routes (re-enable later)
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <DashboardPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/work-orders"
          element={
            <ProtectedRoute>
              <WorkOrdersPage />
            </ProtectedRoute>
          }
        />

        <Route
          path="/contractors"
          element={
            <ProtectedRoute>
              <ContractorsPage />
            </ProtectedRoute>
          }
        />
        */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;