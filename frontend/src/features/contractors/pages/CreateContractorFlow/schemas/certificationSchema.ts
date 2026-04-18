import { z } from "zod";

const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;

export const certificationSchema = z.object({
  certification_name: z.string().trim(),

  certifying_body: z.string().trim(),

  certification_number: z
    .string()
    .trim()
    .min(1, "Certification number is required"),

  issue_date: z
    .string()
    .trim()
    .refine((value) => DATE_REGEX.test(value), {
      message: "Issue date must be YYYY-MM-DD",
    }),

  expiration_date: z
    .string()
    .trim()
    .refine((value) => value === "" || DATE_REGEX.test(value), {
      message: "Expiration date must be YYYY-MM-DD",
    }),

  certification_document_url: z.string().trim(),

  certification_verified: z.boolean(),
});
