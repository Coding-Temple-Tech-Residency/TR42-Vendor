import React from "react";

type ColorVariant =
  | "red"
  | "orange"
  | "gray"
  | "blue"
  | "green"
  | "purple"
  | "yellow";

type Badge =
  | {
      type: "text";
      value: string;
    }
  | {
      type: "trend";
      value: number | string;
      trendDirection: "up" | "down";
    };

type KpiCardProps = {
  title: string;
  value: string | number;
  subtitle?: string;
  colorVariant?: ColorVariant;
  badge?: Badge;
};

const colorStyles: Record<ColorVariant, string> = {
  red: "bg-red-50 text-red-700",
  orange: "bg-orange-50 text-orange-700",
  gray: "bg-gray-50 text-gray-700",
  blue: "bg-blue-50 text-blue-700",
  green: "bg-green-50 text-green-700",
  purple: "bg-purple-50 text-purple-700",
  yellow: "bg-yellow-50 text-yellow-700",
};

const badgeStyles: Record<ColorVariant, string> = {
  red: "bg-red-100 text-red-700",
  orange: "bg-orange-100 text-orange-700",
  gray: "bg-gray-200 text-gray-700",
  blue: "bg-blue-100 text-blue-700",
  green: "bg-green-100 text-green-700",
  purple: "bg-purple-100 text-purple-700",
  yellow: "bg-yellow-100 text-yellow-700",
};

const KpiCard: React.FC<KpiCardProps> = ({
  title,
  value,
  subtitle,
  colorVariant = "gray",
  badge,
}) => {
  return (
    <div
      className={`p-4 rounded-2xl shadow-sm border ${colorStyles[colorVariant]}`}
    >
      {/* Title */}
      <h3 className="text-sm font-medium opacity-80">{title}</h3>

      {/* Value */}
      <div className="text-2xl font-bold mt-1">{value}</div>

      {/* Subtitle */}
      {subtitle && <p className="text-xs mt-1 opacity-70">{subtitle}</p>}

      {/* Badge */}
      {badge && (
        <div
          className={`mt-3 inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium ${badgeStyles[colorVariant]}`}
        >
          {badge.type === "trend" ? (
            <>
              {badge.trendDirection === "up" ? "▲" : "▼"}
              <span>{badge.value}</span>
            </>
          ) : (
            <span>{badge.value}</span>
          )}
        </div>
      )}
    </div>
  );
};

export default KpiCard;
