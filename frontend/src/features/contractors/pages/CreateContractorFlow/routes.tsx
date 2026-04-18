import { Route } from "react-router-dom";
import { CreateContractorFlow } from "./CreateContractorFlow";
import { ContractorBasicInfoStep } from "./steps/BasicInfoStep";

const contractorCreateRoutes = (
  <Route path="/contractors/create" element={<CreateContractorFlow />}>
    <Route index element={<ContractorBasicInfoStep />} />
  </Route>
);

export { contractorCreateRoutes };
