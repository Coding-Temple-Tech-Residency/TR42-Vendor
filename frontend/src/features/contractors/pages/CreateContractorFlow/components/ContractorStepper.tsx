import { useLocation, useNavigate } from "react-router-dom";
import { contractorCreateSteps } from "../schemas/stepConfig";

const ContractorStepper = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const currentStepIndex = contractorCreateSteps.findIndex(
    (step) => step.path === location.pathname,
  );

  const progress =
    currentStepIndex >= 0
      ? ((currentStepIndex + 1) / contractorCreateSteps.length) * 100
      : 0;

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-[#2F4F75]">
            Step {currentStepIndex + 1} of {contractorCreateSteps.length}
          </p>
          <h2 className="text-lg font-semibold text-[#2F4F75]">
            {contractorCreateSteps[currentStepIndex]?.label ??
              "Create Contractor"}
          </h2>
        </div>
      </div>

      <div className="h-3 w-full overflow-hidden rounded-full bg-[#C9D8E6]">
        <div
          className="h-full rounded-full bg-[#2F4F75] transition-all duration-300"
          style={{ width: `${progress}%` }}
        />
      </div>

      <div className="flex flex-wrap gap-2">
        {contractorCreateSteps.map((step, index) => {
          const isActive = index === currentStepIndex;
          const isComplete = index < currentStepIndex;

          return (
            <button
              key={step.path}
              type="button"
              onClick={() => navigate(step.path)}
              className={`rounded-lg px-3 py-2 text-sm font-medium transition ${
                isActive
                  ? "bg-[#2F4F75] text-white"
                  : isComplete
                    ? "bg-[#4A6C8A] text-white"
                    : "bg-[#C9D8E6] text-[#2F4F75] hover:bg-[#B7CADC]"
              }`}
            >
              {index + 1}. {step.label}
            </button>
          );
        })}
      </div>
    </div>
  );
};

export { ContractorStepper };
