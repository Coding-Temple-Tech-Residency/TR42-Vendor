import type { TicketStatus } from "../types/ticket.types";

interface StatusBadgeProps {
    status?: TicketStatus | null;
}

const statusClasses: Record<TicketStatus, string> = {
    open: "bg-slate-100 text-slate-700",
    assigned: "bg-blue-100 text-blue-700",
    in_progress: "bg-amber-100 text-amber-700",
    completed: "bg-emerald-100 text-emerald-700",
    cancelled: "bg-rose-100 text-rose-700",
};

export default function StatusBadge({ status}: StatusBadgeProps) {
    const safeStatus = status ?? "open";

    return (
        <span
            className={`inline-flex rounded-full px-3 py-1 text-sm font-medium ${statusClasses[safeStatus]}`}
        >
            {safeStatus.replace("_", " ")}
        </span>
    );
}