import { z } from "zod";

const isValidOptionalISODate = (value: string) =>
  value === "" || z.iso.date().safeParse(value).success;

export const drugTestSchema = z
  .object({
    drug_test_passed: z.boolean(),

    drug_test_date: z.string().trim().refine(isValidOptionalISODate, {
      message: "Date must be a valid YYYY-MM-DD",
    }),
  })
  .superRefine((data, ctx) => {
    if (!data.drug_test_passed) return;

    if (!data.drug_test_date) {
      ctx.addIssue({
        path: ["drug_test_date"],
        code: "custom",
        message: "Date is required if drug test passed",
      });
    }
  });
