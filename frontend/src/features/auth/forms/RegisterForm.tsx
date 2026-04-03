import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import TextInput from "../components/TextInput";
import PasswordInput from "../components/PasswordInput";
import AuthButton from "../components/AuthButton";

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
setError("");
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

      {/* First + Last Name */}
      <div className="grid grid-cols-2 gap-5">
        <TextInput
          label="First Name"
          name="firstName"
          value={form.firstName}
          onChange={handleChange}
        />

        <TextInput
          label="Last Name"
          name="lastName"
          value={form.lastName}
          onChange={handleChange}
        />
      </div>

      {/* Email */}
      <TextInput
        label="Email"
        name="email"
        type="email"
        value={form.email}
        onChange={handleChange}
      />

      {/* Username */}
      <TextInput
        label="Username"
        name="username"
        value={form.username}
        onChange={handleChange}
      />

      {/* Password */}
      <PasswordInput
        label="Password"
        name="password"
        value={form.password}
        onChange={handleChange}
      />

      {/* Confirm Password */}
      <PasswordInput
        label="Confirm Password"
        name="confirmPassword"
        value={form.confirmPassword}
        onChange={handleChange}
      />

      {/* Button */}
      <AuthButton type="submit">
  Next
</AuthButton>

    </form>
  );
}

export default RegisterForm;