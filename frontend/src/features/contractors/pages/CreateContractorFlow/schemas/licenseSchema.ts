import { z } from "zod";

const STATE_REGEX = /^[A-Z]{2}$/;

const isValidOptionalISODate = (value: string) =>
  value === "" || z.iso.date().safeParse(value).success;

export const licenseSchema = z
  .object({
    license_type: z.string().trim().min(1, "License type is required"),

    license_number: z.string().trim().min(1, "License number is required"),

    license_state: z
      .string()
      .trim()
      .refine((value) => STATE_REGEX.test(value), {
        message: "License state must be a valid 2-letter code",
      }),

    license_expiration_date: z.iso.date(
      "License expiration date must be YYYY-MM-DD",
    ),

    license_document_url: z.string().trim(),

    license_verified: z.boolean(),

    license_verified_by: z.string().trim(),

    license_verified_at: z.string().trim().refine(isValidOptionalISODate, {
      message: "Verification date must be a valid YYYY-MM-DD",
    }),
  })
  .superRefine((data, ctx) => {
    if (data.license_verified) {
      if (!data.license_verified_by) {
        ctx.addIssue({
          path: ["license_verified_by"],
          code: "custom",
          message: "Verified by is required when license is verified",
        });
      }

      if (!data.license_verified_at) {
        ctx.addIssue({
          path: ["license_verified_at"],
          code: "custom",
          message: "Verification date is required when license is verified",
        });
      } else if (
        z.iso.date().safeParse(data.license_verified_at).success &&
        new Date(`${data.license_verified_at}T00:00:00`) > new Date()
      ) {
        ctx.addIssue({
          path: ["license_verified_at"],
          code: "custom",
          message: "Verification date cannot be in the future",
        });
      }
    }
  });
