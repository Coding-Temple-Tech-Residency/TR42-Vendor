import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import type { User, Vendor } from "../../../types/models";
import {
  formatPhoneNumber,
  toBackendPhoneFormat,
  validateVendorRegisterForm,
} from "../../../utils/validation";
import AuthButton from "../components/AuthButton";
import TextInput from "../components/TextInput";

function RegisterVendorForm() {
  const navigate = useNavigate();

  const [userData, setUserData] = useState<User | null>(null);
  const [isLoadingUserData, setIsLoadingUserData] = useState(true);

  // Form state
  const [form, setForm] = useState<Vendor>({
    companyName: "",
    primaryContactName: "",
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

  useEffect(() => {
    try {
      const saved = localStorage.getItem("registerData");
      const parsed = saved ? JSON.parse(saved) : null;

      if (!parsed) {
        navigate("/vendor/register");
        return;
      }

      setUserData(parsed);
    } catch (err) {
      console.log("Error reading localStorage");
      navigate("/vendor/register");
    } finally {
      setIsLoadingUserData(false);
    }
  }, [navigate]);

  // Handle input changes
  function handleChange(
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>,
  ) {
    const { name, value } = e.target;

    // Format phone number
    setForm((prev) => ({
      ...prev,
      [name]: name === "companyPhone" ? formatPhoneNumber(value) : value,
    }));

    // Clear error for that field
    setErrors((prev) => ({
      ...prev,
      [name]: "",
    }));
  }

  // Submit form
  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const newErrors = validateVendorRegisterForm(form);

    // Stop if there are errors
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }
    if (!userData) {
      console.log("Missing registration data. Please start again.");
      navigate("/vendor/register");
      return;
    }

    const payload = {
      user: {
        first_name: userData.firstName,
        middle_name: userData.middleName || null,
        last_name: userData.lastName,
        email: userData.email,
        username: userData.username,
        password: userData.password,
        contact_number: toBackendPhoneFormat(userData.contactNumber),
        alternate_number: userData.alternateNumber
          ? toBackendPhoneFormat(userData.alternateNumber)
          : null,
        date_of_birth: userData.dateOfBirth || null,
        ssn_last_four: userData.ssnLastFour || null,
        address: {
          street: userData.address,
          city: userData.city,
          state: userData.state,
          zip: userData.zip,
        },
      },
      vendor: {
        company_name: form.companyName,
        company_email: form.companyEmail,
        company_phone: toBackendPhoneFormat(form.companyPhone),
        primary_contact_name: form.primaryContactName,
        service_type: form.serviceType,
        address: {
          street: form.address,
          city: form.city,
          state: form.state,
          zip: form.zip,
        },
      },
    };

    try {
      const response = await fetch("/api/registration", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok) {
        throw result;
      }

      localStorage.removeItem("registerData");

      navigate("/vendor/success");
    } catch (err) {
      console.log("error", err);
    }
  }

  if (isLoadingUserData) {
    return null;
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
      {/* Primary Contact Name */}
      <div>
        <TextInput
          label="Primary Contact Name"
          name="primaryContactName"
          value={form.primaryContactName}
          onChange={handleChange}
        />
        {errors.primaryContactName && (
          <p className="text-sm text-red-500">{errors.primaryContactName}</p>
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
          {errors.city && <p className="text-red-500 text-sm">{errors.city}</p>}
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
          {errors.zip && <p className="text-red-500 text-sm">{errors.zip}</p>}
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
      <AuthButton type="submit">Create Vendor Account</AuthButton>
    </form>
  );
}

export default RegisterVendorForm;
