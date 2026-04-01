import React from "react";

function ProfileSetupForm() {
  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    console.log("Profile setup submitted");
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">

      <input className="input" placeholder="Company Name" />
      <input className="input" placeholder="Address" />

      <div className="grid grid-cols-3 gap-4">
        <input className="input" placeholder="City" />
        <input className="input" placeholder="State" />
        <input className="input" placeholder="Zip Code" />
      </div>

      <input className="input" placeholder="Company Email" />
      <input className="input" placeholder="Company Phone" />

      <select className="input">
        <option>Service Type</option>
      </select>

      <button className="btn-primary">
        Create Vendor Account
      </button>

    </form>
  );
}

export default ProfileSetupForm;