import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const DrugTestStep = () => {
  const navigate = useNavigate();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger(["drug_test_passed", "drug_test_date"]);

    if (!isValid) return;

    navigate("/vendor/contractors/create/insurance");
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Drug Test</h3>
        <p className="text-sm text-[#4A6C8A]">Enter drug test details.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label className={labelClassName}>Drug Test Passed</label>
          <label className="mt-2 flex items-center gap-3 text-sm text-[#2F4F75]">
            <input
              type="checkbox"
              {...register("drug_test_passed")}
              className="h-4 w-4 rounded border-[#2F4F75]"
            />
            Mark as passed
          </label>
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label htmlFor="drug_test_date" className={labelClassName}>
            Test Date
          </label>
          <input
            id="drug_test_date"
            type="date"
            {...register("drug_test_date")}
            className={inputClassName}
          />
          {errors.drug_test_date && (
            <p className={errorClassName}>{errors.drug_test_date.message}</p>
          )}
        </div>

        <div className="flex justify-between sm:col-span-2">
          <button
            type="button"
            onClick={() => navigate("/vendor/contractors/create/certification")}
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

export { DrugTestStep };
