import { z } from "zod";
import {
  getPasswordChecks,
  toBackendPhoneFormat,
} from "../../../../../utils/validation";

const PHONE_REGEX = /^\d{3}-\d{3}-\d{4}$/;
const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const SSN_LAST_FOUR_REGEX = /^\d{4}$/;
const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;

function isValidDateString(value: string) {
  if (!DATE_REGEX.test(value.trim())) return false;
  const parsed = new Date(`${value}T00:00:00`);
  return !Number.isNaN(parsed.getTime());
}

const basicInfoSchema = z
  .object({
    first_name: z
      .string()
      .trim()
      .min(2, "First name must be at least 2 characters long")
      .max(50, "First name must be 50 characters or less"),

    last_name: z
      .string()
      .trim()
      .min(2, "Last name must be at least 2 characters long")
      .max(50, "Last name must be 50 characters or less"),

    middle_name: z.string().trim(),

    date_of_birth: z
      .string()
      .trim()
      .min(1, "Date of birth is required")
      .refine((value) => DATE_REGEX.test(value), {
        message: "Date of birth must be in YYYY-MM-DD format.",
      })
      .refine((value) => isValidDateString(value), {
        message: "Enter a valid date of birth.",
      })
      .refine((value) => new Date(`${value}T00:00:00`) <= new Date(), {
        message: "Date of birth cannot be in the future.",
      }),

    ssn_last_four: z
      .string()
      .trim()
      .refine((value) => value === "" || /^\d{4}$/.test(value), {
        message: "SSN last four must be exactly 4 digits.",
      }),

    email: z
      .string()
      .trim()
      .min(1, "Email is required.")
      .refine((value) => EMAIL_REGEX.test(value), {
        message: "Invalid email address, must be in format: user@example.com",
      }),

    contact_number: z
      .string()
      .trim()
      .min(1, "Contact number is required.")
      .refine((value) => PHONE_REGEX.test(toBackendPhoneFormat(value)), {
        message: "Invalid phone number format (XXX-XXX-XXXX)",
      }),

    alternate_number: z
      .string()
      .trim()
      .refine(
        (value) => value === "" || /^\d{3}-\d{3}-\d{4}$/.test(value), // or your helper format
        {
          message: "Invalid phone number format (XXX-XXX-XXXX)",
        },
      ),

    username: z.string().trim().min(1, "Username is required."),

    password: z.string().min(1, "Password is required."),
  })
  .superRefine((form, ctx) => {
    const checks = getPasswordChecks(form.password, {
      username: form.username,
      firstName: form.first_name,
      lastName: form.last_name,
    });

    if (!Object.values(checks).every(Boolean)) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        path: ["password"],
        message:
          "Password must be at least 12 characters long and include uppercase, lowercase, number, and special character, and must not contain more than 2 identical characters in a row or contain your username, first name, or last name.",
      });
    }
  });

type BasicInfoFormValues = z.infer<typeof basicInfoSchema>;

export { basicInfoSchema, type BasicInfoFormValues };
