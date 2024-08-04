import { render, screen } from "@testing-library/react";
import { ItemGrid } from "../../../src/order/components/ItemGrid";
import { Item as ItemProp } from "../../../src/interfaces/Order";

const mockItems: ItemProp[] = [
  { name: "Item 1", unit_price: 10, total: 20 },
  { name: "Item 2", unit_price: 15, total: 30 },
];

describe("ItemGrid Component", () => {
  test("renders items correctly", () => {
    render(<ItemGrid items={mockItems} />);

    expect(screen.getByText("Items")).toBeInTheDocument();
    mockItems.forEach((item) => {
      expect(screen.getByText(item.name)).toBeInTheDocument();
      expect(screen.getByText(item.unit_price)).toBeInTheDocument();
      expect(screen.getByText(item.total)).toBeInTheDocument();
    });
  });
});
