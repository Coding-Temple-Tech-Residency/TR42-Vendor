const ChartPlaceholder = ({ title }: { title?: string }) => {
  return (
    <div className="bg-white p-4 rounded-2xl shadow-sm border h-56 flex flex-col justify-center items-center">
      {title && <p className="text-sm text-gray-500 mb-2">{title}</p>}
      <p className="text-gray-400">Chart coming soon</p>
    </div>
  );
};

export default ChartPlaceholder;
