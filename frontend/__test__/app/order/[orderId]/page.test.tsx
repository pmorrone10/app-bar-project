import { render, screen, waitFor } from "@testing-library/react";
import fetchMock from "jest-fetch-mock";
import OrderPage from "../../../../src/app/order/[orderId]/page";
import { getOrder } from "../../../../src/order/actions/OrderAction";

jest.mock("../../../../src/order/actions/OrderAction");

describe("OrderPage", () => {
  beforeEach(() => {
    fetchMock.resetMocks();
  });

  test("displays order not found message when data is not returned", async () => {
    (getOrder as jest.Mock).mockReturnValue(null);

    render(await OrderPage({ params: { orderId: "DN" } }));

    await waitFor(() => {
      expect(screen.getByText("Order not found")).toBeInTheDocument();
    });
  });

  test("displays order details when data is returned", async () => {
    const mockOrder = {
      id: "1",
      created: "2023-01-01",
      items: [
        { name: "Item 1", unit_price: 10, total: 10 },
        { name: "Item 2", unit_price: 20, total: 20 },
      ],
      subtotal: "30.00",
      taxes: "3.00",
      discounts: "2.00",
      total: "31.00",
    };

    (getOrder as jest.Mock).mockResolvedValue(mockOrder);

    render(await OrderPage({ params: { orderId: "1" } }));

    await waitFor(() => {
      expect(screen.getByText(`Order #${mockOrder.id}`)).toBeInTheDocument();
      expect(screen.getByText(mockOrder.created)).toBeInTheDocument();
      expect(screen.getByText(mockOrder.items[0].name)).toBeInTheDocument();
      expect(screen.getByText(mockOrder.items[1].name)).toBeInTheDocument();
      expect(screen.getByText(mockOrder.subtotal)).toBeInTheDocument();
      expect(screen.getByText(mockOrder.taxes)).toBeInTheDocument();
      expect(screen.getByText(mockOrder.total)).toBeInTheDocument();
    });
  });
});
