import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import TextInput from "../components/TextInput";
import PasswordInput from "../components/PasswordInput";
import AuthButton from "../components/AuthButton";
import { getPasswordChecks, validateRegisterForm } from "../utils/authValidation";

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

  const [errors, setErrors] = useState<any>({});

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setForm({ ...form, [e.target.name]: e.target.value });

    // clear error for that field
    setErrors({ ...errors, [e.target.name]: "" });
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const validationErrors = validateRegisterForm(form);

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    // save data for step 2
    localStorage.setItem("registerData", JSON.stringify(form));

    navigate("/profile-setup");
  }

  // store this once
  const checks = getPasswordChecks(form.password);

  return (
    <form onSubmit={handleSubmit} className="space-y-5">

      {/* First + Last Name */}
      <div className="grid grid-cols-2 gap-5">
        <div>
          <TextInput
            label="First Name"
            name="firstName"
            value={form.firstName}
            onChange={handleChange}
          />
          {errors.firstName && (
            <p className="text-red-500 text-sm">{errors.firstName}</p>
          )}
        </div>

        <div>
          <TextInput
            label="Last Name"
            name="lastName"
            value={form.lastName}
            onChange={handleChange}
          />
          {errors.lastName && (
            <p className="text-red-500 text-sm">{errors.lastName}</p>
          )}
        </div>
      </div>

      {/* Email */}
      <div>
        <TextInput
          label="Email"
          name="email"
          type="email"
          value={form.email}
          onChange={handleChange}
        />
        {errors.email && (
          <p className="text-red-500 text-sm">{errors.email}</p>
        )}
      </div>

      {/* Username */}
      <div>
        <TextInput
          label="Username"
          name="username"
          value={form.username}
          onChange={handleChange}
        />
        {errors.username && (
          <p className="text-red-500 text-sm">{errors.username}</p>
        )}
      </div>

      {/* Password */}
      <div>
        <PasswordInput
          label="Password"
          name="password"
          value={form.password}
          onChange={handleChange}
        />

        {errors.password && (
          <p className="text-red-500 text-sm">{errors.password}</p>
        )}

        {/* password checklist */}
        {form.password && (
          <div className="text-sm mt-1 space-y-1">
            <p className={checks.length ? "text-green-600" : "text-gray-400"}>
              {checks.length ? "✓" : "•"} At least 6 characters
            </p>
            <p className={checks.number ? "text-green-600" : "text-gray-400"}>
              {checks.number ? "✓" : "•"} Includes a number
            </p>
          </div>
        )}
      </div>

      {/* Confirm Password */}
      <div>
        <PasswordInput
          label="Confirm Password"
          name="confirmPassword"
          value={form.confirmPassword}
          onChange={handleChange}
        />
        {errors.confirmPassword && (
          <p className="text-red-500 text-sm">{errors.confirmPassword}</p>
        )}
      </div>

      {/* Button */}
      <AuthButton type="submit">
        Next
      </AuthButton>

    </form>
  );
}

export default RegisterForm;