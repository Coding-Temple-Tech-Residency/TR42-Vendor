import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

interface DonutChartProps {
  data: { name: string; value: number; color?: string }[];
  innerRadius?: number;
  outerRadius?: number;
}

function DonutChart({
  data,
  innerRadius = 60,
  outerRadius = 90,
}: DonutChartProps) {
  const defaultColors = [
    "#1E3A5F",
    "#3B82F6",
    "#10B981",
    "#F59E0B",
    "#EF4444",
  ];

  return (
    <div className="w-full h-full min-h-[220px] min-w-[220px] flex items-center justify-center">
      <ResponsiveContainer width="100%" height="100%" minWidth={220} minHeight={220}>
        <PieChart margin={{ top: 0, right: 0, bottom: 0, left: 0 }}>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            cx="50%"
            cy="50%"
            innerRadius={innerRadius}
            outerRadius={outerRadius}
            paddingAngle={2}
            stroke="none"
          >
            {data.map((entry, index) => (
              <Cell
                key={`slice-${index}`}
                fill={entry.color || defaultColors[index % defaultColors.length]}
              />
            ))}
          </Pie>

          <Tooltip
            contentStyle={{
              borderRadius: "6px",
              border: "1px solid #E2E8F0",
              fontSize: "0.85rem",
            }}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default DonutChart;