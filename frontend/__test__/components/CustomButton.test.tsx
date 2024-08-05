import { render, fireEvent, screen } from "@testing-library/react";
import { CustomButton } from "../../src/components/CustomButton";

describe("CustomButton Component", () => {
  test("renders CustomButton component with text", () => {
    render(<CustomButton text="PAY" handleClick={() => {}} />);
    expect(screen.getByText("PAY")).toBeInTheDocument();
  });

  test("when button is clicked then calls handleClick", () => {
    const handleClick = jest.fn();
    render(<CustomButton text="PAY" handleClick={handleClick} />);
    fireEvent.click(screen.getByText("PAY"));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
