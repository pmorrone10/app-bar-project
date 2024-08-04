import { Order } from "../../interfaces/Order";

export const getOrder = async (orderId: string): Promise<Order | null> => {
  if (!orderId) return null;

  const apiUrl = process.env.API_URL;

  try {
    const response = await fetch(`${apiUrl}${orderId}`);

    if (response.status != 200) {
      return null;
    }

    const data = await response.json();

    return data;
  } catch (error) {
    console.log(error);
    return null;
  }

  return null;
};
