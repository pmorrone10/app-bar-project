interface HeaderProp {
  orderId: string;
  date: string;
}

export const Header: React.FC<HeaderProp> = ({ orderId, date }) => {
  return (
    <div className="flex justify-start item-start space-y-2 flex-col">
      <h1 className="text-3xl dark:text-white lg:text-4xl font-semibold leading-7 lg:leading-9 text-gray-800">
        Order #{orderId}
      </h1>
      <p className="text-base dark:text-gray-300 font-medium leading-6 text-gray-600">
        {date}
      </p>
    </div>
  );
};
