import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPageTest";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/LoginPageTest" element={<LoginPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
