import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPageTest";
import RegisterPage from "./features/auth/pages/RegisterPage";
import ProfileSetupPage from "./features/auth/pages/ProfileSetupPage";
import SuccessPage from "./features/auth/pages/SuccessPage";
// import DashboardPage from "./DashboardPage";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Login */}
        <Route path="/" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />

        {/* Reg Flow */}
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/profile-setup" element={<ProfileSetupPage />} />
        <Route path="/success" element={<SuccessPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;