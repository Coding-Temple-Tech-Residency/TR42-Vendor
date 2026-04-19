import {
  LineChart as RechartsLineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

// TypeScript interface to match your team's standards
interface ChartDataPoint {
  day: string;
  new?: number;
  completed?: number;
  value?: number; // Supports the contractors-specific data key
}

interface LineChartProps {
  data: ChartDataPoint[];
}

function LineChart({ data }: LineChartProps) {
  // Determine if we are showing Dashboard data (new/completed) or Contractor data (value)
  const isContractorMode = data.length > 0 && "value" in data[0];

  return (
    <div className="w-full h-full">
      <div className="h-64 w-full flex flex-col justify-between">
        {/* Chart */}
        <ResponsiveContainer width="100%" height="85%">
          <RechartsLineChart
            data={data}
            margin={{ top: 10, right: 10, left: -20, bottom: 0 }}
          >
            <CartesianGrid
              strokeDasharray="3 3"
              vertical={false}
              stroke="#E5E7EB"
            />

            <XAxis
              dataKey="day"
              tickLine={false}
              axisLine={false}
              tick={{ fill: "#94A3B8", fontSize: 12 }}
              tickMargin={10}
            />

            <YAxis
              tickLine={false}
              axisLine={false}
              tick={{ fill: "#94A3B8", fontSize: 12 }}
            />

            <Tooltip
              contentStyle={{
                borderRadius: "8px",
                border: "1px solid #E5E7EB",
                boxShadow: "0 4px 6px -1px rgb(0 0 0 / 0.1)",
                fontSize: "0.85rem",
              }}
            />

            {isContractorMode ? (
              /* Contractor Page Style: Single Navy Blue Line */
              <Line
                type="monotone"
                dataKey="value"
                name="On-Time Rate"
                stroke="#2F4F75"
                strokeWidth={2}
                dot={{ r: 4, fill: "#FFF", stroke: "#2F4F75", strokeWidth: 2 }}
                activeDot={{ r: 6, strokeWidth: 0 }}
                isAnimationActive={true}
                animationDuration={1500}
              />
            ) : (
              /* Dashboard Style: Blue and Amber Lines */
              <>
                <Line
                  type="monotone"
                  dataKey="new"
                  name="New"
                  stroke="#3B71E3"
                  strokeWidth={2}
                  dot={{
                    r: 4,
                    fill: "#FFF",
                    stroke: "#3B71E3",
                    strokeWidth: 2,
                  }}
                  activeDot={{ r: 6, strokeWidth: 0 }}
                  isAnimationActive={true}
                  animationDuration={1500}
                />
                <Line
                  type="monotone"
                  dataKey="completed"
                  name="Completed"
                  stroke="#F59E0B"
                  strokeWidth={2}
                  dot={{
                    r: 4,
                    fill: "#FFF",
                    stroke: "#F59E0B",
                    strokeWidth: 2,
                  }}
                  activeDot={{ r: 6, strokeWidth: 0 }}
                  isAnimationActive={true}
                  animationDuration={1500}
                />
              </>
            )}
          </RechartsLineChart>
        </ResponsiveContainer>

        {/* Legend: Matches the Figma layout */}
        <div className="flex items-center justify-center gap-6 mt-4 text-[12px] font-medium text-slate-500">
          {isContractorMode ? (
            <div className="flex items-center gap-2">
              <span className="h-2 w-2 rounded-full bg-[#2F4F75]" />
              <span>On-Time Completion</span>
            </div>
          ) : (
            <>
              <div className="flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-[#3B71E3]" />
                <span>New</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-[#F59E0B]" />
                <span>Completed</span>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default LineChart;
