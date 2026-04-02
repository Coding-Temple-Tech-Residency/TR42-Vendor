import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function RegisterForm() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    firstName: "",
    lastName: "",
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState("");

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    // simple validation
    if (!form.firstName || !form.lastName || !form.email || !form.username) {
      setError("Please fill out all fields.");
      return;
    }

    if (form.password !== form.confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    // password rules
const passwordRules = /^(?=.*[A-Za-z])(?=.*\d).{6,}$/;

if (!passwordRules.test(form.password)) {
  setError("Password must be at least 6 characters and include a number.");
  return;
}


    // save data for step 2
    localStorage.setItem("registerData", JSON.stringify(form));

    navigate("/profile-setup");
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5">

      {error && <p className="text-red-500 text-sm">{error}</p>}

      <div className="grid grid-cols-2 gap-5">
        <input
          className="input"
          placeholder="First Name"
          name="firstName"
          onChange={handleChange}
        />
        <input
          className="input"
          placeholder="Last Name"
          name="lastName"
          onChange={handleChange}
        />
      </div>

      <input
        className="input"
        placeholder="Email"
        name="email"
        onChange={handleChange}
      />

      <input
        className="input"
        placeholder="Username"
        name="username"
        onChange={handleChange}
      />

      <input
        className="input"
        placeholder="Password"
        name="password"
        type="password"
        onChange={handleChange}
      />

      <input
        className="input"
        placeholder="Confirm Password"
        name="confirmPassword"
        type="password"
        onChange={handleChange}
      />

      <button className="btn-primary mt-4">Next</button>
    </form>
  );
}

export default RegisterForm;
