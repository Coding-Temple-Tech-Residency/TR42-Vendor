type ContractorContactInfoProps = {
    email: string;
    phone: string;
    region?: string;
    address: string;
};

export default function ContractorContactInfo({
    email,
    phone,
    region,
    address,
}: ContractorContactInfoProps) {
    return (
        <section className="rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
            <div className="mb-4">
                <h3 className="text-lg font-semibold text-[#2F4F75]">Contact Information</h3>
                <p className="text-sm text-[#4A6C8A]">Primary contact and service area details.</p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Email
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {email || "No email available"}
                    </p>
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Phone
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {phone || "No phone number available"}
                    </p>
                </div>
                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-white text-[#2F4F75]">
                        Region / Address
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {address || region || "Region and address placeholder"}
                    </p>
                </div>
            </div>
        </section>
    );
} 