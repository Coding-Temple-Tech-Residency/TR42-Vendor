import {
    type ContractorLocation,
    type Ticket,
    type CreateTicketPayload,
    type UpdateTicketAssignmentPayload,
} from "../types/ticket.types";

const API_BASE = "/api";

async function handleResponse<Ticket>(response: Response): Promise<Ticket> {
    if(!response.ok) {
        let message = "Something went wrong.";
        try {
            const errorData = await response.json();
            message = errorData?.message || message;
        } catch {
            // ignore json parse errors
        }
        throw new Error(message);
    }

    return response.json() as Promise<Ticket>;
}

export async function createTicket(payload: CreateTicketPayload): Promise<Ticket> {
    const response = await fetch(`${API_BASE}/tickets`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    return handleResponse<Ticket>(response);
}

export async function getTicketById(ticketId: string): Promise<Ticket> {
    const response = await fetch(`${API_BASE}/tickets/${ticketId}`);
    return handleResponse<Ticket>(response);
}

export async function assignContractorToTicket(
    ticketId: string,
    payload: UpdateTicketAssignmentPayload
): Promise<Ticket> {
    const response = await fetch(`${API_BASE}/tickets/${ticketId}/assign`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    return handleResponse<Ticket>(response);
}

export async function getActiveContractorLocations(): Promise<ContractorLocation[]> {
    const response = await fetch(`${API_BASE}/contractors/locations/active`);
    return handleResponse<ContractorLocation[]>(response);
}