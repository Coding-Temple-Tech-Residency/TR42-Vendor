import { useState } from "react";

type ContractorBasicInfoProps = {
    first_name?: string;
    last_name?: string;
    middle_name?: string;
    date_of_birth?: string;
    ssn_last_four?: string;
    address?: string;
    email?: string;
    phone?: string;
    address_id?: string;
    onSave?: (data: any) => void;
}

export default function ContractorBasicInfoForm({
    first_name = "",
    last_name = "",
    middle_name = "",
    date_of_birth = "",
    ssn_last_four = "",
    address = "",
    email = "",
    phone = "",
    address_id = "",
    onSave,
}: ContractorBasicInfoProps) {
    const [formData, setFormData] = useState({
        first_name,
        last_name,
        middle_name,
        date_of_birth,
        ssn_last_four,
        address,
        email,
        phone,
        address_id,
    });

    const [showConfirm, setShowConfirm] = useState(false);

    const handleChange = (field: string, value: string) => {
        setFormData((prev) => ({
            ...prev,
            [field]: value,
        }));
    };

    const handleSubmit = () => {
        setShowConfirm(true);
    };

    const confirmSave = () => {
        console.log("Saved Data:", formData);
        onSave?.(formData);
        setShowConfirm(false);
    };

    const cancelSave = () => {
        setShowConfirm(false);
    };

    return(
        <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
            <div className="mb-4">
                <h3 className="text-lg text-[#2F4F75]">Basic Personal Information</h3>
                <p className="text-sm text-[#4A6C8A]">Update employee personal information.</p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        First Name
                    </label>
                    <input
                        type="text"
                        value={formData.first_name}
                        onChange={(e) => handleChange("first_name", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Middle Name
                    </label>
                    <input
                        type="text"
                        value={formData.middle_name}
                        onChange={(e) => handleChange("middle_name", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Last Name
                    </label>
                    <input
                        type="text"
                        value={formData.last_name}
                        onChange={(e) => handleChange("last_name", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div> 

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        DOB
                    </label>
                    <input
                        type="date"
                        value={formData.date_of_birth}
                        onChange={(e) => handleChange("date_of_birth", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 sm:col-span-2 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Address
                    </label>
                    <input
                        type="text"
                        value={formData.address}
                        onChange={(e) => handleChange("address", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Last 4 SSN
                    </label>
                    <input
                        type="text"
                        value={formData.ssn_last_four}
                        onChange={(e) => handleChange("ssn_last_four", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Email
                    </label>
                    <input
                        type="text"
                        value={formData.email}
                        onChange={(e) => handleChange("email", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Phone Number
                    </label>
                    <input
                        type="text"
                        value={formData.phone}
                        onChange={(e) => handleChange("phone", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Region / Address
                    </label>
                    <input
                        type="text"
                        value={formData.address_id}
                        onChange={(e) => handleChange("address_id", e.target.value)}
                        className="mt-2 w-full rounded-lg border border-[#2F4F75] px-3 py-2 text-sm text-[#2F4F75] bg-white"
                    />
                </div>

                <div className="mt-6 flex justify-end">
                    <button
                        onClick={handleSubmit}
                        className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#4A6C8A]">
                            Save Changes
                    </button>
                </div>
            </div>

            {showConfirm && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
                    <div className="w-full max-w-md rounded-2xl bg-white p-6 shadow-xl">
                        <h3 className="text-lg font-semibold text-[#2F4F75]">Confirm Changes</h3>

                        <p className="mt-2 text-sm text-[#4A6C8A]">Are you sure you want to save these changes?</p>

                        <div className="mt-6 flex justify-end gap-3">
                            <button 
                                onClick={cancelSave}
                                className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm text-[#2F4F75] hover:bg-[#4A6C8A]">
                                    Cancel
                            </button>

                            <button
                                onClick={confirmSave}
                                className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#4A6C8A]">
                                    Save Changes
                            </button>
                        </div>
                    </div>
                </div>
            )}

        </section>
    );
}