import { render, screen, fireEvent } from "@testing-library/react";
import { Summary } from "../../../src/order/components/Summary";

describe("Summary Component", () => {
  test("renders summary details correctly", () => {
    const props = {
      subtotal: "100",
      discount: "10",
      taxes: "5",
      total: "95",
    };

    render(<Summary {...props} />);

    expect(screen.getByText("Subtotal")).toBeInTheDocument();
    expect(screen.getByText(props.subtotal)).toBeInTheDocument();
    expect(screen.getByText("Discount")).toBeInTheDocument();
    expect(screen.getByText(props.discount)).toBeInTheDocument();
    expect(screen.getByText("Taxes")).toBeInTheDocument();
    expect(screen.getByText(props.taxes)).toBeInTheDocument();
    expect(screen.getByText("Total")).toBeInTheDocument();
    expect(screen.getByText(props.total)).toBeInTheDocument();
  });

  test("shows toast message on button click", () => {
    render(<Summary subtotal="100" taxes="5" total="105" />);

    const button = screen.getByText("Pagar");
    fireEvent.click(button);

    expect(screen.getByText("Not implemented yet")).toBeInTheDocument();
  });
});
