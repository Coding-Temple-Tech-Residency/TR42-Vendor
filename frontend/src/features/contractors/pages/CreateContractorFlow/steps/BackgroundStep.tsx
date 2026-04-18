import { useFormContext } from "react-hook-form";
import { ContractorStepNavigation } from "../components/ContractorStepNavigation";
import { useContractorStepNavigation } from "../hooks/useContractorStepNavigation";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";
import {
  errorClassName,
  fieldWrapperClassName,
  inputClassName,
  labelClassName,
} from "./stepClassNames";

const BackgroundStep = () => {
  const { next, back, isFirst } = useContractorStepNavigation();
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

    next();
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

        <ContractorStepNavigation
          onNext={handleNext}
          onBack={back}
          isFirst={isFirst}
        />
      </div>
    </section>
  );
};

export { BackgroundStep };
