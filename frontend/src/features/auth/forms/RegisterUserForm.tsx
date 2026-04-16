import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import AuthButton from "../components/AuthButton";
import PasswordInput from "../components/PasswordInput";
import TextInput from "../components/TextInput";
import type { User } from "../types/types";
import {
  getPasswordChecks,
  validateUserRegisterForm,
} from "../utils/authValidation";

function RegisterUserForm() {
  const navigate = useNavigate();

  const [form, setForm] = useState<User>({
    firstName: "",
    lastName: "",
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
  });

  const [errors, setErrors] = useState<any>({});

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const { name, value } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));

    setErrors((prev: any) => ({
      ...prev,
      [name]: "",
    }));
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const validationErrors = validateUserRegisterForm(form);

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    // save data for step 2
    localStorage.setItem("registerData", JSON.stringify(form));

    navigate("/vendor/profile-setup");
  }

  const checks = getPasswordChecks(form.password, form);
  const passwordValid = Object.values(checks).every(Boolean);

  return (
    <form onSubmit={handleSubmit} className="space-y-3">

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
        {errors.email && <p className="text-red-500 text-sm">{errors.email}</p>}
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

        {/* password checklist + strength */}
        {form.password && (
          <div className="text-sm mt-2 space-y-1">
            <p
              className={checks.minLength ? "text-green-600" : "text-gray-400"}
            >
              {checks.minLength ? "✓" : "•"} At least 12 characters
            </p>
            <p
              className={
                checks.hasLowercase ? "text-green-600" : "text-gray-400"
              }
            >
              {checks.hasLowercase ? "✓" : "•"} Includes a lowercase letter
            </p>
            <p
              className={
                checks.hasUppercase ? "text-green-600" : "text-gray-400"
              }
            >
              {checks.hasUppercase ? "✓" : "•"} Includes an uppercase letter
            </p>
            <p className={checks.hasDigit ? "text-green-600" : "text-gray-400"}>
              {checks.hasDigit ? "✓" : "•"} Includes a number
            </p>
            <p
              className={checks.hasSpecial ? "text-green-600" : "text-gray-400"}
            >
              {checks.hasSpecial ? "✓" : "•"} Includes a special character
            </p>
            <p
              className={
                checks.noTripleRepeat ? "text-green-600" : "text-gray-400"
              }
            >
              {checks.noTripleRepeat ? "✓" : "•"} No 3 repeated characters in a
              row
            </p>
            <p
              className={checks.noUsername ? "text-green-600" : "text-gray-400"}
            >
              {checks.noUsername ? "✓" : "•"} Does not contain username
            </p>
            <p
              className={
                checks.noFirstName ? "text-green-600" : "text-gray-400"
              }
            >
              {checks.noFirstName ? "✓" : "•"} Does not contain first name
            </p>
            <p
              className={checks.noLastName ? "text-green-600" : "text-gray-400"}
            >
              {checks.noLastName ? "✓" : "•"} Does not contain last name
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
      <AuthButton type="submit" disabled={!passwordValid}>
        Next
      </AuthButton>
    </form>
  );
}

export default RegisterUserForm;
