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

    navigate("/vendor/profile-setup");
  }

  // store this once
  const checks = getPasswordChecks(form.password);

  // calculate password strength
const passedChecks = Object.values(checks).filter(Boolean).length;

let strength = "";
let strengthColor = "";

if (passedChecks <= 2) {
  strength = "Weak";
  strengthColor = "text-red-500";
} else if (passedChecks <= 4) {
  strength = "Medium";
  strengthColor = "text-yellow-500";
} else {
  strength = "Strong";
  strengthColor = "text-green-600";
}

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

        {/* password checklist + strength */}
        {form.password && (
          <div className="text-sm mt-1 space-y-1">

            <p className={`font-medium ${strengthColor}`}>
  Password strength: {strength}
</p>
            <p className={checks.length ? "text-green-600" : "text-gray-400"}>
              {checks.length ? "✓" : "•"} At least 6 characters
          </p>
          <p className={checks.uppercase ? "text-green-600" : "text-gray-400"}>
            {checks.uppercase ? "✓" : "•"} Includes an uppercase letter
          </p>
          <p className={checks.lowercase ? "text-green-600" : "text-gray-400"}>
            {checks.lowercase ? "✓" : "•"} Includes a lowercase letter
          </p>
          <p className={checks.number ? "text-green-600" : "text-gray-400"}>
            {checks.number ? "✓" : "•"} Includes a number
          </p>
          <p className={checks.special ? "text-green-600" : "text-gray-400"}>
            {checks.special ? "✓" : "•"} Includes a special character
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