import { useLocation, useNavigate } from "react-router-dom";
import { contractorCreateSteps } from "../schemas/stepConfig";

const useContractorStepNavigation = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const currentIndex = contractorCreateSteps.findIndex(
    (step) => step.path === location.pathname,
  );

  const next = () => {
    if (currentIndex < contractorCreateSteps.length - 1) {
      navigate(contractorCreateSteps[currentIndex + 1].path);
    }
  };

  const back = () => {
    if (currentIndex > 0) {
      navigate(contractorCreateSteps[currentIndex - 1].path);
    }
  };

  return {
    currentIndex,
    currentStep: contractorCreateSteps[currentIndex],
    next,
    back,
    isFirst: currentIndex === 0,
    isLast: currentIndex === contractorCreateSteps.length - 1,
  };
};

export { useContractorStepNavigation };
