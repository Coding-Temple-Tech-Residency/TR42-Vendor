import { z } from "zod";

const isValidISODate = (value: string) => {
  if (value === "") return true;

  const parsed = z.iso.date().safeParse(value);
  if (!parsed.success) return false;

  const date = new Date(`${value}T00:00:00`);
  return !isNaN(date.getTime());
};

export const backgroundCheckSchema = z
  .object({
    background_check_passed: z.boolean(),

    background_check_date: z.string().trim().refine(isValidISODate, {
      message: "Date must be a valid YYYY-MM-DD",
    }),

    background_check_provider: z.string().trim(),
  })
  .superRefine((data, ctx) => {
    if (!data.background_check_passed) return;

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
