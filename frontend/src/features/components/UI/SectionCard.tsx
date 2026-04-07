type SectionCardProps = {
    title?: string;
    subtitle?: string;
    children: React.ReactNode;
    action?: React.ReactNode;
    className?: string;
};

export default function SectionCard({
    title,
    subtitle,
    children,
    action,
    className = "",
}: SectionCardProps) {
    return(
        <section 
            className={`rounded-2xl border border-slate-200 bg-white p-5 shadow-sm ${className}`}
        >
            {(title || action) && (
                <div className="mb-4 flex items-start justify-between gap-4">
                    <div>
                        {title && (
                            <h2 className="text-lg font-semibold text-slate-900">{title}</h2>
                        )}
                        {subtitle && (
                            <h2 className="mt-1 text-sm text-slate-500">{subtitle}</h2>
                        )}
                    </div>
                    {action && <div>{action}</div>}
                </div>
            )}

            {children}
        </section>
    );
}