import React from "react";

type SectionCardProps = {
  // CHANGE: Changed from string to React.ReactNode to allow JSX
  title?: React.ReactNode;
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
  return (
    <section
      className={`rounded-2xl border border-slate-200 bg-white p-5 shadow-sm ${className}`}
    >
      {(title || action) && (
        <div className="mb-4 flex items-start justify-between gap-4">
          <div>
            {title && (
              // Use a <div> or <span> instead of <h2> if you pass
              // complex JSX to avoid invalid HTML nesting
              <div className="text-lg font-semibold text-slate-900">
                {title}
              </div>
            )}
            {subtitle && (
              <p className="mt-1 text-sm text-slate-500">{subtitle}</p>
            )}
          </div>
          {action && <div>{action}</div>}
        </div>
      )}

      {children}
    </section>
  );
}
