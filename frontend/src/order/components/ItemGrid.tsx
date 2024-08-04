import { Item } from "./Item";
import { Item as ItemProp } from "../../interfaces/Order";

interface GridProp {
  items: ItemProp[];
}

export const ItemGrid = ({ items }: GridProp) => {
  return (
    <div className="flex flex-col justify-start items-start dark:bg-gray-800 bg-gray-50 px-4 py-8 md:py-6 md:p-6 xl:p-8 w-full">
      <p className="text-lg md:text-xl dark:text-white font-semibold leading-6 xl:leading-5 text-gray-800">
        Items
      </p>
      {items && items.map((object, i) => <Item key={i} {...object} />)}
    </div>
  );
};
