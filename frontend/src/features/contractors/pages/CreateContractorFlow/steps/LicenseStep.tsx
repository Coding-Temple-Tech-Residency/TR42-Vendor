import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const LicenseStep = () => {
  const navigate = useNavigate();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger([
      "license_type",
      "license_number",
      "license_state",
      "license_expiration_date",
      "license_document_url",
      "license_verified",
    ]);

    if (!isValid) return;

    navigate("/vendor/contractors/create/review");
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">License</h3>
        <p className="text-sm text-[#4A6C8A]">
          Enter contractor license details.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={fieldWrapperClassName}>
          <label htmlFor="license_type" className={labelClassName}>
            License Type
          </label>
          <input
            id="license_type"
            {...register("license_type")}
            className={inputClassName}
          />
          {errors.license_type && (
            <p className={errorClassName}>{errors.license_type.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="license_number" className={labelClassName}>
            License Number
          </label>
          <input
            id="license_number"
            {...register("license_number")}
            className={inputClassName}
          />
          {errors.license_number && (
            <p className={errorClassName}>{errors.license_number.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="license_state" className={labelClassName}>
            License State
          </label>
          <input
            id="license_state"
            {...register("license_state")}
            className={inputClassName}
            placeholder="TX"
            maxLength={2}
          />
          {errors.license_state && (
            <p className={errorClassName}>{errors.license_state.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="license_expiration_date" className={labelClassName}>
            License Expiration Date
          </label>
          <input
            id="license_expiration_date"
            type="date"
            {...register("license_expiration_date")}
            className={inputClassName}
          />
          {errors.license_expiration_date && (
            <p className={errorClassName}>
              {errors.license_expiration_date.message}
            </p>
          )}
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label htmlFor="license_document_url" className={labelClassName}>
            License Document URL
          </label>
          <input
            id="license_document_url"
            {...register("license_document_url")}
            className={inputClassName}
          />
          {errors.license_document_url && (
            <p className={errorClassName}>
              {errors.license_document_url.message}
            </p>
          )}
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label className={labelClassName}>License Verified</label>
          <label className="mt-2 flex items-center gap-3 text-sm text-[#2F4F75]">
            <input
              type="checkbox"
              {...register("license_verified")}
              className="h-4 w-4 rounded border-[#2F4F75]"
            />
            Verified
          </label>
        </div>

        <div className="flex justify-between sm:col-span-2">
          <button
            type="button"
            onClick={() => navigate("/vendor/contractors/create/insurance")}
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

export { LicenseStep };
