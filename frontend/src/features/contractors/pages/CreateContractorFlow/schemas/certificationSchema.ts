import { z } from "zod";

const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;

export const certificationSchema = z
  .object({
    certification_name: z.string().trim(),

    certifying_body: z.string().trim(),

    certification_number: z
      .string()
      .trim()
      .min(1, "Certification number is required"),

    issue_date: z.iso.date("Issue date must be YYYY-MM-DD"),

    expiration_date: z
      .string()
      .trim()
      .refine((value) => value === "" || DATE_REGEX.test(value), {
        message: "Expiration date must be YYYY-MM-DD",
      }),

    certification_document_url: z.string().trim(),

    certification_verified: z.boolean(),
  })
  .superRefine((data, ctx) => {
    if (data.expiration_date !== "" && data.expiration_date < data.issue_date) {
      ctx.addIssue({
        path: ["expiration_date"],
        code: "custom",
        message: "Expiration date cannot be before issue date",
      });
    }
  });
