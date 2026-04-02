import React, { useState } from "react";

function ProfileSetupForm() {
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

    // go to success page
    window.location.href = "/success";
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">

      <input
        className="input"
        placeholder="Company Name"
        name="companyName"
        onChange={handleChange}
      />

      <input
        className="input"
        placeholder="Address"
        name="address"
        onChange={handleChange}
      />

      <div className="grid grid-cols-3 gap-4">
        <input
          className="input"
          placeholder="City"
          name="city"
          onChange={handleChange}
        />
        <input
          className="input"
          placeholder="State"
          name="state"
          onChange={handleChange}
        />
        <input
          className="input"
          placeholder="Zip Code"
          name="zip"
          onChange={handleChange}
        />
      </div>

      <input
        className="input"
        placeholder="Company Email"
        name="companyEmail"
        onChange={handleChange}
      />

      <input
        className="input"
        placeholder="Company Phone"
        name="companyPhone"
        onChange={handleChange}
      />

      <select
        className="input"
        name="serviceType"
        onChange={handleChange}
      >
        <option value="">Service Type</option>
        <option value="plumbing">Plumbing</option>
        <option value="electrical">Electrical</option>
        <option value="hvac">HVAC</option>
      </select>

      <button className="btn-primary mt-4">
        Create Vendor Account
      </button>
    </form>
  );
}

export default ProfileSetupForm;
