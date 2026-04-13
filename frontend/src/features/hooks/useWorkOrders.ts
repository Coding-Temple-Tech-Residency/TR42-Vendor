import { useCallback, useEffect, useMemo, useState } from "react";
import {
  getVendorWorkOrders,
  type WorkOrderRow,
} from "../../features/auth/services/workOrderService";

type UseWorkOrdersOptions = {
  page?: number;
  perPage?: number;
  current_status?: string;
  autoFetch?: boolean;
};

export function useWorkOrders(options: UseWorkOrdersOptions = {}) {
  const {
    page = 1,
    perPage = 10,
    current_status = "all",
    autoFetch = true,
  } = options;

  const [workOrders, setWorkOrders] = useState<WorkOrderRow[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchWorkOrders = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const rows = await getVendorWorkOrders({ page, perPage, current_status });
      setWorkOrders(rows);
    } catch (err: any) {
      setError(err?.message || "Failed to load work orders");
    } finally {
      setLoading(false);
    }
  }, [page, perPage, current_status]);

  useEffect(() => {
    if (autoFetch) fetchWorkOrders();
  }, [autoFetch, fetchWorkOrders]);

  const unassignedCount = useMemo(
    () => workOrders.filter((wo) => wo.assignedTo === "Unassigned").length,
    [workOrders],
  );

  const assignedCount = useMemo(
    () => workOrders.filter((wo) => wo.assignedTo !== "Assigned").length,
    [workOrders],
  );

  const completedInWeekCount = useMemo(() => {
    const today = new Date();
    const startOfWeek = new Date(today);
    startOfWeek.setDate(today.getDate() - today.getDay());
    startOfWeek.setHours(0, 0, 0, 0);

    const endOfWeek = new Date(startOfWeek);
    endOfWeek.setDate(startOfWeek.getDate() + 6);
    endOfWeek.setHours(23, 59, 59, 999);

    return workOrders.filter((wo) => {
      if (wo.current_status !== "Completed" || wo.dueDate === null)
        return false;
      const completedDate = new Date(wo.completed_at);
      return completedDate >= startOfWeek && completedDate <= endOfWeek;
    }).length;
  }, [workOrders]);

  const completedCount = useMemo(
    () => workOrders.filter((wo) => wo.current_status === "Completed").length,
    [workOrders],
  );

  const inProgressCount = useMemo(
    () => workOrders.filter((wo) => wo.current_status === "In Progress").length,
    [workOrders],
  );

  const overDueCount = useMemo(() => {
    const today = new Date();
    return workOrders.filter((wo) => {
      const dueDate = new Date(wo.dueDate);
      return dueDate < today && wo.current_status !== "Completed";
    }).length;
  }, [workOrders]);

  const unassignedWorkOrders = workOrders.filter(
    (wo) => wo.assignedTo === "Unassigned" && wo.current_status === "Unassigned",
  );

  const assignedWorkOrders = workOrders.filter(
    (wo) => wo.assignedTo !== "Unassigned" && wo.current_status === "Assigned",
  );

  const inProgressWorkOrders = workOrders.filter(
    (wo) => wo.current_status === "In Progress",
  );

  const recentlyCompleted = workOrders.filter(
    (wo) => wo.current_status === "Completed",
  );

  const overDueWorkOrders = workOrders.filter((wo) => {
    const today = new Date();
    const dueDate = new Date(wo.dueDate);
    return dueDate < today && wo.current_status !== "Completed";
  });

  return {
    workOrders,
    loading,
    error,
    refetch: fetchWorkOrders,
    unassignedCount,
    assignedCount,
    completedInWeekCount,
    completedCount,
    inProgressCount,
    unassignedWorkOrders,
    assignedWorkOrders,
    inProgressWorkOrders,
    recentlyCompleted,
    overDueWorkOrders,
    overDueCount,
  };
}
