import { useEffect, useState } from "react";
import { FormField } from "./FormField";
import { TextInput } from "./TextInput";

import type { Contractor } from "../../../types/models";
import { validateContractorForm } from "../../../utils/validation";
import { PasswordInput } from "../components/PasswordInput";

type ContractorFormProps = {
  mode: "create" | "edit";
  initialData?: Partial<Contractor>;
  onSave?: (data: Contractor) => void;
};

const contractorRoleOptions = [
  { label: "Driver", value: "DRIVER" },
  { label: "Worker", value: "WORKER" },
  { label: "Private Contractor", value: "PRIVATE_CONTRACTOR" },
] as const;

const statusOptions = [
  { label: "Active", value: "ACTIVE" },
  { label: "Inactive", value: "INACTIVE" },
] as const;

const defaultFormData: Contractor = {
  first_name: "",
  last_name: "",
  middle_name: "",
  date_of_birth: "",
  ssn_last_four: "",
  email: "",
  contact_number: "",
  alternate_number: "",
  username: "",
  password: "",
  address: {
    street: "",
    city: "",
    state: "",
    zip: "",
  },
  status: "ACTIVE",
  vendor_contractor_role: "WORKER",
  tickets_completed: 0,
  tickets_open: 0,
  biometric_enrolled: false,
  is_onboarded: false,
  is_subcontractor: false,
  is_fte: false,
  is_licensed: false,
  is_insured: false,
  is_certified: false,
  average_rating: 0,
  years_experience: 0,
};

