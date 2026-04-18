import { useState } from "react";
import { useFormContext } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import type { BasicInfoFormValues } from "../schemas/basicInfoSchema";

const fieldWrapperClassName = "rounded-xl bg-[#C9D8E6] p-4 shadow-md";
const labelClassName =
  "text-xs font-medium uppercase tracking-wide text-[#2F4F75]";
const inputBaseClassName =
  "mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]";
const errorClassName = "mt-2 text-xs text-red-600";

const BasicInfoStep = () => {
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useFormContext<BasicInfoFormValues>();

  const onSubmit = (data: BasicInfoFormValues) => {
    console.log("basic info valid", data);
    navigate("/vendor/contractors/create/address");
  };

  return (
    <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div className="mb-4">
          <h3 className="text-lg text-[#2F4F75]">Create Contractor</h3>
          <p className="text-sm text-[#4A6C8A]">
            Enter contractor information.
          </p>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          <div className={fieldWrapperClassName}>
            <label htmlFor="first_name" className={labelClassName}>
              First Name
            </label>
            <input
              id="first_name"
              {...register("first_name")}
              className={inputBaseClassName}
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
              className={inputBaseClassName}
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
              className={inputBaseClassName}
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
              className={inputBaseClassName}
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
              className={inputBaseClassName}
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
              className={inputBaseClassName}
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
              className={inputBaseClassName}
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
              className={inputBaseClassName}
            />
            {errors.alternate_number && (
              <p className={errorClassName}>
                {errors.alternate_number.message}
              </p>
            )}
          </div>

          <div className={fieldWrapperClassName}>
            <label htmlFor="username" className={labelClassName}>
              Username
            </label>
            <input
              id="username"
              {...register("username")}
              className={inputBaseClassName}
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
                className="w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 pr-16 text-sm text-[#2F4F75] outline-none focus:border-[#2F3B4A] focus:ring-2 focus:ring-[#2F3B4A]"
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

          <div className="flex justify-end sm:col-span-2">
            <button
              type="submit"
              className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white transition hover:bg-[#4A6C8A]"
            >
              Next
            </button>
          </div>
        </div>
      </form>
    </section>
  );
};

export { BasicInfoStep };
