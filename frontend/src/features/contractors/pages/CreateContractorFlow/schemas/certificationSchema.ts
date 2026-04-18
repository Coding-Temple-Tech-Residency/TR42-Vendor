import { z } from "zod";

export const certificationSchema = z
  .object({
    certification_name: z.string().trim(),

    certifying_body: z.string().trim(),

    certification_number: z
      .string()
      .trim()
      .min(1, "Certification number is required"),

    issue_date: z.iso.date("Issue date must be YYYY-MM-DD"),

    expiration_date: z.iso.date("Expiration date must be YYYY-MM-DD"),

    certification_document_url: z.string().trim(),

    certification_verified: z.boolean(),
  })
  .superRefine((data, ctx) => {
    if (data.expiration_date < data.issue_date) {
      ctx.addIssue({
        path: ["expiration_date"],
        code: "custom",
        message: "Expiration date cannot be before issue date",
      });
    }
  });
