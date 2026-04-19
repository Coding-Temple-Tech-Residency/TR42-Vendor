import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  assignContractorToTicket,
  getActiveContractorLocations,
  getTicketById,
} from "../api/ticketApi";
import AssignmentPanel from "../components/AssignmentPanel";
import TicketInfoSection from "../components/TicketInfoSection";
import type { ContractorLocation, Ticket } from "../types/ticket.types";

export default function TicketDetailPage() {
  const { ticketId } = useParams<{ ticketId: string }>();

  // Replace with your auth source
  const currentUserId = "current-user-id";

  const [ticket, setTicket] = useState<Ticket | null>(null);
  const [contractors, setContractors] = useState<ContractorLocation[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isAssigning, setIsAssigning] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadPageData() {
      if (!ticketId) return;

      try {
        setIsLoading(true);
        setError("");

        const [ticketData, contractorData] = await Promise.all([
          getTicketById(ticketId),
          getActiveContractorLocations(),
        ]);

        setTicket(ticketData);
        setContractors(contractorData);
      } catch (err) {
        const message = err instanceof Error ? err.message : "Failed to load ticket details.";
        setError(message);
      } finally {
        setIsLoading(false);
      }
    }

    void loadPageData();
  }, [ticketId]);

  async function handleAssign(contractorId: string) {
    if (!ticketId) return;

    try {
      setIsAssigning(true);
      setError("");

      const updatedTicket = await assignContractorToTicket(ticketId, {
        assigned_contractor: contractorId,
        status: "assigned",
        updated_by: currentUserId,
      });

      setTicket(updatedTicket);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Failed to assign contractor.";
      setError(message);
    } finally {
      setIsAssigning(false);
    }
  }

  if (isLoading) {
    return (
      <div className="p-6">
        <div className="rounded-2xl bg-white p-6 shadow-sm">
          <p className="text-sm text-slate-500">Loading ticket...</p>
        </div>
      </div>
    );
  }

  if (!ticket) {
    return (
      <div className="p-6">
        <div className="rounded-2xl border border-red-200 bg-red-50 p-6 text-red-700">
          Ticket not found.
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6 p-6">
      {error && (
        <div className="rounded-2xl border border-red-200 bg-red-50 p-4 text-sm text-red-700">
          {error}
        </div>
      )}

      <TicketInfoSection ticket={ticket} />

      <AssignmentPanel
        ticket={ticket}
        contractors={contractors}
        onAssign={handleAssign}
        isAssigning={isAssigning}
        error={error}
      />
    </div>
  );
}