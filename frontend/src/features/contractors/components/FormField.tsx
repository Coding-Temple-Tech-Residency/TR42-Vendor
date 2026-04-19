type FormFieldProps = {
  label: string;
  children: React.ReactNode;
  className?: string;
};

export function FormField({ label, children, className = "" }: FormFieldProps) {
  return (
    <div className={`rounded-xl bg-[#C9D8E6] p-4 shadow-md ${className}`}>
      <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
        {label}
      </label>
      {children}
    </div>
  );
}
