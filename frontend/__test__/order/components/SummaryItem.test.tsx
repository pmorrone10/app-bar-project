import { render, screen } from "@testing-library/react";
import { SummaryItem } from "../../../src/order/components/SummaryItem";

describe("SummaryItem Component", () => {
  test("renders label and value correctly", () => {
    const props = {
      label: "Subtotal",
      value: "100",
    };

    render(<SummaryItem {...props} />);

    expect(screen.getByText(props.label)).toBeInTheDocument();
    expect(screen.getByText(props.value)).toBeInTheDocument();
  });

  test("renders with semi-bold font when isSemiBold is true", () => {
    const props = {
      label: "Total",
      value: "100",
      isSemiBold: true,
    };

    render(<SummaryItem {...props} />);

    const labelElement = screen.getByText(props.label);
    const valueElement = screen.getByText(props.value);

    expect(labelElement).toHaveClass("font-semibold");
    expect(valueElement).toHaveClass("font-semibold");
  });
});
