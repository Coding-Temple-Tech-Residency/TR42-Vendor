import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const BackgroundStep = () => {
  const navigate = useNavigate();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger([
      "background_check_passed",
      "background_check_date",
      "background_check_provider",
    ]);

    if (!isValid) return;

    navigate("/vendor/contractors/create/certification");
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Background Check</h3>
        <p className="text-sm text-[#4A6C8A]">
          Enter the contractor background check details.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label className={labelClassName}>Background Check Passed</label>
          <label className="mt-2 flex items-center gap-3 text-sm text-[#2F4F75]">
            <input
              type="checkbox"
              {...register("background_check_passed")}
              className="h-4 w-4 rounded border-[#2F4F75]"
            />
            Mark as passed
          </label>
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="background_check_date" className={labelClassName}>
            Check Date
          </label>
          <input
            id="background_check_date"
            type="date"
            {...register("background_check_date")}
            className={inputClassName}
          />
          {errors.background_check_date && (
            <p className={errorClassName}>
              {errors.background_check_date.message}
            </p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="background_check_provider" className={labelClassName}>
            Provider
          </label>
          <input
            id="background_check_provider"
            {...register("background_check_provider")}
            className={inputClassName}
            placeholder="Enter provider"
          />
          {errors.background_check_provider && (
            <p className={errorClassName}>
              {errors.background_check_provider.message}
            </p>
          )}
        </div>

        <div className="flex justify-between sm:col-span-2">
          <button
            type="button"
            onClick={() => navigate("/vendor/contractors/create/address")}
            className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm font-medium text-[#2F4F75]"
          >
            Back
          </button>

          <button
            type="button"
            onClick={handleNext}
            className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white transition hover:bg-[#4A6C8A]"
          >
            Next
          </button>
        </div>
      </div>
    </section>
  );
};

export { BackgroundStep };
