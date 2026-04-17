import { useMemo } from "react";
import type {
  PriorityStatus,
  WorkOrder,
  WorkOrderSortOption,
  WorkOrderStatus,
} from "../types/workOrder.types";

interface UseFilteredWorkOrderProps {
  workOrders: WorkOrder[];
  searchTerm: string;
  statusFilter: WorkOrderStatus | "all";
  priorityFilter: PriorityStatus | "all";
  assignmentFilter: "all" | "assigned" | "unassigned";
  sortBy: WorkOrderSortOption;
}

const priorityRank: Record<PriorityStatus, number> = {
  low: 1,
  medium: 2,
  high: 3,
  urgent: 4,
};

const getTimestamp = (value?: string | null): number => {
  if (!value) return 0;

  const timestamp = new Date(value).getTime();
  return Number.isNaN(timestamp) ? 0 : timestamp;
};

const getSafeString = (value?: string | null): string =>
  value?.toLowerCase() ?? "";

export const useFilteredWorkOrders = ({
  workOrders,
  searchTerm,
  statusFilter,
  priorityFilter,
  assignmentFilter,
  sortBy,
}: UseFilteredWorkOrderProps) => {
  return useMemo(() => {
    let results = [...workOrders];

    const trimmedSearch = searchTerm.trim().toLowerCase();

    if (trimmedSearch) {
      results = results.filter((workOrder) => {
        const searchableValues = [
          workOrder.id,
          workOrder.description,
          workOrder.comments,
          workOrder.location,
          workOrder.current_status,
          workOrder.priority,
          workOrder.assigned_vendor,
          workOrder.well_id,
          workOrder.vendor?.name,
          workOrder.well?.name,
        ];

        return searchableValues.some((value) =>
          getSafeString(value).includes(trimmedSearch),
        );
      });
    }

    if (statusFilter !== "all") {
      results = results.filter(
        (workOrder) => workOrder.current_status === statusFilter,
      );
    }

    if (priorityFilter !== "all") {
      results = results.filter(
        (workOrder) => workOrder.priority === priorityFilter,
      );
    }

    if (assignmentFilter === "assigned") {
      results = results.filter((workOrder) =>
        Boolean(workOrder.assigned_vendor),
      );
    }

    if (assignmentFilter === "unassigned") {
      results = results.filter((workOrder) => !workOrder.assigned_vendor);
    }

    results.sort((a, b) => {
      switch (sortBy) {
        case "due_date_asc":
          return getTimestamp(a.due_date) - getTimestamp(b.due_date);

        case "due_date_desc":
          return getTimestamp(b.due_date) - getTimestamp(a.due_date);

        case "priority_desc":
          return priorityRank[b.priority] - priorityRank[a.priority];

        case "status_asc":
          return a.current_status.localeCompare(b.current_status);

        case "location_asc":
          return getSafeString(a.location).localeCompare(
            getSafeString(b.location),
          );

        case "created_at_desc":
        default:
          return getTimestamp(b.created_at) - getTimestamp(a.created_at);
      }
    });

    return results;
  }, [
    workOrders,
    searchTerm,
    statusFilter,
    priorityFilter,
    assignmentFilter,
    sortBy,
  ]);
};
