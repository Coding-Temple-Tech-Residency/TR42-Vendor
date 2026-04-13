type ContractorComplianceSnapshotProps = {
    isOnboarded: boolean;
    isLicensed: boolean;
    isInsured: boolean;
    isCertified: boolean;
    backgroundCheckPassed: boolean;
    drugPassedPassed: boolean;
};

type ComplianceItemProps = {
    label: string;
    value: boolean;
};

function ComplianceItem({ label, value}: ComplianceItemProps) {
    return (
        <div className="rounded-xl bg=[#1E3A5F] p-4">
            <p className="text-xs font-medium uppercase tracking-wide text-[#4A6C8A]">
                {label}
            </p>

            <span
                className={`mt-3 inline-flex rounded-full px-3 py-1 text-xs font-medium ${
                    value
                        ? "bg-[#5C9E7E4D] text-[#5C9E7E]"
                        : "bg-[#D96B5F4D] text-[#D96B5F]"
                }`}
                >
                    {value ? "Complete" : "Pending"}
                </span>
        </div>
    );
}

export default function ContractorComplianceSnapshot({
    isOnboarded,
    isLicensed,
    isInsured,
    isCertified,
    backgroundCheckPassed,
    drugPassedPassed,
}: ContractorComplianceSnapshotProps) {
    return (
        <section className="rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
            <div className="mb-4">
                <h3 className="text-lg font-semibold text-[#2F4F75]">Compliance Snapshot</h3>
                <p className="text-sm text-[#4A6C8A]">Quick view of contractor qualification and verification status</p>
            </div>

            <div className="grid gap-4 sm:grid-col-2 xl:grid-cols-3">
                <ComplianceItem label="Onboarded" value={isOnboarded} />
                <ComplianceItem label="Licensed" value={isLicensed} />
                <ComplianceItem label="Insured" value={isInsured} />
                <ComplianceItem label="Certified" value={isCertified} />
                <ComplianceItem label="Background Check" value={backgroundCheckPassed} />
                <ComplianceItem label="Drug Test" value={drugPassedPassed} />
            </div>
        </section>
    );
}