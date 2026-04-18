import z from "zod";

const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;

export const backgroundCheckSchema = z
  .object({
    background_check_passed: z.boolean(),

    background_check_date: z
      .string()
      .trim()
      .refine((value) => value === "" || DATE_REGEX.test(value), {
        message: "Date must be YYYY-MM-DD",
      }),

    background_check_provider: z.string().trim(),
  })
  .superRefine((data, ctx) => {
    const isPassed = data.background_check_passed;

    if (!isPassed) return;

    if (!data.background_check_provider) {
      ctx.addIssue({
        path: ["background_check_provider"],
        code: "custom",
        message: "Provider is required if background check passed",
      });
    }

    if (!data.background_check_date) {
      ctx.addIssue({
        path: ["background_check_date"],
        code: "custom",
        message: "Date is required if background check passed",
      });
    }
  });
