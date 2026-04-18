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

const AddressStep = () => {
  const { next, back, isFirst } = useContractorStepNavigation();

  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger([
      "address.street",
      "address.city",
      "address.state",
      "address.zip",
    ]);

    if (!isValid) return;

    next();
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Contractor Address</h3>
        <p className="text-sm text-[#4A6C8A]">Enter the contractor address.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={`${fieldWrapperClassName} sm:col-span-2`}>
          <label htmlFor="address.street" className={labelClassName}>
            Street
          </label>
          <input
            id="address.street"
            {...register("address.street")}
            className={inputClassName}
          />
          {errors.address?.street && (
            <p className={errorClassName}>{errors.address.street.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="address.city" className={labelClassName}>
            City
          </label>
          <input
            id="address.city"
            {...register("address.city")}
            className={inputClassName}
          />
          {errors.address?.city && (
            <p className={errorClassName}>{errors.address.city.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="address.state" className={labelClassName}>
            State
          </label>
          <input
            id="address.state"
            {...register("address.state")}
            className={inputClassName}
            placeholder="TX"
            maxLength={2}
          />
          {errors.address?.state && (
            <p className={errorClassName}>{errors.address.state.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="address.zip" className={labelClassName}>
            ZIP
          </label>
          <input
            id="address.zip"
            {...register("address.zip")}
            className={inputClassName}
            placeholder="12345"
          />
          {errors.address?.zip && (
            <p className={errorClassName}>{errors.address.zip.message}</p>
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

export { AddressStep };
