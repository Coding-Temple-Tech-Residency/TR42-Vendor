import { useMemo, useState } from "react";
import type { ContractorLocation, Ticket } from "../types/ticket.types";

interface AssignmentPanelProps {
  ticket: Ticket;
  contractors: ContractorLocation[];
  onAssign: (contractorId: string) => Promise<void>;
  isAssigning: boolean;
  error: string;
}

export default function AssignmentPanel({
  ticket,
  contractors,
  onAssign,
  isAssigning,
  error,
}: AssignmentPanelProps) {
  const [selectedContractorId, setSelectedContractorId] = useState<string>("");

  const sortedContractors = useMemo(() => {
    return [...contractors].sort((a, b) => {
      if (a.status === "available" && b.status !== "available") return -1;
      if (a.status !== "available" && b.status === "available") return 1;
      return a.contractor_name.localeCompare(b.contractor_name);
    });
  }, [contractors]);

  async function handleAssign() {
    if (!selectedContractorId) return;
    await onAssign(selectedContractorId);
  }

  return (
    <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
      <div className="rounded-2xl bg-white p-6 shadow-sm">
        <div className="mb-4">
          <h2 className="text-lg font-semibold text-slate-900">Contractor Assignment Map</h2>
          <p className="mt-1 text-sm text-slate-500">
            Show all active contractors on jobs here. Select one to assign this ticket.
          </p>
        </div>

        <div className="flex min-h-[420px] items-center justify-center rounded-2xl border border-dashed border-slate-300 bg-slate-50 text-center text-sm text-slate-500">
          Replace this container with your Leaflet map component.
        </div>
      </div>

      <div className="rounded-2xl bg-white p-6 shadow-sm">
        <div className="mb-4">
          <h2 className="text-lg font-semibold text-slate-900">Assign Contractor</h2>
          <p className="mt-1 text-sm text-slate-500">
            Ticket status:{" "}
            <span className="font-medium text-slate-700">{ticket.status || "open"}</span>
          </p>
        </div>

        {error && (
          <div className="mb-4 rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {error}
          </div>
        )}

        <div className="space-y-3">
          {sortedContractors.map((contractor) => {
            const isSelected = selectedContractorId === contractor.contractor_id;

            return (
              <button
                key={contractor.contractor_id}
                type="button"
                onClick={() => setSelectedContractorId(contractor.contractor_id)}
                className={`w-full rounded-xl border p-4 text-left transition ${
                  isSelected
                    ? "border-slate-900 bg-slate-50"
                    : "border-slate-200 hover:border-slate-400"
                }`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <p className="font-semibold text-slate-900">{contractor.contractor_name}</p>
                    <p className="mt-1 text-sm text-slate-500">
                      {contractor.vendor_name || "No vendor"}
                    </p>
                    <p className="mt-2 text-sm text-slate-600">
                      Current Job: {contractor.current_job_title || "No active job listed"}
                    </p>
                  </div>

                  <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-700">
                    {contractor.status.replace("_", " ")}
                  </span>
                </div>
              </button>
            );
          })}
        </div>

        <button
          type="button"
          disabled={isAssigning || !selectedContractorId}
          onClick={handleAssign}
          className="mt-6 w-full rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {isAssigning ? "Assigning..." : "Assign Contractor"}
        </button>
      </div>
    </div>
  );
}