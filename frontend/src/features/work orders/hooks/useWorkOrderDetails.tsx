import { useCallback, useEffect, useState } from "react";
import {
  getWorkOrderById,
  type WorkOrderRow,
} from "../../auth/services/workOrderService";

type UseWorkOrderDetailsOptions = {
  autoFetch?: boolean;
};

export function useWorkOrderDetails(
  id: string,
  { autoFetch = true }: UseWorkOrderDetailsOptions = {},
) {
  const [workOrder, setWorkOrder] = useState<WorkOrderRow | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchWorkOrderById = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const details = await getWorkOrderById(id);
      setWorkOrder(details);
    } catch (err: any) {
      setError(err?.message || "Failed to load work order details");
    } finally {
      setLoading(false);
    }
  }, [id]);

  useEffect(() => {
    if (autoFetch && id) fetchWorkOrderById();
  }, [autoFetch, fetchWorkOrderById, id]);

  return {
    workOrder,
    loading,
    error,
    refetch: fetchWorkOrderById,
  };
}
