type KpiCardProps = {
  label: string;
  value: string | number;
  sub?: string;
};

function KpiCard({ label, value, sub }: KpiCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
      <p className="text-sm text-slate-500">{label}</p>
      <h2 className="mt-2 text-2xl font-bold text-slate-900">{value}</h2>
      {sub && <p className="mt-1 text-sm text-slate-400">{sub}</p>}
    </div>
  );
}

export default KpiCard;