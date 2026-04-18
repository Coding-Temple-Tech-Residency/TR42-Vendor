import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { toBackendPhoneFormat } from "../../../../../utils/validation";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const sectionClass =
  "rounded-xl border border-[#2F4F75] bg-[#F4F8FC] p-4 shadow-sm";
const labelClass = "text-xs text-[#4A6C8A]";
const valueClass = "text-sm text-[#2F4F75] font-medium";

const ReviewStep = () => {
  const navigate = useNavigate();
  const { getValues } = useFormContext<CreateContractorFormValues>();

  const data = getValues();

  const handleSubmit = async () => {
    const payload = {
      ...data,

      contact_number: toBackendPhoneFormat(data.contact_number),
      alternate_number: data.alternate_number
        ? toBackendPhoneFormat(data.alternate_number)
        : "",

      // convert nullable fields
      background_check_date:
        data.background_check_date === "" ? null : data.background_check_date,

      expiration_date:
        data.expiration_date === "" ? null : data.expiration_date,

      drug_test_date: data.drug_test_date === "" ? null : data.drug_test_date,

      coverage_amount:
        data.coverage_amount === "" ? null : Number(data.coverage_amount),

      deductible: data.deductible === "" ? null : Number(data.deductible),

      effective_date: data.effective_date === "" ? null : data.effective_date,

      insurance_document_url:
        data.insurance_document_url === "" ? null : data.insurance_document_url,

      additional_insured_certificate_url:
        data.additional_insured_certificate_url === ""
          ? null
          : data.additional_insured_certificate_url,

      license_document_url:
        data.license_document_url === "" ? null : data.license_document_url,
    };

    try {
      const response = await fetch("/api/contractors/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        console.error("Failed to create contractor");
        return;
      }

      navigate("/vendor/contractors");
    } catch (err) {
      console.error("Submit error", err);
    }
  };

  return (
    <section className="mx-12 mt-12 space-y-6">
      <h3 className="text-lg text-[#2F4F75]">Review Contractor</h3>

      {/* Basic Info */}
      <div className={sectionClass}>
        <h4 className="mb-2 font-semibold text-[#2F4F75]">Basic Info</h4>
        <div className="grid sm:grid-cols-2 gap-2">
          <div>
            <p className={labelClass}>Name</p>
            <p className={valueClass}>
              {data.first_name} {data.last_name}
            </p>
          </div>
          <div>
            <p className={labelClass}>Email</p>
            <p className={valueClass}>{data.email}</p>
          </div>
        </div>
      </div>

      {/* Address */}
      <div className={sectionClass}>
        <h4 className="mb-2 font-semibold text-[#2F4F75]">Address</h4>
        <p className={valueClass}>
          {data.address.street}, {data.address.city}, {data.address.state}{" "}
          {data.address.zip}
        </p>
      </div>

      {/* Background */}
      <div className={sectionClass}>
        <h4 className="mb-2 font-semibold text-[#2F4F75]">Background Check</h4>
        <p className={valueClass}>
          Passed: {data.background_check_passed ? "Yes" : "No"}
        </p>
      </div>

      {/* Certification */}
      <div className={sectionClass}>
        <h4 className="mb-2 font-semibold text-[#2F4F75]">Certification</h4>
        <p className={valueClass}>{data.certification_name}</p>
      </div>

      {/* Insurance */}
      <div className={sectionClass}>
        <h4 className="mb-2 font-semibold text-[#2F4F75]">Insurance</h4>
        <p className={valueClass}>{data.provider_name}</p>
      </div>

      {/* License */}
      <div className={sectionClass}>
        <h4 className="mb-2 font-semibold text-[#2F4F75]">License</h4>
        <p className={valueClass}>{data.license_number}</p>
      </div>

      {/* Actions */}
      <div className="flex justify-between">
        <button
          type="button"
          onClick={() => navigate("/vendor/contractors/create/license")}
          className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm text-[#2F4F75]"
        >
          Back
        </button>

        <button
          type="button"
          onClick={handleSubmit}
          className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm text-white hover:bg-[#4A6C8A]"
        >
          Create Contractor
        </button>
      </div>
    </section>
  );
};

export { ReviewStep };
