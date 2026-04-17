import { useCallback, useEffect, useMemo, useState } from "react";
import {
  getVendorWorkOrders,
  type WorkOrderRow,
} from "../../auth/services/workOrderService";

type UseWorkOrdersOptions = {
  page?: number;
  perPage?: number;
  status?: string;
  scope?: "all" | "vendor";
  autoFetch?: boolean;
};

function toValidDate(value?: string | null): Date | null {
  if (!value) {
    return null;
  }

  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? null : date;
}

function isCompletedInCurrentWeek(value?: string | null): boolean {
  const completedDate = toValidDate(value);
  if (!completedDate) {
    return false;
  }

  const today = new Date();
  const startOfWeek = new Date(today);
  const dayOfWeek = today.getDay();
  const daysSinceMonday = dayOfWeek === 0 ? 6 : dayOfWeek - 1;

  startOfWeek.setDate(today.getDate() - daysSinceMonday);
  startOfWeek.setHours(0, 0, 0, 0);

  const startOfNextWeek = new Date(startOfWeek);
  startOfNextWeek.setDate(startOfWeek.getDate() + 7);

  return completedDate >= startOfWeek && completedDate < startOfNextWeek;
}

export function useWorkOrders(options: UseWorkOrdersOptions = {}) {
  const {
    page = 1,
    perPage = 10,
    status = "all",
    scope = "all",
    autoFetch = true,
  } = options;

  const [workOrders, setWorkOrders] = useState<WorkOrderRow[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchWorkOrders = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const rows = await getVendorWorkOrders({ page, perPage, status, scope });
      setWorkOrders(rows);
    } catch (err: any) {
      setError(err?.message || "Failed to load work orders");
    } finally {
      setLoading(false);
    }
  }, [page, perPage, scope, status]);

  useEffect(() => {
    if (autoFetch) fetchWorkOrders();
  }, [autoFetch, fetchWorkOrders]);

  const activeWorkOrders = useMemo(
    () =>
      workOrders.filter(
        (wo) =>
          wo.currentStatus !== "Completed" && wo.currentStatus !== "Cancelled",
      ),
    [workOrders],
  );

  const unassignedCount = useMemo(
    () =>
      activeWorkOrders.filter((wo) => wo.currentStatus === "Pending").length,
    [activeWorkOrders],
  );

  const assignedCount = useMemo(
    () =>
      activeWorkOrders.filter(
        (wo) => Boolean(wo.assignedVendorId) && wo.currentStatus !== "Pending",
      ).length,
    [activeWorkOrders],
  );

  const pendingCount = useMemo(
    () => workOrders.filter((wo) => wo.currentStatus === "Pending").length,
    [workOrders],
  );

  const completedInWeekCount = useMemo(() => {
    return workOrders.filter(
      (wo) =>
        wo.currentStatus === "Completed" &&
        isCompletedInCurrentWeek(wo.completedAt),
    ).length;
  }, [workOrders]);

  const completedCount = useMemo(
    () => workOrders.filter((wo) => wo.currentStatus === "Completed").length,
    [workOrders],
  );

  const inProgressCount = useMemo(
    () => workOrders.filter((wo) => wo.currentStatus === "In Progress").length,
    [workOrders],
  );

  const cancelledCount = useMemo(
    () => workOrders.filter((wo) => wo.currentStatus === "Cancelled").length,
    [workOrders],
  );

  const recurringCount = useMemo(
    () => activeWorkOrders.filter((wo) => wo.isRecurring).length,
    [activeWorkOrders],
  );

  const overDueCount = useMemo(() => {
    const today = new Date();
    return activeWorkOrders.filter((wo) => {
      const estimatedEndDate = toValidDate(wo.estimatedEndDate);
      return Boolean(estimatedEndDate && estimatedEndDate < today);
    }).length;
  }, [activeWorkOrders]);

  const unassignedWorkOrders = activeWorkOrders.filter(
    (wo) => wo.currentStatus === "Pending",
  );

  const assignedWorkOrders = activeWorkOrders.filter(
    (wo) => Boolean(wo.assignedVendorId) && wo.currentStatus !== "Pending",
  );

  const inProgressWorkOrders = activeWorkOrders.filter(
    (wo) => wo.currentStatus === "In Progress",
  );

  const recentlyCompleted = useMemo(
    () =>
      [...workOrders]
        .filter((wo) => wo.currentStatus === "Completed")
        .sort((left, right) => {
          const leftDate = toValidDate(left.completedAt)?.getTime() ?? 0;
          const rightDate = toValidDate(right.completedAt)?.getTime() ?? 0;
          return rightDate - leftDate;
        })
        .slice(0, 8),
    [workOrders],
  );

  const recurringWorkOrders = useMemo(
    () => activeWorkOrders.filter((wo) => wo.isRecurring),
    [activeWorkOrders],
  );

  const overDueWorkOrders = activeWorkOrders.filter((wo) => {
    const today = new Date();
    const estimatedEndDate = toValidDate(wo.estimatedEndDate);
    return Boolean(estimatedEndDate && estimatedEndDate < today);
  });

  const avgCompletion = useMemo(() => {
    const completedDurations = workOrders
      .filter((wo) => wo.currentStatus === "Completed")
      .map((wo) => {
        const startedAt = toValidDate(wo.assignedAt ?? wo.createdAt);
        const completedAt = toValidDate(wo.completedAt);

        if (!startedAt || !completedAt) {
          return null;
        }

        return completedAt.getTime() - startedAt.getTime();
      })
      .filter(
        (duration): duration is number => duration !== null && duration >= 0,
      );

    if (completedDurations.length === 0) {
      return "N/A";
    }

    const avgMs =
      completedDurations.reduce((sum, duration) => sum + duration, 0) /
      completedDurations.length;
    const avgDays = avgMs / (1000 * 60 * 60 * 24);

    return `${avgDays.toFixed(1)} days`;
  }, [workOrders]);

  // const workOrdersTrend = useMemo<TrendPoint[]>(() => {
  //   const today = new Date();
  //   const currentWeekStart = startOfWeek(today);
  //   const buckets = Array.from({ length: 4 }, (_, index) => {
  //     const offset = 3 - index;
  //     const bucketStart = new Date(currentWeekStart);
  //     bucketStart.setDate(currentWeekStart.getDate() - offset * 7);

  //     const bucketEnd = new Date(bucketStart);
  //     bucketEnd.setDate(bucketStart.getDate() + 7);

  //     return {
  //       day: `Week ${index + 1}`,
  //       start: bucketStart,
  //       end: bucketEnd,
  //       new: 0,
  //       completed: 0,
  //     };
  //   });

  //   for (const workOrder of workOrders) {
  //     const createdAt = toValidDate(workOrder.createdAt);
  //     const completedAt = toValidDate(workOrder.completedAt);

  //     for (const bucket of buckets) {
  //       if (createdAt && createdAt >= bucket.start && createdAt < bucket.end) {
  //         bucket.new += 1;
  //       }

  //       if (completedAt && completedAt >= bucket.start && completedAt < bucket.end) {
  //         bucket.completed += 1;
  //       }
  //     }
  //   }

  //   return buckets.map(({ day, new: newCount, completed }) => ({
  //     day,
  //     new: newCount,
  //     completed,
  //   }));
  // }, [workOrders]);

  return {
    workOrders,
    activeWorkOrders,
    loading,
    error,
    refetch: fetchWorkOrders,
    unassignedCount,
    assignedCount,
    pendingCount,
    completedInWeekCount,
    completedCount,
    inProgressCount,
    cancelledCount,
    recurringCount,
    avgCompletion,
    unassignedWorkOrders,
    assignedWorkOrders,
    inProgressWorkOrders,
    recentlyCompleted,
    recurringWorkOrders,
    overDueWorkOrders,
    overDueCount,
    // workOrdersTrend,
  };
}
