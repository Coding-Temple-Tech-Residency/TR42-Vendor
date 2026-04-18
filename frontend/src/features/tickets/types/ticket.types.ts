export type TicketStatus = 
    | "open"
    | "assigned"
    | "in_progress"
    | "completed"
    | "cancelled"

export type TicketPriority = "low" | "medium" | "high" | "urgent";

export interface Ticket {
    ticket_id: string;
    invoice_id?: string | null;
    work_order_id: string;
    description: string;
    assigned_contractor?: string | null;
    vendor_id?: string | null;
    priority?: TicketPriority | null;
    status?: TicketStatus | null;
    start_date: string;
    due_date: string;
    estimated_duration?: string | null;
    notes?: string | null;
    contractor_start_lat?: number | null;
    contractor_start_lng?: number | null;
    contractor_end_lat?: number | null;
    contractor_end_lng?: number | null;
    estimated_quantity?: number | null;
    unit?: string | null;
    special_requirements?: string | null;
    anomaly_flag?: boolean;
    anomaly_reason?: string | null;
    created_at?: string | null;
    updated_at?: string | null;
    created_by: string;
    updated_by?: string | null;
}

export interface CreateTicketPayload {
    work_order_id: string;
    description: string;
    vendor_id?: string | null;
    priority?: TicketPriority | null;
    status?: TicketStatus | null;
    start_date: string;
    due_date: string;
    estimated_duration?: string | null;
    notes?: string | null;
    estimated_quantity?: number | null;
    unit?: string | null;
    special_requirements?: string | null;
    created_by: string;
}

export interface UpdateTicketAssignmentPayload {
    assigned_contractor: string;
    status?: TicketStatus;
    updated_by: string;
}

export interface ContractorLocation {
    contractor_id: string;
    contractor_name: string;
    vendor_name?: string;
    status: "available" | "on_job" | "offline";
    current_job_title?: string;
    lat: number;
    lng: number;
}

export interface ContractorOption {
    contractor_id: string;
    contractor_name: string;
    vendor_id?: string | null;
}