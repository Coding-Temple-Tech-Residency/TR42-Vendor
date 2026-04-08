import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
} from "recharts";

interface FraudGaugeProps {
  value: number;
}

function FraudGauge({ value }: FraudGaugeProps) {
  const safeValue = Math.max(0, Math.min(100, value));
  const angle = (safeValue / 100) * 180;

  const data = [
    { value: 33, color: "#10B981" },
    { value: 33, color: "#F59E0B" },
    { value: 34, color: "#EF4444" },
  ];

  const getRiskColor = () => {
    if (safeValue < 33) return "#10B981";
    if (safeValue < 66) return "#F59E0B";
    return "#EF4444";
  };

  return (
    <div className="w-full flex justify-center">
      
      <div className="bg-white rounded-xl shadow-sm p-6 w-full max-w-md flex flex-col items-center">
        
        <div className="relative w-full h-52">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={data}
                startAngle={180}
                endAngle={0}
                innerRadius={80}
                outerRadius={100}
                dataKey="value"
                stroke="none"
              >
                {data.map((entry, index) => (
                  <Cell key={index} fill={entry.color} />
                ))}
              </Pie>
            </PieChart>
          </ResponsiveContainer>

          {/* Needle */}
          <div
            className="absolute left-1/2 bottom-2 origin-bottom"
            style={{
              width: "3px",
              height: "80px",
              backgroundColor: "#1E3A5F",
              transform: `translateX(-50%) rotate(${angle - 90}deg)`,
              transition: "transform 0.4s ease",
            }}
          />

          {/* Needle base */}
          <div className="absolute left-1/2 bottom-2 w-4 h-4 bg-gray-800 rounded-full transform -translate-x-1/2 translate-y-1/2" />

          {/* Center text */}
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-xs text-gray-500">Risk Score</span>
            <span className="text-2xl font-bold text-gray-900">
              {safeValue}%
            </span>
          </div>
        </div>

        {/* Label */}
        <p
          className="mt-4 text-sm font-semibold"
          style={{ color: getRiskColor() }}
        >
          Fraud Risk: {safeValue}%
        </p>

      </div>
    </div>
  );
}

export default FraudGauge;