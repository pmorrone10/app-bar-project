import { getOrder } from "../../../src/order/actions/OrderAction";

describe("getOrder", () => {
  beforeEach(() => {
    fetchMock.resetMocks();
  });

  test("when response code is 200 then return data", async () => {
    const mock = {
      id: "1",
      created: "2024-09-10 12:00:30",
      items: [
        {
          name: "Corona",
          unit_price: "$ 300,00",
          total: "$ 600,00",
        },
        {
          name: "Club Colombia",
          unit_price: "$ 200,00",
          total: "$ 600,00",
        },
        {
          name: "Quilmes",
          unit_price: "$ 150,00",
          total: "$ 150,00",
        },
      ],
      paid: false,
      subtotal: "$ 1.350,00",
      taxes: "$ 135,00",
      total: "$ 1.485,00",
      discounts: "$ 0,00",
    };
    fetchMock.mockResponseOnce(JSON.stringify(mock), { status: 200 });

    const order = await getOrder("1");

    expect(order).toEqual(mock);
    expect(fetch).toHaveBeenCalledWith("http://localhost:8080/api/v1/order/1");
  });

  test("when response code is not 200 then return null", async () => {
    fetchMock.mockResponseOnce("", { status: 404 });

    const order = await getOrder("1");

    expect(order).toBeNull();
    expect(fetch).toHaveBeenCalledWith("http://localhost:8080/api/v1/order/1");
  });

  test("when there is an error then return null", async () => {
    fetchMock.mockRejectOnce(new Error("API is down"));

    const order = await getOrder("1");

    expect(order).toBeNull();
    expect(fetch).toHaveBeenCalledWith("http://localhost:8080/api/v1/order/1");
  });
  //
  test("when orderId is empty then return null", async () => {
    const order = await getOrder("");

    expect(order).toBeNull();
    expect(fetch).not.toHaveBeenCalled();
  });
});
