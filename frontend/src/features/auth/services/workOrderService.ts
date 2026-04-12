import { getAuthHeaders } from "../utils/authTokenUtils";

export async function getOpenWorkOrders(
    page: number = 1,
    perPage: number = 10
): Promise<any> {
    try {
        const url = `api/work_orders/vendor?page=${page}&per_page=${perPage}`;
        const headers = getAuthHeaders();

        const response = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                ...headers,
            }
        });

        if (!response.ok) {
            if (response.status === 401) {
                throw new Error("Session expired. Please log in again.");
            }
            if (response.status === 403) {
                throw new Error("You do not have permission to view this resource.");
            }
            throw new Error(`Failed to fetch work orders. ${response.statusText}`);
        }

        const data = await response.json();

        const workOrders = data.work_orders.map((wo: any) => ({
            id: wo.work_order_id,
            location: wo.location,
            current_status: wo.current_status,
            assignedTo: wo.assigned_vendor_name || "Unassigned",
            dueDate: wo.due_date ? new Date(wo.due_date).toLocaleDateString() : "N/A",
        }));

        return workOrders;
    } catch (error) {
        console.error("Error fetching work orders:", error);
        throw error;
    }
}