import { render, screen } from "@testing-library/react";
import { Toast } from "../../../src/order/components/Toast";

describe("Toast Component", () => {
  test("renders message correctly", () => {
    const message = "Not implemented yet";

    render(<Toast message={message} />);

    expect(screen.getByText(message)).toBeInTheDocument();
  });
});
