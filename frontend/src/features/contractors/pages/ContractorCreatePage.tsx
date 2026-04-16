import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import type { Contractor } from "../../../types/models";
import { toBackendPhoneFormat } from "../../../utils/validation";
import AppLayout from "../../components/layout/AppLayout";
import Sidebar from "../../components/layout/Sidebar";
import Topbar from "../../components/layout/Topbar";
import PageHeader from "../../components/UI/PageHeader";
import ContractorForm from "../components/ContractorForm";

export default function ContractorCreatePage() {
  const navigate = useNavigate();
  const [submitError, setSubmitError] = useState<string | null>(null);
  const [fieldErrors, setFieldErrors] = useState<
    Record<string, string | string[]>
  >({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleCreate = async (data: Contractor) => {
    try {
      setIsSubmitting(true);
      setSubmitError(null);
      setFieldErrors({});

      const payload = {
        ...data,
        contact_number: toBackendPhoneFormat(data.contact_number),
        alternate_number: data.alternate_number
          ? toBackendPhoneFormat(data.alternate_number)
          : "",
      };

      const response = await fetch("/api/contractors/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok) {
        if (response.status === 400 && result.messages) {
          setFieldErrors(result.messages);
          setSubmitError("Please correct the highlighted fields.");
        } else {
          setSubmitError(result.error || "Failed to create contractor.");
        }
        return;
      }

      navigate("/vendor/contractors");
    } catch {
      setSubmitError("Something went wrong while creating the contractor.");
    } finally {
      setIsSubmitting(false);
    }
  };
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <div className="space-y-6">
        <PageHeader
          title="Create Contractor"
          description="Add a new contractor to your vendor account."
        />

        <Link
          to="/vendor/contractors"
          className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
        >
          Back to Contractors
        </Link>

        {submitError && (
          <div className="rounded-lg border border-red-300 bg-red-50 px-4 py-3 text-sm text-red-700">
            {submitError}
          </div>
        )}

        <ContractorForm
          mode="create"
          onSave={handleCreate}
          externalErrors={fieldErrors}
        />
      </div>
    </AppLayout>
  );
}
