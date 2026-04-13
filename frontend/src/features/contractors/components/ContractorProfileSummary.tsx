type ContractorProfileSummaryProps = {
    name: string,
    employeeNumber: string,
    role: string,
    status: string,
    isFte: boolean;
    isSubcontractor: boolean;
    averageRating?: number;
    yearsExperience?: number;
};

export default function ContractorProfileSummary({
    name,
    employeeNumber,
    role,
    status,
    isFte,
    isSubcontractor,
    averageRating,
    yearsExperience,
}: ContractorProfileSummaryProps) {
    const workerType = isFte
    ? "Employee"
    : isSubcontractor
        ? "1099 Contractor"
        : "Contractor";

    const statusStyles: Record<string, string> = {
        active: "bg-[#5C9E7E4D] text-[#5C9E7E] border border-[#5C9E7E]",
        inactive: "bg-[#7777774D] text-[#777777] border border-[#777777]",
        pending: "bg-[#2563EB4D] text-[#2563EB] border border-[#2563EB]",
        suspended: "bg-[#D96B5F4D] text-[#D96B5F] border border-[#D96B5F]",
    };

    const normalizedStatus = status.toLowerCase();
    const statusClass =
        statusStyles[normalizedStatus] ??
        "bg-[#7777774D] text-[#777777] border border-[#777777CC]";

    return (
        <section className="rounded-2xl border border-[#777777] bg-white p-6 shadow-lg">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
                <div className="flex items-center gap-4">
                    <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#7777774D] text-lg font-semibold text-white">
                        {name
                            .split(" ")
                            .map((part) => part[0])
                            .join("")
                            .slice(0, 2)
                            .toUpperCase()
                        }
                    </div>

                    <div className="space-y-2">
                        <div>
                            <h1 className="text-2xl font-semibody text-[#111827]">{name}</h1>
                            <p className="text-sm text=[#6B7280]">Employee ID: {employeeNumber}</p>
                        </div>

                        <div className="flex flex-wrap items-center gap-2">
                            <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass}`}>
                                {status}
                            </span>

                            <span className="rounded-full bg-[#D1DAE6] px-3 py-1 text-xs font-medium border border-[#6B7280] text-[#6B7280]">
                                {role}
                            </span>

                            <span className="rounded-full bg-[#C9D8E6] px-3 py-1 text-xs font-medium border border-[#1F2A44] text-[#1F2A44]">
                                {workerType}
                            </span>
                        </div>
                    </div>
                </div>

                <div className="grid gird-cols-2 gap-4 sm:grid-cols-2 lg:min-w-65">
                    <div className="rounded-xl bg-[#C9D8E6] border border-[#6B8CA8] p-4">
                        <p className="text-xs font-medium uppercase tracking-wide text-[#4A6C8A]">
                            Average Rating
                        </p>
                        <p className="mt-1 text-2xl font-semibold text-[#2F4F75]">
                            {averageRating ?? "--"}
                        </p>
                    </div>

                    <div className="rounded-xl bg-[#C9D8E6] border border-[#6B8CA8] p-4">
                        <p className="text-sm font-medium uppercase tracking-wide text-[#4A6C8A]">
                            Experience
                        </p>
                        <p className="mt-1 text-2xl font-semibold text-[#2F4F75]">
                            {yearsExperience ?? "--"}
                        </p>
                        <p className="text-sm text-[#4A6C8A]">years</p>
                    </div>
                </div>
            </div>
        </section>
    );
}