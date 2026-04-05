import { Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPageTest";
import RegisterPage from "./features/RegisterPage";
import ProfileSetupPage from "./features/ProfileSetupPage";
import DashboardPage from "./test";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />

      <Route path="/register" element={<RegisterPage />} />
      <Route path="/profile-setup" element={<ProfileSetupPage />} />
      <Route path="/test" element={<DashboardPage />} />
    </Routes>
  );
}

export default App;