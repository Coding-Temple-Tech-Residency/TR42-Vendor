import { z } from "zod";

const MONEY_REGEX = /^\d+(\.\d{1,2})?$/;
const PHONE_REGEX = /^\d{3}-\d{3}-\d{4}$/;

export const insuranceSchema = z
  .object({
    insurance_type: z.string().trim().min(1, "Insurance type is required"),

    policy_number: z.string().trim().min(1, "Policy number is required"),

    provider_name: z.string().trim().min(1, "Provider name is required"),

    provider_phone: z
      .string()
      .trim()
      .min(1, "Provider phone is required")
      .refine((value) => PHONE_REGEX.test(value), {
        message: "Phone must be in XXX-XXX-XXXX format",
      }),

    coverage_amount: z
      .string()
      .trim()
      .refine((value) => value === "" || MONEY_REGEX.test(value), {
        message: "Coverage amount must be a valid number with up to 2 decimals",
      }),

    deductible: z
      .string()
      .trim()
      .refine((value) => value === "" || MONEY_REGEX.test(value), {
        message: "Deductible must be a valid number with up to 2 decimals",
      }),

    effective_date: z.iso.date("Effective date must be YYYY-MM-DD"),

    expiration_date: z.iso.date("Expiration date must be YYYY-MM-DD"),

    insurance_document_url: z.string().trim(),

    insurance_verified: z.boolean(),

    additional_insurance_required: z.boolean(),

    additional_insured_certificate_url: z.string().trim(),
  })
  .superRefine((data, ctx) => {
    if (data.expiration_date < data.effective_date) {
      ctx.addIssue({
        path: ["expiration_date"],
        code: "custom",
        message: "Expiration date cannot be before effective date",
      });
    }

    if (
      data.additional_insurance_required &&
      !data.additional_insured_certificate_url
    ) {
      ctx.addIssue({
        path: ["additional_insured_certificate_url"],
        code: "custom",
        message:
          "Additional insured certificate URL is required when additional insurance is required",
      });
    }
  });
