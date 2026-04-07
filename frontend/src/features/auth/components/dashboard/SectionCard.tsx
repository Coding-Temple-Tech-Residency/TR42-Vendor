function SectionCard({ title, children }: any) {
  return (
    <div className="bg-white p-5 rounded-xl shadow-sm border">
      <h2 className="font-semibold mb-3">{title}</h2>
      {children}
    </div>
  );
}

export default SectionCard;