export default function ContractorForm({
  mode,
  initialData,
  onSave,
}: ContractorFormProps) {
  const [formData, setFormData] = useState<Contractor>(defaultFormData);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [showConfirm, setShowConfirm] = useState(false);

  useEffect(() => {
    if (initialData) {
      setFormData({
        ...defaultFormData,
        ...initialData,
        address: {
          ...defaultFormData.address,
          ...initialData.address,
        },
      });
    }
  }, [initialData]);

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const { name, value } = e.target;

    if (name.startsWith("address.")) {
      const addressField = name.split(".")[1] as keyof Contractor["address"];

      setFormData((prev) => ({
        ...prev,
        address: {
          ...prev.address,
          [addressField]: value,
        },
      }));
    } else {
      setFormData((prev) => ({
        ...prev,
        [name]: value,
      }));
    }

    setErrors((prev) => ({
      ...prev,
      [name]: "",
    }));
  }

  function handleValueChange<K extends keyof Contractor>(
    name: K,
    value: Contractor[K],
  ) {
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));

    setErrors((prev) => ({
      ...prev,
      [name]: "",
    }));
  }

  function handleOpenConfirm() {
    const newErrors = validateContractorForm(formData, mode);
    setErrors(newErrors);

    if (Object.keys(newErrors).length > 0) {
      return;
    }

    setShowConfirm(true);
  }

  const confirmLabel = mode === "create" ? "Create Contractor" : "Save Changes";

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">
          {mode === "create" ? "Create Contractor" : "Edit Contractor"}
        </h3>
        <p className="text-sm text-[#4A6C8A]">
          {mode === "create"
            ? "Enter contractor information."
            : "Update contractor information."}
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <FormField label="First Name">
          <TextInput
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
          />
          {errors.first_name && (
            <p className="mt-2 text-xs text-red-600">{errors.first_name}</p>
          )}
        </FormField>

        <FormField label="Middle Name">
          <TextInput
            name="middle_name"
            value={formData.middle_name}
            onChange={handleChange}
          />
          {errors.middle_name && (
            <p className="mt-2 text-xs text-red-600">{errors.middle_name}</p>
          )}
        </FormField>

        <FormField label="Last Name">
          <TextInput
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
          />
          {errors.last_name && (
            <p className="mt-2 text-xs text-red-600">{errors.last_name}</p>
          )}
        </FormField>

        <FormField label="DOB">
          <TextInput
            name="date_of_birth"
            type="date"
            value={formData.date_of_birth}
            onChange={handleChange}
          />
          {errors.date_of_birth && (
            <p className="mt-2 text-xs text-red-600">{errors.date_of_birth}</p>
          )}
        </FormField>

        <FormField label="Street" className="sm:col-span-2">
          <TextInput
            name="address.street"
            value={formData.address.street}
            onChange={handleChange}
          />
          {errors["address.street"] && (
            <p className="mt-2 text-xs text-red-600">
              {errors["address.street"]}
            </p>
          )}
        </FormField>

        <FormField label="City">
          <TextInput
            name="address.city"
            value={formData.address.city}
            onChange={handleChange}
          />
          {errors["address.city"] && (
            <p className="mt-2 text-xs text-red-600">
              {errors["address.city"]}
            </p>
          )}
        </FormField>

        <FormField label="State">
          <TextInput
            name="address.state"
            value={formData.address.state}
            onChange={handleChange}
          />
          {errors["address.state"] && (
            <p className="mt-2 text-xs text-red-600">
              {errors["address.state"]}
            </p>
          )}
        </FormField>

        <FormField label="ZIP">
          <TextInput
            name="address.zip"
            value={formData.address.zip}
            onChange={handleChange}
          />
          {errors["address.zip"] && (
            <p className="mt-2 text-xs text-red-600">{errors["address.zip"]}</p>
          )}
        </FormField>

        <FormField label="Last 4 SSN">
          <TextInput
            name="ssn_last_four"
            value={formData.ssn_last_four}
            maxLength={4}
            onChange={handleChange}
          />
          {errors.ssn_last_four && (
            <p className="mt-2 text-xs text-red-600">{errors.ssn_last_four}</p>
          )}
        </FormField>

        <FormField label="Email">
          <TextInput
            name="email"
            type="email"
            value={formData.email}
            onChange={handleChange}
          />
          {errors.email && (
            <p className="mt-2 text-xs text-red-600">{errors.email}</p>
          )}
        </FormField>

        <FormField label="Phone Number">
          <TextInput
            name="contact_number"
            value={formData.contact_number}
            onChange={handleChange}
          />
          {errors.contact_number && (
            <p className="mt-2 text-xs text-red-600">{errors.contact_number}</p>
          )}
        </FormField>

        <FormField label="Alternate Number">
          <TextInput
            name="alternate_number"
            value={formData.alternate_number}
            onChange={handleChange}
          />
          {errors.alternate_number && (
            <p className="mt-2 text-xs text-red-600">
              {errors.alternate_number}
            </p>
          )}
        </FormField>

        <FormField label="Username">
          <TextInput
            name="username"
            value={formData.username}
            onChange={handleChange}
          />
          {errors.username && (
            <p className="mt-2 text-xs text-red-600">{errors.username}</p>
          )}
        </FormField>

        <FormField label="Contractor Role">
          <div className="mt-2 flex flex-wrap gap-2">
            {contractorRoleOptions.map((option) => {
              const isActive = formData.vendor_contractor_role === option.value;

              return (
                <button
                  key={option.value}
                  type="button"
                  onClick={() =>
                    handleValueChange("vendor_contractor_role", option.value)
                  }
                  className={`rounded-lg border px-3 py-2 text-sm font-medium transition ${
                    isActive
                      ? "border-[#2F4F75] bg-[#2F4F75] text-white"
                      : "border-[#2F4F75] bg-white text-[#2F4F75] hover:bg-[#4A6C8A] hover:text-white"
                  }`}
                >
                  {option.label}
                </button>
              );
            })}
          </div>
        </FormField>

        <FormField label="Status">
          <div className="mt-2 flex gap-2">
            {statusOptions.map((option) => {
              const isActive = formData.status === option.value;

              return (
                <button
                  key={option.value}
                  type="button"
                  onClick={() => handleValueChange("status", option.value)}
                  className={`rounded-lg border px-3 py-2 text-sm font-medium transition ${
                    isActive
                      ? "border-[#2F4F75] bg-[#2F4F75] text-white"
                      : "border-[#2F4F75] bg-white text-[#2F4F75] hover:bg-[#4A6C8A] hover:text-white"
                  }`}
                >
                  {option.label}
                </button>
              );
            })}
          </div>
        </FormField>

        {mode === "create" && (
          <FormField label="Password">
            <PasswordInput
              name="password"
              label="Password"
              value={formData.password || ""}
              onChange={handleChange}
            />

            {errors.password && (
              <p className="mt-2 text-xs text-red-600">{errors.password}</p>
            )}
          </FormField>
        )}

        <div className="flex justify-end sm:col-span-2">
          <button
            type="button"
            onClick={handleOpenConfirm}
            className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#4A6C8A]"
          >
            {confirmLabel}
          </button>
        </div>
      </div>

      {showConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center pointer-events-none">
          <div className="pointer-events-auto w-full max-w-lg rounded-2xl bg-white/70 backdrop-blur-md p-8 shadow-2xl">
            <div className="rounded-xl bg-white p-6 shadow-lg">
              <h3 className="text-lg font-semibold text-[#2F4F75]">
                {confirmLabel}
              </h3>

              <p className="mt-2 text-sm text-[#4A6C8A]">
                {mode === "create"
                  ? "Are you sure you want to create this contractor?"
                  : "Are you sure you want to save these changes?"}
              </p>

              <div className="mt-6 flex justify-end gap-3">
                <button
                  type="button"
                  onClick={() => setShowConfirm(false)}
                  className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm text-[#2F4F75]"
                >
                  Cancel
                </button>

                <button
                  type="button"
                  onClick={() => {
                    onSave?.(formData);
                    setShowConfirm(false);
                  }}
                  className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#4A6C8A]"
                >
                  {mode === "create" ? "Create" : "Save"}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
