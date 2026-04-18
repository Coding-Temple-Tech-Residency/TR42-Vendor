import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { CreateContractorFormValues } from "../schemas/createContractorSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const AddressStep = () => {
  const navigate = useNavigate();
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

    console.log("step 2 valid");

    navigate("/vendor/contractors/create/background-check");
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
          />
          {errors.address?.zip && (
            <p className={errorClassName}>{errors.address.zip.message}</p>
          )}
        </div>

        <div className="flex justify-between sm:col-span-2">
          <button
            type="button"
            onClick={() => navigate("/vendor/contractors/create")}
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

export { AddressStep };
