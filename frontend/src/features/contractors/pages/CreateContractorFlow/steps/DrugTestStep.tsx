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

const DrugTestStep = () => {
  const { next, back, isFirst } = useContractorStepNavigation();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger(["drug_test_passed", "drug_test_date"]);

    if (!isValid) return;

    next();
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

        <ContractorStepNavigation
          onNext={handleNext}
          onBack={back}
          isFirst={isFirst}
        />
      </div>
    </section>
  );
};

export { DrugTestStep };
