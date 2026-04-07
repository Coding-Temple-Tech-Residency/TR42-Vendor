import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import TextInput from "../components/TextInput";
import AuthButton from "../components/AuthButton";
import { formatPhoneNumber, validateProfileForm } from "../utils/authValidation";

function ProfileSetupForm() {
  const navigate = useNavigate();

  // Get step 1 data from localStorage
  let userData: any = null;

  try {
    const saved = localStorage.getItem("registerData");
    userData = saved ? JSON.parse(saved) : null;
  } catch (err) {
    console.log("Error reading localStorage");
  }

  // Form state
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

  // Store errors
  const [errors, setErrors] = useState<{ [key: string]: string }>({});

  // Handle input changes
  function handleChange(
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) {
    const name = e.target.name;
    const value = e.target.value;

    // Format phone number
    if (name === "companyPhone") {
      setForm({ ...form, [name]: formatPhoneNumber(value) });
    } else {
      setForm({ ...form, [name]: value });
    }

    // Clear error for that field
    setErrors((prev) => ({
      ...prev,
      [name]: "",
    }));
  }

  // Submit form
  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const newErrors = validateProfileForm(form);

    // Stop if there are errors
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    console.log("Step 1 data:", userData);
    console.log("Step 2 data:", form);

    localStorage.removeItem("registerData");

    navigate("/vendor/success");
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5">

      {/* Company Name */}
      <div>
        <TextInput
          label="Company Name"
          name="companyName"
          value={form.companyName}
          onChange={handleChange}
        />
        {errors.companyName && (
          <p className="text-red-500 text-sm">{errors.companyName}</p>
        )}
      </div>

      {/* Address */}
      <div>
        <TextInput
          label="Address"
          name="address"
          value={form.address}
          onChange={handleChange}
        />
        {errors.address && (
          <p className="text-red-500 text-sm">{errors.address}</p>
        )}
      </div>

      {/* City / State / Zip */}
      <div className="grid grid-cols-3 gap-5">
        <div>
          <TextInput
            label="City"
            name="city"
            value={form.city}
            onChange={handleChange}
          />
          {errors.city && (
            <p className="text-red-500 text-sm">{errors.city}</p>
          )}
        </div>

        <div>
          <TextInput
            label="State"
            name="state"
            value={form.state}
            onChange={handleChange}
          />
          {errors.state && (
            <p className="text-red-500 text-sm">{errors.state}</p>
          )}
        </div>

        <div>
          <TextInput
            label="Zip Code"
            name="zip"
            value={form.zip}
            onChange={handleChange}
          />
          {errors.zip && (
            <p className="text-red-500 text-sm">{errors.zip}</p>
          )}
        </div>
      </div>

      {/* Company Email */}
      <div>
        <TextInput
          label="Company Email"
          name="companyEmail"
          type="email"
          value={form.companyEmail}
          onChange={handleChange}
        />
        {errors.companyEmail && (
          <p className="text-red-500 text-sm">{errors.companyEmail}</p>
        )}
      </div>

      {/* Company Phone */}
      <div>
        <TextInput
          label="Company Phone"
          name="companyPhone"
          value={form.companyPhone}
          onChange={handleChange}
        />
        {errors.companyPhone && (
          <p className="text-red-500 text-sm">{errors.companyPhone}</p>
        )}
      </div>

      {/* Service Type */}
      <div className="flex flex-col gap-1">
        <label className="text-sm font-medium text-gray-700">
          Service Type
        </label>

        <select
          name="serviceType"
          value={form.serviceType}
          onChange={handleChange}
          className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-[#2F3B4A]"
        >
          <option value="">Select service type</option>
          <option value="plumbing">Plumbing</option>
          <option value="electrical">Electrical</option>
          <option value="hvac">HVAC</option>
        </select>

        {errors.serviceType && (
          <p className="text-red-500 text-sm">{errors.serviceType}</p>
        )}
      </div>

      {/* Button */}
      <AuthButton type="submit">
        Create Vendor Account
      </AuthButton>

    </form>
  );
}

export default ProfileSetupForm;