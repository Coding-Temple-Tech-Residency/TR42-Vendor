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

const CertificationStep = () => {
  const { next, back, isFirst } = useContractorStepNavigation();
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

    next();
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Certification</h3>
        <p className="text-sm text-[#4A6C8A]">Enter certification details.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={fieldWrapperClassName}>
          <label htmlFor="certification_name" className={labelClassName}>
            Certification Name
          </label>
          <input
            id="certification_name"
            {...register("certification_name")}
            className={inputClassName}
          />
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="certifying_body" className={labelClassName}>
            Certifying Body
          </label>
          <input
            id="certifying_body"
            {...register("certifying_body")}
            className={inputClassName}
          />
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="certification_number" className={labelClassName}>
            Certification Number
          </label>
          <input
            id="certification_number"
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
          <label htmlFor="issue_date" className={labelClassName}>
            Issue Date
          </label>
          <input
            id="issue_date"
            type="date"
            {...register("issue_date")}
            className={inputClassName}
          />
          {errors.issue_date && (
            <p className={errorClassName}>{errors.issue_date.message}</p>
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
          <label htmlFor="document_url" className={labelClassName}>
            Document URL
          </label>
          <input
            id="document_url"
            {...register("certification_document_url")}
            className={inputClassName}
          />
        </div>

        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label htmlFor="verified" className={labelClassName}>
            Verified
          </label>
          <input
            id="verified"
            type="checkbox"
            {...register("certification_verified")}
          />
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

export { CertificationStep };
