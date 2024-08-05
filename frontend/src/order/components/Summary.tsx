"use client";
import { SummaryItem } from "./SummaryItem";
import { useState, useEffect } from "react";
import { Toast } from "./Toast";
import { CustomButton } from "@/components/CustomButton";

interface SummaryProps {
  subtotal: string;
  discount?: string;
  taxes: string;
  total: string;
}

export const Summary: React.FC<SummaryProps> = ({
  subtotal,
  discount,
  taxes,
  total,
}) => {
  const [showMessage, setShowMessage] = useState(false);

  const handleClick = () => {
    setShowMessage(true);
  };

  useEffect(() => {
    if (showMessage) {
      const timer = setTimeout(() => {
        setShowMessage(false);
      }, 3000);

      return () => clearTimeout(timer);
    }
  }, [showMessage]);

  return (
    <div className="flex flex-col px-4 py-6 md:p-6 xl:p-8 w-96 bg-gray-50 dark:bg-gray-800 space-y-6">
      <h3 className="text-xl dark:text-white font-semibold leading-5 text-gray-800">
        Summary
      </h3>
      <div className="flex justify-center items-center w-full space-y-4 flex-col border-gray-200 border-b pb-4">
        <SummaryItem label={"Subtotal"} value={subtotal} />
        {discount && <SummaryItem label={"Discount"} value={discount} />}
        <SummaryItem label={"Taxes"} value={taxes} />
      </div>
      <div className="flex justify-between items-center w-full">
        <SummaryItem label={"Total"} value={total} isSemiBold={true} />
      </div>
      <div className="flex justify-center xl:h-full items-stretch w-full flex-col mt-6 md:mt-0">
        <CustomButton text="PAY" handleClick={handleClick} />
        {showMessage && <Toast message="Not implemented yet" />}
      </div>
    </div>
  );
};
