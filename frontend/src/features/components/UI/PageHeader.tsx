type PageHeaderProps = {
    title: string;
    description?: string;
    action?: string;
};

export default function PageHeader({
    title,
    description,
    action,
}: PageHeaderProps) {
    return(
        <div className="mb-6 flex flex-col gap-4 border-b border-[#1F2A44] pb-4" sm:flex-row sm:items-center sm:justify-between>
            <div>
                <h1 className="text-2xl font-semibold text-slate-900">{title}</h1>
                {description && (
                    <p className="mt-1 text-sm text-slate-500">{description}</p>
                )}
            </div>

            {action && <div className="shrink-0">{action}</div>}
        </div>
    );
}