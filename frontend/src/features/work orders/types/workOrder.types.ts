export type WorkOrderStatus = 
    | "pending"
    | "assigned"
    | "in_progress"
    | "completed"
    | "cancelled";

export type PriorityStatus = "low" | "medium" | "high" | "urgent";

export interface VendorSummary {
    vendor_id: string;
    name?: string;
}

export interface WellSummary {
    well_id: string;
    name?: string;
}

export interface WorkOrder {
    id: string;
    assigned_vendor: string | null;
    completed_at: string | null;
    description: string | null;
    due_date: string | null;
    estimated_start_date: string | null;
    estimated_end_date: string | null;
    current_status: WorkOrderStatus;
    priority: PriorityStatus;
    comments: string | null;
    location: string | null;
    estimated_cost: number | string | null;
    estimated_duration: string | null;
    well_id: string | null;
    updated_by: string;
    vendor?: VendorSummary | null;
    well?: WellSummary | null;
    created_at?: string | null;
    updated_at?: string | null;
}

export type WorkOrderSortOption = 
    | "due_date_asc"
    | "due_date_desc"
    | "priority_desc"
    | "status_asc"
    | "location_asc"
    | "created_at_desc";