import { getAuthHeaders } from "../utils/authTokenUtils";

export type WorkOrderRow = {
  id: string;
  clientId: string;
  description: string;
  location: string;
  locationType: string | null;
  locationSummary: string;
  currentStatus: string;
  priority: string;
  serviceType: string;
  assignedVendorId: string | null;
  assignmentLabel: string;
  assignedAt: string | null;
  estimatedStartDate: string | null;
  estimatedEndDate: string | null;
  scheduleWindow: string;
  estimatedQuantity: number | null;
  units: string | null;
  quantityLabel: string;
  isRecurring: boolean;
  recurrenceType: string | null;
  recurrenceLabel: string;
  comments: string;
  createdAt: string | null;
  createdAtLabel: string;
  completedAt: string | null;
  completedAtLabel: string;
  cancelledAt: string | null;
  cancellationReason: string | null;
};

type GetVendorWorkOrdersParams = {
  page?: number;
  perPage?: number;
  status?: string;
  scope?: "all" | "vendor";
};

type WorkOrderApiResponse = {
  id?: string;
  work_order_id?: string;
  client_id: string;
  description?: string | null;
  location?: string | null;
  location_type?: string | null;
  current_status: string;
  priority: string;
  service_type: string;
  assigned_vendor?: string | null;
  assigned_at?: string | null;
  estimated_start_date?: string | null;
  estimated_end_date?: string | null;
  estimated_quantity?: number | null;
  units?: string | null;
  is_recurring?: boolean | null;
  recurrence_type?: string | null;
  comments?: string | null;
  created_at?: string | null;
  completed_at?: string | null;
  cancelled_at?: string | null;
  cancellation_reason?: string | null;
};

function formatDate(value?: string | null): string {
  if (!value) {
    return "N/A";
  }

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return "N/A";
  }

  return new Intl.DateTimeFormat("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  }).format(date);
}

function formatEnumLabel(value?: string | null): string {
  if (!value) {
    return "N/A";
  }

  return value
    .toLowerCase()
    .split("_")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function formatScheduleWindow(
  estimatedStartDate?: string | null,
  estimatedEndDate?: string | null,
): string {
  if (estimatedStartDate && estimatedEndDate) {
    return `${formatDate(estimatedStartDate)} - ${formatDate(estimatedEndDate)}`;
  }

  if (estimatedStartDate) {
    return `Starts ${formatDate(estimatedStartDate)}`;
  }

  if (estimatedEndDate) {
    return `Ends ${formatDate(estimatedEndDate)}`;
  }

  return "Unscheduled";
}

function mapWorkOrder(wo: WorkOrderApiResponse): WorkOrderRow {
  const workOrderId = wo.id ?? wo.work_order_id;
  if (!workOrderId) {
    throw new Error("Work order payload is missing an id");
  }

  const assignedVendorId = wo.assigned_vendor ?? null;
  const isRecurring = Boolean(wo.is_recurring);
  const quantityLabel =
    wo.estimated_quantity != null
      ? `${wo.estimated_quantity}${wo.units ? ` ${wo.units}` : ""}`
      : "N/A";
  const locationSummary = wo.location
    ? `${wo.location}${wo.location_type ? ` (${formatEnumLabel(wo.location_type)})` : ""}`
    : formatEnumLabel(wo.location_type);

  return {
    id: workOrderId,
    clientId: wo.client_id,
    description: wo.description ?? "No description provided",
    location: wo.location ?? "Location unavailable",
    locationType: wo.location_type ?? null,
    locationSummary,
    currentStatus: wo.current_status,
    priority: formatEnumLabel(wo.priority),
    serviceType: formatEnumLabel(wo.service_type),
    assignedVendorId,
    assignmentLabel: assignedVendorId ? "Assigned" : "Unassigned",
    assignedAt: wo.assigned_at ?? null,
    estimatedStartDate: wo.estimated_start_date ?? null,
    estimatedEndDate: wo.estimated_end_date ?? null,
    scheduleWindow: formatScheduleWindow(
      wo.estimated_start_date,
      wo.estimated_end_date,
    ),
    estimatedQuantity: wo.estimated_quantity ?? null,
    units: wo.units ?? null,
    quantityLabel,
    isRecurring,
    recurrenceType: wo.recurrence_type ?? null,
    recurrenceLabel: isRecurring
      ? formatEnumLabel(wo.recurrence_type) || "Recurring"
      : "One Time",
    comments: wo.comments ?? "",
    createdAt: wo.created_at ?? null,
    createdAtLabel: formatDate(wo.created_at),
    completedAt: wo.completed_at ?? null,
    completedAtLabel: formatDate(wo.completed_at),
    cancelledAt: wo.cancelled_at ?? null,
    cancellationReason: wo.cancellation_reason ?? null,
  };
}

export async function getVendorWorkOrders(
  params: GetVendorWorkOrdersParams = {},
): Promise<WorkOrderRow[]> {
  const { page = 1, perPage = 10, status = "all", scope = "all" } = params;

  const query = new URLSearchParams({
    page: String(page),
    per_page: String(perPage),
  });

  if (scope === "vendor" && status !== "all") {
    query.set("status", status);
  }

  const endpoint =
    scope === "vendor" ? "/api/work_orders/vendor" : "/api/work_orders/";

  const response = await fetch(`${endpoint}?${query.toString()}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
  });

  if (!response.ok) {
    if (response.status === 401)
      throw new Error("Session expired. Please log in again.");
    if (response.status === 403)
      throw new Error("You do not have permission to view this resource.");
    if (response.status === 500)
      throw new Error(
        "Server error while fetching work orders. Please try again later.",
      );
    throw new Error(`Failed to fetch work orders (${response.status})`);
  }

  const data = await response.json();

  return (data.work_orders ?? []).map((wo: WorkOrderApiResponse) =>
    mapWorkOrder(wo),
  );
}

export async function getWorkOrderById(id: string): Promise<WorkOrderRow> {
  const response = await fetch(`/api/work_orders/${encodeURIComponent(id)}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
  });

  if (!response.ok) {
    if (response.status === 401) {
      throw new Error("Session expired. Please log in again.");
    }
    if (response.status === 403) {
      throw new Error("You do not have permission to view this resource.");
    }
    if (response.status === 404) {
      throw new Error("Work order not found.");
    }
    if (response.status === 500) {
      throw new Error(
        "Server error while fetching work order details. Please try again later.",
      );
    }
    throw new Error(`Failed to fetch work order (${response.status})`);
  }

  const data: WorkOrderApiResponse = await response.json();
  return mapWorkOrder(data);
}