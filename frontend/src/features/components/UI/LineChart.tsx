import {
  LineChart as RechartsLineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

function LineChart({ data }) {
  return (
    <div className="w-full flex justify-center">
    
      <div className="bg-white rounded-xl shadow-sm p-5 w-full">
        
        <div className="h-64 w-full flex flex-col justify-between">
          
          {/* Chart */}
          <ResponsiveContainer width="100%" height="80%">
            <RechartsLineChart
              data={data}
              margin={{ top: 10, right: 20, left: -10, bottom: 0 }}
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
                tick={{ fill: "#6B7280", fontSize: 12 }}
                tickMargin={15}
              />

              <YAxis
                tickLine={false}
                axisLine={false}
                tick={{ fill: "#6B7280", fontSize: 12 }}
              />

              <Tooltip
                contentStyle={{
                  borderRadius: "8px",
                  border: "1px solid #E5E7EB",
                  fontSize: "0.85rem",
                }}
              />

              {/* NEW line */}
              <Line
                type="monotone"
                dataKey="new"
                stroke="#2563EB"
                strokeWidth={3}
                dot={{ r: 4 }}
                activeDot={{ r: 6 }}
              />

              {/* COMPLETED line */}
              <Line
                type="monotone"
                dataKey="completed"
                stroke="#F59E0B"
                strokeWidth={3}
                dot={{ r: 4 }}
                activeDot={{ r: 6 }}
              />
            </RechartsLineChart>
          </ResponsiveContainer>

          {/* Legend */}
          <div className="flex items-center justify-center gap-6 mt-6 text-sm text-gray-600">
            <div className="flex items-center gap-2">
              <span className="h-2 w-2 rounded-full bg-blue-600" />
              <span>New</span>
            </div>

            <div className="flex items-center gap-2">
              <span className="h-2 w-2 rounded-full bg-amber-500" />
              <span>Completed</span>
            </div>
          </div>

        </div>

      </div>
    </div>
  );
}

export default LineChart;