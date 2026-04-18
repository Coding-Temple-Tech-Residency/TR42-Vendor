import type { TicketPriority } from "../types/ticket.types";

interface PriorityBadgeProps {
    priority?: TicketPriority | null;
}

const priorityClasses: Record<TicketPriority, string> = {
    low: "bg-slate-100 text-slate-700",
    medium: "bg-sky-100 text-sky-700",
    high: "bg-orange-100 text-orange-700",
    urgent: "bg-red-100 text-red-700",
};

export default function PriorityBadge({ priority }: PriorityBadgeProps) {
    if (!priority) return null;

    return (
        <span
            className={`inline-flex rounded-full px-3 py-1 text-sm font-medium ${priorityClasses[priority]}`}
        >
            {priority}
        </span>
    );
}