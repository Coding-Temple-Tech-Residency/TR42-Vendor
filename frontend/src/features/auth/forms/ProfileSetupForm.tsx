import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import TextInput from "../components/TextInput";
import AuthButton from "../components/AuthButton";

function ProfileSetupForm() {
  const navigate = useNavigate();

  // Load Step 1 data
  const saved = localStorage.getItem("registerData");
  const userData = saved ? JSON.parse(saved) : null;

  // Step 2 form state
  const [form, setForm] = useState({
    companyName: "",
    address: "",
    city: "",
    state: "",
    zip: "",
    companyEmail: "",
    companyPhone: "",
    serviceType: "",
  });

  // Handle input changes
  function handleChange(
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  // handleSubmit function
  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    console.log("Step 1 data:", userData);
    console.log("Step 2 data:", form);

    // clear saved data
    localStorage.removeItem("registerData");

    navigate("/success");
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5">

      {/* Company Name */}
      <TextInput
        label="Company Name"
        name="companyName"
        value={form.companyName}
        onChange={handleChange}
      />

      {/* Address */}
      <TextInput
        label="Address"
        name="address"
        value={form.address}
        onChange={handleChange}
      />

      {/* City / State / Zip */}
      <div className="grid grid-cols-3 gap-5">
        <TextInput
          label="City"
          name="city"
          value={form.city}
          onChange={handleChange}
        />

        <TextInput
          label="State"
          name="state"
          value={form.state}
          onChange={handleChange}
        />

        <TextInput
          label="Zip Code"
          name="zip"
          value={form.zip}
          onChange={handleChange}
        />
      </div>

      {/* Company Email */}
      <TextInput
        label="Company Email"
        name="companyEmail"
        type="email"
        value={form.companyEmail}
        onChange={handleChange}
      />

      {/* Company Phone */}
      <TextInput
        label="Company Phone"
        name="companyPhone"
        value={form.companyPhone}
        onChange={handleChange}
      />

      {/* Service Type */}
      <div className="flex flex-col gap-1">
        <label className="text-sm font-medium text-gray-700">
          Service Type
        </label>

        <select
          name="serviceType"
          value={form.serviceType}
          onChange={handleChange}
          className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#2F3B4A] focus:border-[#2F3B4A]"
        >
          <option value="">Select service type</option>
          <option value="plumbing">Plumbing</option>
          <option value="electrical">Electrical</option>
          <option value="hvac">HVAC</option>
        </select>
      </div>

      {/* Button */}
      <AuthButton type="submit">
        Create Vendor Account
      </AuthButton>

    </form>
  );
}

export default ProfileSetupForm;