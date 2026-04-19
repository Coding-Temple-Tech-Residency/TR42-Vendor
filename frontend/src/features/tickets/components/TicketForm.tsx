import type {
  ContractorOption,
  CreateTicketPayload,
  TicketPriority,
  TicketStatus,
} from "../types/ticket.types";

interface TicketFormProps {
  formData: CreateTicketPayload;
  onChange: (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >,
  ) => void;
  onSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
  isSubmitting: boolean;
  error: string;
  vendorOptions?: { vendor_id: string; vendor_name: string }[];
  contractorOptions?: ContractorOption[];
}

const priorities: TicketPriority[] = ["low", "medium", "high", "urgent"];
const statuses: TicketStatus[] = [
  "open",
  "assigned",
  "in_progress",
  "completed",
  "cancelled",
];

export default function TicketForm({
  formData,
  onChange,
  onSubmit,
  isSubmitting,
  error,
  vendorOptions = [],
}: TicketFormProps) {
  return (
    <form
      onSubmit={onSubmit}
      className="space-y-6 rounded-2xl bg-white p-6 shadow-lg"
    >
      <div>
        <h2 className="text-xl font-semibold text-slate-900">Create Ticket</h2>
        <p className="mt-1 text-sm text-slate-500">
          Add the ticket details first. Contractor assignment happens after
          creation.
        </p>
      </div>

      {error && (
        <div className="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          {error}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-2">
        <div className="md:col-span-2">
          <label
            htmlFor="description"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Description
          </label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={onChange}
            rows={4}
            required
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
            placeholder="Describe the work being completed"
          />
        </div>

        <div>
          <label
            htmlFor="priority"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Priority
          </label>
          <select
            id="priority"
            name="priority"
            value={formData.priority ?? ""}
            onChange={onChange}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
          >
            <option value="">Select Priority</option>
            {priorities.map((priority) => (
              <option key={priority} value={priority}>
                {priority}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label
            htmlFor="status"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Status
          </label>
          <select
            id="status"
            name="status"
            value={formData.status ?? "open"}
            onChange={onChange}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
          >
            {statuses.map((status) => (
              <option key={status} value={status}>
                {status.replace("_", " ")}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label
            htmlFor="start_date"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Due Date
          </label>
          <input
            id="due_date"
            name="due_date"
            type="datetime-local"
            value={formData.due_date}
            onChange={onChange}
            required
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
          />
        </div>

        <div>
          <label
            htmlFor="estimated_duration"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Estimated Duration
          </label>
          <input
            id="estimated_duration"
            name="estimated_duration"
            type="text"
            value={formData.estimated_duration ?? ""}
            onChange={onChange}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
            placeholder="ex. 2hours"
          />
        </div>

        <div>
          <label
            htmlFor="vendor_id"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Vendor
          </label>
          <select
            id="vendor_id"
            name="vendor_id"
            value={formData.vendor_id ?? ""}
            onChange={onChange}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
          >
            <option value="">Select vendor</option>
            {vendorOptions.map((vendor) => (
              <option key={vendor.vendor_id} value={vendor.vendor_id}>
                {vendor.vendor_name}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label
            htmlFor="estimated_quantity"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Estimated Quantity
          </label>
          <select
            id="estimated_quantity"
            name="estimated_quantity"
            type="number"
            value={formData.estimated_quantity ?? ""}
            onChange={onChange}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
            placeholder="Enter quantity"
          />
        </div>

        <div>
          <label
            htmlFor="unit"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Unit
          </label>
          <input
            id="unit"
            name="unit"
            type="text"
            value={formData.unit ?? ""}
            onChange={onChange}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
            placeholder="barrels"
          />
        </div>

        <div className="md:col-span-2">
          <label
            htmlFor="special_requirements"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Special Requirements
          </label>
          <input
            id="special_requirements"
            name="special_requirements"
            type="text"
            value={formData.special_requirements ?? ""}
            onChange={onChange}
            rows={3}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
            placeholder="Any special handling, compliances, equiptment, or job requirements."
          />
        </div>

        <div className="md:col-span-2">
          <label
            htmlFor="notes"
            className="mb-2 block text-sm font-medium text-slate-700"
          >
            Notes
          </label>
          <textarea
            id="notes"
            name="notes"
            value={formData.notes ?? ""}
            onChange={onChange}
            rows={3}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-slate-500"
            placeholder="Additional internal notes"
          />
        </div>
      </div>

      <div className="flex justify-end">
        <button
            type="submit"
            disabled={isSubmitting}
            className="rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
        >
            {isSubmitting ? "Creating...": "Create Ticket"}
        </button>
      </div>
    </form>
  );
}
