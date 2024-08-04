import { ItemGrid } from "@/order/components/ItemGrid";
import { getOrder } from "../../../order/actions/OrderAction";
import { Header } from "../../../order/components/Header";
import { Summary } from "../../../order/components/Summary";

export default async function OrderPage({
  params = { orderId: "" },
}: {
  params: { orderId: string };
}) {
  const data = await getOrder(params.orderId);

  if (!data) {
    return (
      <div className="py-14 px-4 md:px-6 2xl:px-20 2xl:container 2xl:mx-auto">
        <div className="error-message bg-red-100 text-red-700 p-4 rounded">
          Order not found
        </div>
      </div>
    );
  }

  return (
    <div className="py-14 px-4 md:px-6 2xl:px-20 2xl:container 2xl:mx-auto">
      <Header orderId={data!.id} date={data!.created} />
      <div className="mt-10 flex flex-col xl:flex-row jusitfy-center items-stretch w-full xl:space-x-8 space-y-4 md:space-y-6 xl:space-y-0">
        <div className="flex flex-col justify-start items-start w-full space-y-4 md:space-y-6 xl:space-y-8">
          <ItemGrid items={data!.items} />
        </div>
        <Summary
          subtotal={data!.subtotal}
          taxes={data!.taxes}
          discount={data!.discounts}
          total={data!.total}
        />
      </div>
    </div>
  );
}
