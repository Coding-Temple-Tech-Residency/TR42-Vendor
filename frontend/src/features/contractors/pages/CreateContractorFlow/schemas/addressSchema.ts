import { z } from "zod";

const ADDRESS_REGEX = /^[A-Za-z0-9\s.'#,-]{5,120}$/;
const ZIP_REGEX = /^\d{5}(-\d{4})?$/;
const STATE_REGEX = /^[A-Z]{2}$/;
const CITY_REGEX = /^[A-Za-z\s.'-]{2,50}$/;

export const addressSchema = z.object({
  address: z.object({
    street: z
      .string()
      .trim()
      .min(1, "Street is required")
      .regex(
        ADDRESS_REGEX,
        "Enter a valid street address (e.g., '123 Main St')",
      ),

    city: z
      .string()
      .trim()
      .min(1, "City is required")
      .regex(CITY_REGEX, "Enter a valid city."),

    state: z
      .string()
      .trim()
      .min(1, "State is required")
      .regex(STATE_REGEX, "Enter a valid 2-letter state code."),

    zip: z
      .string()
      .trim()
      .min(1, "zip is required")
      .regex(ZIP_REGEX, "Enter a valid ZIP code."),
  }),
});
