import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { Item } from "../../../src/order/components/Item";

describe("Item Component", () => {
  test("renders name, unit_price, and total correctly", () => {
    const name = "Cerveza";
    const unit_price = 10;
    const total = 30;

    render(<Item name={name} unit_price={unit_price} total={total} />);

    expect(screen.getByText(name)).toBeInTheDocument();
    expect(screen.getByText(unit_price)).toBeInTheDocument();
    expect(screen.getByText(total)).toBeInTheDocument();
  });
});
