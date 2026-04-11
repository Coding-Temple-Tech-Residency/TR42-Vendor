function KpiCard({ label, value }: { label: string; value: number }) {
  return (
    <div className="flex-1 bg-white p-4 rounded-xl shadow-sm border">
      <p className="text-sm text-gray-500">{label}</p>
      <h2 className="text-2xl font-bold">{value}</h2>
    </div>
  );
}

export default KpiCard;