interface BarData {
  label: string;
  value: number;
}

interface BarChartProps {
  data: BarData[];
  maxValue?: number;
}

export default function BarChart({ data, maxValue = 30 }: BarChartProps) {
  return (
    <div className="w-full h-full flex flex-col min-h-37.5">
      <div className="relative flex-1 flex items-end justify-between px-2 gap-4">
        {/* Y-Axis Grid Lines: 0, 10, 20, 30 scale as seen in screenshot */}
        <div className="absolute inset-0 flex flex-col justify-between pointer-events-none">
          {[maxValue, 20, 10, 0].map((tick) => (
            <div
              key={tick}
              className="w-full border-t border-slate-100 flex items-start h-0"
            >
              <span className="text-[10px] text-slate-400 pr-2 bg-white z-10">
                {tick}
              </span>
            </div>
          ))}
        </div>

        {/* Thick Gradient Bars */}
        {data.map((item, index) => {
          const heightPercent = Math.min((item.value / maxValue) * 100, 100);
          return (
            <div
              key={index}
              className="relative flex-1 flex flex-col items-center h-full justify-end"
            >
              <div
                style={{
                  height: `${heightPercent}%`,
                  background:
                    "linear-gradient(to top, #2F4F75 0%, #64748B 50%, #CBD5E1 100%)",
                }}
                className="w-full max-w-13 rounded-t-sm transition-all duration-500 hover:brightness-110 shadow-sm"
              />
            </div>
          );
        })}
      </div>

      <div className="flex justify-between px-2 mt-4 border-t border-slate-100 pt-2">
        {data.map((item, index) => (
          <div key={index} className="flex-1 text-center">
            <span className="text-[10px] text-slate-500 font-medium">
              {item.label}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
