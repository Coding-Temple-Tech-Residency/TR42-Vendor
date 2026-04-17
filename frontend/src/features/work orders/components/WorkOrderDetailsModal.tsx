import React from "react";
import { useWorkOrders } from "../hooks/useWorkOrders";

export interface WorkOrder {
  id: string;
  title?: string;
  description?: string;
  status?: string;
  priority?: string;
  assigned_vendor?: string;
  assigned_at?: string | null;
  created_at?: string;
  updated_at?: string;
  location_address?: string;
  city?: string;
  state?: string;
  zip_code?: string;
  service_type?: string;
  scheduled_date?: string | null;
}

interface WorkOrderDetailsModalProps {
  isOpen: boolean;
  onClose: () => void;
  workOrder: WorkOrder | null;
}

const formatLabel = (value?: string | null) => {
  if (!value) return "-";

  return value
    .replace(/_/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
};

const formatDate = (value?: string | null) => {
  if (!value) return "-";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) return value;

  return date.toLocaleString();
};

const DetailItem = ({
  label,
  value,
}: {
  label: string;
  value?: string | null;
}) => (
  <div className="rounded-lg border border-slate-200 bg-slate-50 p-3">
    <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
      {label}
    </p>
    <p className="mt-1 text-sm text-slate-800 wrap-break-words">
      {value || "-"}
    </p>
  </div>
);

const WorkOrderDetailsModal = ({
  isOpen,
  onClose,
  workOrder,
}: WorkOrderDetailsModalProps) => {
  if (!isOpen || !workOrder) return null;

  const {
    // activeWorkOrders,
    loading,
    unassignedCount,
    error,
    inProgressCount,
    assignedCount,
    completedInWeekCount,
    completedCount,
    // recurringCount,
    // avgCompletion,
    unassignedWorkOrders,
    // assignedWorkOrders,
    inProgressWorkOrders,
    recentlyCompleted,
    overDueCount,
    // overDueWorkOrders,
  } = useWorkOrders({ page: 1, perPage: 100, status: "all", scope: "vendor" });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/55 px-4">
      <div className="w-full max-s-3xl rounded-2xl bg-white shadow-2xl">
        <div className="flex items-start jusify-between border-b border-slate-200 px-6 py-4">
          <div>
            <p className="text-sm font-semibold uppercase tracking-wide text-[#1E3A5F]">
              Work Order Details
            </p>
            <h2 className="mt-1 text-xl font-bold text-slate-900">
              {workOrder.title || `Work Order #${workOrder.id}`}
            </h2>
            <p className="mt-1 text-sm text-slate-500">ID: {workOrder.id}</p>
          </div>
        </div>

        <div className="max-h-[75vh] overflow-y-auto px-6 py-5">
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <DetailItem label="Status" value={formatLabel(workOrder.status)} />
            <DetailItem
              label="Priority"
              value={formatLabel(workOrder.priority)}
            />
            <DetailItem
              label="Assigned Vendor"
              value={workOrder.assigned_vendor}
            />
            <DetailItem
              label="Assigned At"
              value={formatLabel(workOrder.assigned_at)}
            />
            <DetailItem label="Service Type" value={workOrder.service_type} />
            <DetailItem
              label="Scheduled Date"
              value={formatLabel(workOrder.scheduled_date)}
            />
            <DetailItem
              label="Created At"
              value={formatLabel(workOrder.created_at)}
            />
            <DetailItem
              label="Updated At"
              value={formatLabel(workOrder.updated_at)}
            />
            <DetailItem label="Address" value={workOrder.location_address} />
            <DetailItem label="City" value={workOrder.city} />
            <DetailItem label="State" value={workOrder.state} />
            <DetailItem label="Zip Code" value={workOrder.zip_code} />
          </div>

          <div className="mt-4 rounded-lg border border-slate-200 bg-slate-50 p-4">
            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
              Description
            </p>
            <p className="mt-2 text-sm leading-6 textg-slate-800">
              {workOrder.description || "-"}
            </p>
          </div>
        </div>

        <div className="flex justify-end gap-3 border-t border-slate-200 px-6 py-4">
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-semibold text-slate-700 transition hover:bg-slate-100"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
};

export default WorkOrderDetailsModal;
