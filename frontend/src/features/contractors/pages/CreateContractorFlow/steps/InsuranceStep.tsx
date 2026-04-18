import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const InsuranceStep = () => {
  const navigate = useNavigate();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger([
      "insurance_type",
      "policy_number",
      "provider_name",
      "provider_phone",
      "coverage_amount",
      "deductible",
      "effective_date",
      "expiration_date",
      "insurance_document_url",
      "insurance_verified",
      "additional_insurance_required",
      "additional_insured_certificate_url",
    ]);

    if (!isValid) return;

    navigate("/vendor/contractors/create/license");
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Insurance</h3>
        <p className="text-sm text-[#4A6C8A]">
          Enter contractor insurance details.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={fieldWrapperClassName}>
          <label htmlFor="insurance_type" className={labelClassName}>
            Insurance Type
          </label>
          <input
            id="insurance_type"
            {...register("insurance_type")}
            className={inputClassName}
          />
          {errors.insurance_type && (
            <p className={errorClassName}>{errors.insurance_type.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="policy_number" className={labelClassName}>
            Policy Number
          </label>
          <input
            id="policy_number"
            {...register("policy_number")}
            className={inputClassName}
          />
          {errors.policy_number && (
            <p className={errorClassName}>{errors.policy_number.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="provider_name" className={labelClassName}>
            Provider Name
          </label>
          <input
            id="provider_name"
            {...register("provider_name")}
            className={inputClassName}
          />
          {errors.provider_name && (
            <p className={errorClassName}>{errors.provider_name.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="provider_phone" className={labelClassName}>
            Provider Phone
          </label>
          <input
            id="provider_phone"
            {...register("provider_phone")}
            className={inputClassName}
            placeholder="123-456-7890"
          />
          {errors.provider_phone && (
            <p className={errorClassName}>{errors.provider_phone.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="coverage_amount" className={labelClassName}>
            Coverage Amount
          </label>
          <input
            id="coverage_amount"
            {...register("coverage_amount")}
            className={inputClassName}
            placeholder="100000.00"
          />
          {errors.coverage_amount && (
            <p className={errorClassName}>{errors.coverage_amount.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="deductible" className={labelClassName}>
            Deductible
          </label>
          <input
            id="deductible"
            {...register("deductible")}
            className={inputClassName}
            placeholder="500.00"
          />
          {errors.deductible && (
            <p className={errorClassName}>{errors.deductible.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="effective_date" className={labelClassName}>
            Effective Date
          </label>
          <input
            id="effective_date"
            type="date"
            {...register("effective_date")}
            className={inputClassName}
          />
          {errors.effective_date && (
            <p className={errorClassName}>{errors.effective_date.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="expiration_date" className={labelClassName}>
            Expiration Date
          </label>
          <input
            id="expiration_date"
            type="date"
            {...register("expiration_date")}
            className={inputClassName}
          />
          {errors.expiration_date && (
            <p className={errorClassName}>{errors.expiration_date.message}</p>
          )}
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label htmlFor="insurance_document_url" className={labelClassName}>
            Insurance Document URL
          </label>
          <input
            id="insurance_document_url"
            {...register("insurance_document_url")}
            className={inputClassName}
          />
          {errors.insurance_document_url && (
            <p className={errorClassName}>
              {errors.insurance_document_url.message}
            </p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>Insurance Verified</label>
          <label className="mt-2 flex items-center gap-3 text-sm text-[#2F4F75]">
            <input
              type="checkbox"
              {...register("insurance_verified")}
              className="h-4 w-4 rounded border-[#2F4F75]"
            />
            Verified
          </label>
        </div>

        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>
            Additional Insurance Required
          </label>
          <label className="mt-2 flex items-center gap-3 text-sm text-[#2F4F75]">
            <input
              type="checkbox"
              {...register("additional_insurance_required")}
              className="h-4 w-4 rounded border-[#2F4F75]"
            />
            Required
          </label>
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label
            htmlFor="additional_insured_certificate_url"
            className={labelClassName}
          >
            Additional Insured Certificate URL
          </label>
          <input
            id="additional_insured_certificate_url"
            {...register("additional_insured_certificate_url")}
            className={inputClassName}
          />
          {errors.additional_insured_certificate_url && (
            <p className={errorClassName}>
              {errors.additional_insured_certificate_url.message}
            </p>
          )}
        </div>

        <div className="flex justify-between sm:col-span-2">
          <button
            type="button"
            onClick={() => navigate("/vendor/contractors/create/drug-test")}
            className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm text-[#2F4F75]"
          >
            Back
          </button>

          <button
            type="button"
            onClick={handleNext}
            className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm text-white hover:bg-[#4A6C8A]"
          >
            Next
          </button>
        </div>
      </div>
    </section>
  );
};

export { InsuranceStep };
