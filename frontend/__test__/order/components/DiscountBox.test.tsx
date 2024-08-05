import { render, screen, fireEvent } from "@testing-library/react";
import { DiscountBox } from "../../../src/order/components/DiscountBox";

describe("DiscountBox Component", () => {
  test("render component", () => {
    render(<DiscountBox />);
    expect(
      screen.getByPlaceholderText("ADD YOUR DISCOUNT CODE")
    ).toBeInTheDocument();
    expect(screen.getByText("APPLY")).toBeInTheDocument();
  });

  test("when add a value to input then value change", () => {
    render(<DiscountBox />);
    const input = screen.getByPlaceholderText("ADD YOUR DISCOUNT CODE");
    fireEvent.change(input, { target: { value: "FREEBEER" } });
    expect(input.value).toBe("FREEBEER");
  });

  test("when click on button, then toast appear", () => {
    render(<DiscountBox />);
    const button = screen.getByText("APPLY");
    fireEvent.click(button);
    expect(screen.getByText("Not Implement Yet")).toBeInTheDocument();
  });
});
