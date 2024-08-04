export interface Item {
  name: string;
  unit_price: number;
  total: number;
}

export interface Order {
  id: string;
  created: string;
  paid: boolean;
  subtotal: string;
  total: string;
  taxes: string;
  discounts: string;
  items: Item[];
}
