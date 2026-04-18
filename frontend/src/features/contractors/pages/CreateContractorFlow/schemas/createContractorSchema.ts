import { z } from "zod";
import { addressSchema } from "./addressSchema";
import { backgroundCheckSchema } from "./backgroundCheckSchema";
import { basicInfoSchema } from "./basicInfoSchema";
import { certificationSchema } from "./certificationSchema";
import { drugTestSchema } from "./drugTestSchema";
import { insuranceSchema } from "./insuranceSchema";
import { licenseSchema } from "./licenseSchema";

const createContractorSchema = basicInfoSchema
  .and(addressSchema)
  .and(backgroundCheckSchema)
  .and(certificationSchema)
  .and(drugTestSchema)
  .and(insuranceSchema)
  .and(licenseSchema);

type CreateContractorFormValues = z.infer<typeof createContractorSchema>;

export { createContractorSchema, type CreateContractorFormValues };
