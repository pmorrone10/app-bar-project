import { Item as ItemProp } from "../../interfaces/Order";
export const Item = ({ name, unit_price, total }: ItemProp) => {
  return (
    <div className="mt-4 md:mt-6 flex flex-col md:flex-row justify-start items-start md:items-center md:space-x-6 xl:space-x-8 w-full space-y-4">
      <div className="border-b border-gray-200 md:flex-row flex-col flex justify-between items-start w-full pb-8 space-y-4 md:space-y-0">
        <div className="w-full flex flex-col justify-start items-start space-y-8">
          <h3 className="text-xl dark:text-white xl:text-2xl font-semibold leading-6 text-gray-800">
            {name}
          </h3>
        </div>
        <div className="flex justify-between space-x-8 items-start w-full">
          <p className="text-base dark:text-white xl:text-lg leading-6">
            {unit_price}
          </p>
          <p className="text-base dark:text-white xl:text-lg font-semibold leading-6 text-gray-800">
            {total}
          </p>
        </div>
      </div>
    </div>
  );
};
