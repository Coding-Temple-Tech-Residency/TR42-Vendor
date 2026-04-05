type EmptyStateProps = {
    title: string,
    description?: string,
    action?: string,
};

export default function EmptyStateProps({
    title,
    description,
    action,
}: EmptyStateProps) {
    return(
        <div className="flex flex-col items-center justify-center rounded-2xl border border-dashed border-[#E5E7EB] bg-[#FFFFFF] px-6 py-12 text-center">
            <div className="mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-[#F9FAFB] text-xl">
                 📄
            </div>

            <h3 className="text-lg font-semibold text-[#111827]">{title}</h3>

            {description && (
                <p className="mt-2 max-w-md text-sm text-[#6B7280]">{description}</p>
            )}

            {action && <div className="mt-5">{action}</div>}
        </div>
    );
}