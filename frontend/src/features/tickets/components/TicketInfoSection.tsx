import type { Ticket } from "../types/ticket.types";
import PriorityBadge from "./PriorityBadge";
import StatusBadge from "./StatusBadge";

interface TicketInfoSectionProps {
  ticket: Ticket;
}

function formatDate(value?: string | null) {
  if (!value) return "—";
  return new Date(value).toLocaleString();
}

export default function TicketInfoSection({ ticket }: TicketInfoSectionProps) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <div className="flex flex-col gap-4 border-b border-slate-200 pb-6 md:flex-row md:items-start md:justify-between">
        <div>
          <p className="text-sm text-slate-500">Ticket ID</p>
          <h1 className="mt-1 text-2xl font-bold text-slate-900">{ticket.ticket_id}</h1>
          <p className="mt-2 text-sm text-slate-500">Work Order: {ticket.work_order_id}</p>
        </div>

        <div className="flex gap-2">
          <StatusBadge status={ticket.status} />
          <PriorityBadge priority={ticket.priority} />
        </div>
      </div>

      <div className="grid gap-6 pt-6 md:grid-cols-2">
        <div>
          <h2 className="mb-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
            Description
          </h2>
          <p className="text-sm leading-6 text-slate-700">{ticket.description || "—"}</p>
        </div>

        <div>
          <h2 className="mb-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
            Assignment
          </h2>
          <div className="space-y-2 text-sm text-slate-700">
            <p>
              <span className="font-medium">Assigned Contractor:</span>{" "}
              {ticket.assigned_contractor || "Unassigned"}
            </p>
            <p>
              <span className="font-medium">Vendor:</span> {ticket.vendor_id || "—"}
            </p>
          </div>
        </div>

        <div>
          <h2 className="mb-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
            Dates
          </h2>
          <div className="space-y-2 text-sm text-slate-700">
            <p>
              <span className="font-medium">Start:</span> {formatDate(ticket.start_date)}
            </p>
            <p>
              <span className="font-medium">Due:</span> {formatDate(ticket.due_date)}
            </p>
            <p>
              <span className="font-medium">Estimated Duration:</span>{" "}
              {ticket.estimated_duration || "—"}
            </p>
          </div>
        </div>

        <div>
          <h2 className="mb-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
            Quantity & Requirements
          </h2>
          <div className="space-y-2 text-sm text-slate-700">
            <p>
              <span className="font-medium">Estimated Quantity:</span>{" "}
              {ticket.estimated_quantity ?? "—"}
            </p>
            <p>
              <span className="font-medium">Unit:</span> {ticket.unit || "—"}
            </p>
            <p>
              <span className="font-medium">Special Requirements:</span>{" "}
              {ticket.special_requirements || "—"}
            </p>
          </div>
        </div>

        <div className="md:col-span-2">
          <h2 className="mb-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
            Notes
          </h2>
          <p className="text-sm leading-6 text-slate-700">{ticket.notes || "—"}</p>
        </div>

        {ticket.anomaly_flag && (
          <div className="md:col-span-2 rounded-xl border border-amber-200 bg-amber-50 p-4">
            <h2 className="mb-2 text-sm font-semibold text-amber-800">Anomaly Flagged</h2>
            <p className="text-sm text-amber-700">{ticket.anomaly_reason || "No reason provided."}</p>
          </div>
        )}
      </div>
    </div>
  );
}