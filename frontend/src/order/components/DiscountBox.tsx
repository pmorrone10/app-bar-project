"use client";

import { useState, useEffect } from "react";
import { Toast } from "./Toast";

export const DiscountBox = () => {
  const [discount, setDiscount] = useState("");
  const [showMessage, setShowMessage] = useState(false);

  const handleChange = ({
    currentTarget,
  }: React.FormEvent<HTMLInputElement>) => {
    setDiscount(currentTarget.value);
  };

  const handleClick = () => {
    console.log(discount);
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
    <div className="flex flex-col justify-center px-4 py-6 md:p-6 xl:p-8 w-1/2 bg-gray-50 dark:bg-gray-800 space-y-6">
      <h3 className="text-xl dark:text-white font-semibold leading-5 text-gray-800">
        Discount Code
      </h3>
      <div className="w-full flex justify-center items-center">
        <input
          className="h-12 py-5 w-96 md:w-full dark:border-bg-gray-500 indent-4 text-emerald-900 shadow-lg focus:outline-none focus:ring focus:ring-bg-gray-300"
          placeholder="ADD YOUR DISCOUNT CODE"
          onChange={handleChange}
          value={discount}
        ></input>
      </div>
      <div className="w-full flex justify-center items-center">
        <button
          className="hover:bg-black dark:bg-white dark:text-gray-800 dark:hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 py-5 w-96 md:w-full bg-gray-800 text-base font-medium leading-4 text-white"
          onClick={handleClick}
        >
          Apply
        </button>
      </div>
      {showMessage && <Toast message="Not Implement Yet"></Toast>}
    </div>
  );
};
