import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const CertificationStep = () => {
  const navigate = useNavigate();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger([
      "certification_number",
      "issue_date",
      "expiration_date",
    ]);

    if (!isValid) return;

    navigate("/vendor/contractors/create/drug-test");
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Certification</h3>
        <p className="text-sm text-[#4A6C8A]">Enter certification details.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>Certification Name</label>
          <input
            {...register("certification_name")}
            className={inputClassName}
          />
        </div>

        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>Certifying Body</label>
          <input {...register("certifying_body")} className={inputClassName} />
        </div>

        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>Certification Number</label>
          <input
            {...register("certification_number")}
            className={inputClassName}
          />
          {errors.certification_number && (
            <p className={errorClassName}>
              {errors.certification_number.message}
            </p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>Issue Date</label>
          <input
            type="date"
            {...register("issue_date")}
            className={inputClassName}
          />
          {errors.issue_date && (
            <p className={errorClassName}>{errors.issue_date.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label className={labelClassName}>Expiration Date</label>
          <input
            type="date"
            {...register("expiration_date")}
            className={inputClassName}
          />
          {errors.expiration_date && (
            <p className={errorClassName}>{errors.expiration_date.message}</p>
          )}
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label className={labelClassName}>Document URL</label>
          <input
            {...register("certification_document_url")}
            className={inputClassName}
          />
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label className={labelClassName}>Verified</label>
          <input type="checkbox" {...register("certification_verified")} />
        </div>

        <div className="flex justify-between sm:col-span-2">
          <button
            type="button"
            onClick={() =>
              navigate("/vendor/contractors/create/background-check")
            }
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

export { CertificationStep };
