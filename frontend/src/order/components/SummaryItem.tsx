interface SummaryItemProps {
  label: string;
  value: string;
  isSemiBold?: boolean;
}

export const SummaryItem: React.FC<SummaryItemProps> = ({
  label,
  value,
  isSemiBold,
}) => {
  return (
    <div className="flex justify-between w-full">
      <p
        className={`text-base dark:text-white leading-4 text-gray-800 ${
          isSemiBold && "font-semibold"
        }`}
      >
        {label}
      </p>
      <p
        className={`text-base dark:text-white leading-4 text-gray-800 ${
          isSemiBold && "font-semibold"
        }`}
      >
        {value}
      </p>
    </div>
  );
};
