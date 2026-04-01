import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPageTest";
import RegisterPage from "./features/RegisterPage";
import ProfileSetupPage from "./features/ProfileSetupPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Login */}
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />

        {/* Reg Flow */}
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/profile-setup" element={<ProfileSetupPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;