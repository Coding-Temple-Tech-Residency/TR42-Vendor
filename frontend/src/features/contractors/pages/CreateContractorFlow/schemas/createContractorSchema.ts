import { z } from "zod";
import { addressSchema } from "./addressSchema";
import { backgroundCheckSchema } from "./backgroundCheckSchema";
import { basicInfoSchema } from "./basicInfoSchema";
import { certificationSchema } from "./certificationSchema";
import { drugTestSchema } from "./drugTestSchema";
import { insuranceSchema } from "./insuranceSchema";
import { licenseSchema } from "./licenseSchema";

const createContractorSchema = basicInfoSchema
  .extend(addressSchema.shape)
  .extend(backgroundCheckSchema.shape)
  .extend(certificationSchema.shape)
  .extend(drugTestSchema.shape)
  .extend(insuranceSchema.shape)
  .extend(licenseSchema.shape);

type CreateContractorFormValues = z.infer<typeof createContractorSchema>;

export { createContractorSchema, type CreateContractorFormValues };
