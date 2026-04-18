import { z } from "zod";

const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;

export const drugTestSchema = z.object({
  drug_test_passed: z.boolean(),

  drug_test_date: z
    .string()
    .trim()
    .refine((value) => value === "" || DATE_REGEX.test(value), {
      message: "Date must be YYYY-MM-DD",
    }),
});
