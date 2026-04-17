import { useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import TicketForm from "../components/TicketForm";
import { createTicket } from "../api/ticketApi";
import type { CreateTicketPayload } from "../types/ticket.types";

export default function CreateTicketPage() {
  const navigate = useNavigate();
  const { workOrderId } = useParams<{ workOrderId: string }>();

  // Replace with actual auth/user hook
  const currentUserId = "current-user-id";

  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const initialFormState = useMemo<CreateTicketPayload>(
    () => ({
      work_order_id: workOrderId ?? "",
      description: "",
      vendor_id: "",
      priority: "medium",
      status: "open",
      start_date: "",
      due_date: "",
      estimated_duration: "",
      notes: "",
      estimated_quantity: null,
      unit: "",
      special_requirements: "",
      created_by: currentUserId,
    }),
    [workOrderId, currentUserId]
  );

  const [formData, setFormData] = useState<CreateTicketPayload>(initialFormState);

  function handleChange(
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) {
    const { name, value } = event.target;

    setFormData((prev) => ({
      ...prev,
      [name]:
        name === "estimated_quantity"
          ? value === ""
            ? null
            : Number(value)
          : value,
    }));
  }

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");

    if (!formData.work_order_id) {
      setError("Missing work order. Please start ticket creation from a work order.");
      return;
    }

    if (new Date(formData.due_date) < new Date(formData.start_date)) {
      setError("Due date cannot be before start date.");
      return;
    }

    try {
      setIsSubmitting(true);
      const createdTicket = await createTicket(formData);
      navigate(`/tickets/${createdTicket.ticket_id}`);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Failed to create ticket.";
      setError(message);
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <div className="space-y-6 p-6">
      <div>
        <h1 className="text-2xl font-bold text-slate-900">New Ticket</h1>
        <p className="mt-1 text-sm text-slate-500">
          Create the ticket first, then assign the best contractor from the ticket details page.
        </p>
      </div>

      <div className="rounded-2xl bg-slate-50 p-4 text-sm text-slate-600">
        <span className="font-medium text-slate-800">Work Order:</span> {formData.work_order_id}
      </div>

      <TicketForm
        formData={formData}
        onChange={handleChange}
        onSubmit={handleSubmit}
        isSubmitting={isSubmitting}
        error={error}
      />
    </div>
  );
}