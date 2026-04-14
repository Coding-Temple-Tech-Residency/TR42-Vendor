type ContractorBasicInfoProps = {
    first_name: string;
    last_name: string;
    middle_name: string;
    date_of_birth: string;
    ssn_last_four: string;
    address: string;
};

export default function ContractorBasicInfo({
    first_name,
    last_name,
    middle_name,
    date_of_birth,
    ssn_last_four,
    address,
}: ContractorBasicInfoProps) {
    return (
        <section className="rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
            <div className="mb-4">
                <h3 className="text-lg font-semibold text-[#2F4F75]">Basic Personal Information</h3>
                <p className="text-sm text-[#4A6C8A]">Employee personal information.</p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        First Name: 
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {first_name || "Information not available yet."}
                    </p>
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                        Middle Name: 
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {middle_name || "Information not available yet."}
                    </p>
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-white text-[#2F4F75]">
                        Last Name: 
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {last_name || "Information not available yet."}
                    </p>
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-white text-[#2F4F75]">
                        DOB: 
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {date_of_birth || "Information not available yet."}
                    </p>
                </div>

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-white text-[#2F4F75]">
                        Last 4 SSN: 
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {ssn_last_four || "Information not available yet."}
                    </p>
                </div>   

                <div className="rounded-xl bg-[#C9D8E6] p-4 shadow-md">
                    <p className="text-xs font-medium uppercase tracking-white text-[#2F4F75]">
                        Address: 
                    </p>
                    <p className="mt-2 text-sm font-medium text-[#4A6C8A]">
                        {address || "Information not available yet."}
                    </p>
                </div>



            </div>
        </section>
    );
} 