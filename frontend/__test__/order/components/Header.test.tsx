import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { Header } from "../../../src/order/components/Header";

describe("Header Component", () => {
  test("renders orderId and date correctly", () => {
    const orderId = "12345";
    const date = "2023-08-01";

    render(<Header orderId={orderId} date={date} />);

    expect(screen.getByText(`Order #${orderId}`)).toBeInTheDocument();
    expect(screen.getByText(date)).toBeInTheDocument();
  });
});
