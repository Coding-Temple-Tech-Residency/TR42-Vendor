import { z } from "zod";

const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;
const STATE_REGEX = /^[A-Z]{2}$/;

export const licenseSchema = z.object({
  license_type: z.string().trim().min(1, "License type is required"),

  license_number: z.string().trim().min(1, "License number is required"),

  license_state: z
    .string()
    .trim()
    .refine((value) => STATE_REGEX.test(value), {
      message: "License state must be a valid 2-letter code",
    }),

  license_expiration_date: z
    .string()
    .trim()
    .refine((value) => DATE_REGEX.test(value), {
      message: "License expiration date must be YYYY-MM-DD",
    }),

  license_document_url: z.string().trim(),

  license_verified: z.boolean(),

  license_verified_by: z.string().trim(),

  license_verified_at: z.string().trim(),
});
