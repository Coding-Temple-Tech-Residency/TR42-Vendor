type ContractorStepNavigationProps = {
  onNext: () => void | Promise<void>;
  onBack?: () => void;
  isFirst?: boolean;
  nextLabel?: string;
};

const ContractorStepNavigation = ({
  onNext,
  onBack,
  isFirst = false,
  nextLabel = "Next",
}: ContractorStepNavigationProps) => {
  return (
    <div className="flex justify-between sm:col-span-2">
      <div>
        {!isFirst ? (
          <button
            type="button"
            onClick={onBack}
            className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm font-medium text-[#2F4F75]"
          >
            Back
          </button>
        ) : (
          <div />
        )}
      </div>

      <button
        type="button"
        onClick={onNext}
        className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white transition hover:bg-[#4A6C8A]"
      >
        {nextLabel}
      </button>
    </div>
  );
};

export { ContractorStepNavigation };
