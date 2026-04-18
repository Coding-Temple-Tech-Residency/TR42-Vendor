import { useState } from "react";
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

const BasicInfoStep = () => {
  const [showPassword, setShowPassword] = useState(false);
  const { next, back, isFirst } = useContractorStepNavigation();
  const {
    register,
    trigger,
    formState: { errors },
  } = useFormContext<CreateContractorFormValues>();

  const handleNext = async () => {
    const isValid = await trigger([
      "first_name",
      "middle_name",
      "last_name",
      "date_of_birth",
      "ssn_last_four",
      "email",
      "contact_number",
      "alternate_number",
      "username",
      "password",
    ]);

    if (!isValid) return;

    next();
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <div className="mb-4">
        <h3 className="text-lg text-[#2F4F75]">Create Contractor</h3>
        <p className="text-sm text-[#4A6C8A]">Enter contractor information.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className={fieldWrapperClassName}>
          <label htmlFor="first_name" className={labelClassName}>
            First Name
          </label>
          <input
            id="first_name"
            {...register("first_name")}
            className={inputClassName}
          />
          {errors.first_name && (
            <p className={errorClassName}>{errors.first_name.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="middle_name" className={labelClassName}>
            Middle Name
          </label>
          <input
            id="middle_name"
            {...register("middle_name")}
            className={inputClassName}
          />
          {errors.middle_name && (
            <p className={errorClassName}>{errors.middle_name.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="last_name" className={labelClassName}>
            Last Name
          </label>
          <input
            id="last_name"
            {...register("last_name")}
            className={inputClassName}
          />
          {errors.last_name && (
            <p className={errorClassName}>{errors.last_name.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="date_of_birth" className={labelClassName}>
            DOB
          </label>
          <input
            id="date_of_birth"
            type="date"
            {...register("date_of_birth")}
            className={inputClassName}
          />
          {errors.date_of_birth && (
            <p className={errorClassName}>{errors.date_of_birth.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="ssn_last_four" className={labelClassName}>
            Last 4 SSN
          </label>
          <input
            id="ssn_last_four"
            maxLength={4}
            {...register("ssn_last_four")}
            className={inputClassName}
          />
          {errors.ssn_last_four && (
            <p className={errorClassName}>{errors.ssn_last_four.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="email" className={labelClassName}>
            Email
          </label>
          <input
            id="email"
            type="email"
            {...register("email")}
            className={inputClassName}
          />
          {errors.email && (
            <p className={errorClassName}>{errors.email.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="contact_number" className={labelClassName}>
            Phone Number
          </label>
          <input
            id="contact_number"
            {...register("contact_number")}
            className={inputClassName}
          />
          {errors.contact_number && (
            <p className={errorClassName}>{errors.contact_number.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="alternate_number" className={labelClassName}>
            Alternate Number
          </label>
          <input
            id="alternate_number"
            {...register("alternate_number")}
            className={inputClassName}
          />
          {errors.alternate_number && (
            <p className={errorClassName}>{errors.alternate_number.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="username" className={labelClassName}>
            Username
          </label>
          <input
            id="username"
            {...register("username")}
            className={inputClassName}
          />
          {errors.username && (
            <p className={errorClassName}>{errors.username.message}</p>
          )}
        </div>

        <div className={fieldWrapperClassName}>
          <label htmlFor="password" className={labelClassName}>
            Password
          </label>

          <div className="mt-2 relative">
            <input
              id="password"
              type={showPassword ? "text" : "password"}
              {...register("password")}
              placeholder="Enter password"
              className={`${inputClassName} pr-16`}
            />

            <button
              type="button"
              onClick={() => setShowPassword((prev) => !prev)}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-sm font-medium text-[#2F4F75]"
            >
              {showPassword ? "Hide" : "Show"}
            </button>
          </div>

          {errors.password && (
            <p className={errorClassName}>{errors.password.message}</p>
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

export { BasicInfoStep };
