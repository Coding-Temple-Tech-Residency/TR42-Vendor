type Assignment = {
    title: string;
    location: string;
    date: string;
    status: string;
};

type ContractorAssignmentProps = {
    currentAssignment?: Assignment;
    upcomingAssignment?: Assignment;
};

function AssignmentCard({
    label,
    assignment,
}: {
    label: string;
    assignment?: Assignment;
}) {
    return (
        <div className="rounded-xl bg-[#C9D8E6] p-4">
            <p className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
                {label}
            </p>

            {assignment ? (
                <div className="mt-3 bg-white border rounded-xl border-[#2F4F75] space-y-2 p-4">
                    <h4 className="text-base font-semibold text-[#2F4F75]">
                        {assignment.title}
                    </h4>
                    <p className="text-sm text-[#4A6C8A]">{assignment.location}</p>
                    <p className="text-sm text-[#4A6C8A]">{assignment.date}</p>
                    <span className="inline-flex rounded-full bg-[#C9D8E6] px-3 py-1 text-xs font-medium text-[#4A6C8A]">{assignment.status}</span>
                </div>
            ) : (
                <p className="mt-3 text-sm text-[#4A6C8A]">No assignment available</p>
            )}
        </div>
    );
}

export default function ContractorAssignment({
    currentAssignment,
    upcomingAssignment,
}: ContractorAssignmentProps) {
    return (
        <section className="rounded-2xl border border-[#2F4F75] bg-white shadow-lg p-6">
            <div className="mb-4">
                <h3 className="text-lg font-semibold text-[#2F4F75]">Assignments</h3>
                <p className="text-sm text-[#4A6C8A]">
                    Current and upcoming work assigned to this contractor.
                </p>
            </div>
            
            <div className="grid gap-4 md:grid-cols-2">
                <AssignmentCard label="Current Assignment" assignment={currentAssignment} />
                <AssignmentCard label="Upcoming Assignment" assignment={upcomingAssignment} />
            </div>
        </section>
    );
}