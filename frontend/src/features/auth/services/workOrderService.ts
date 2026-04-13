import { getAuthHeaders } from "../utils/authTokenUtils";

export type WorkOrderRow = {
  id: string;
  location: string;
  current_status: string;
  assignedTo: string;
  dueDate: string;
};

type GetVendorWorkOrdersParams = {
  page?: number;
  perPage?: number;
  current_status?: string;
};

export async function getVendorWorkOrders(
  params: GetVendorWorkOrdersParams = {},
): Promise<WorkOrderRow[]> {
  const { page = 1, perPage = 10, current_status = "all" } = params;

  const query = new URLSearchParams({
    page: String(page),
    per_page: String(perPage),
    current_status,
  });

  const response = await fetch(`/api/work_orders/vendor?${query.toString()}`, {
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

  return (data.work_orders ?? []).map((wo: any) => ({
    id: wo.work_order_id,
    location: wo.location,
    current_status: wo.current_status,
    assignedTo: wo.assigned_vendor_name || "Unassigned",
    dueDate: wo.due_date ? new Date(wo.due_date).toLocaleDateString() : "N/A",
  }));
}