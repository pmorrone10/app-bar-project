interface ToastProp {
  message: string;
}

export const Toast: React.FC<ToastProp> = ({ message }) => {
  return (
    <div>
      <div
        className="max-w-xs bg-gray-500 text-sm text-white rounded-md shadow-lg dark:bg-gray-700 mb-3 ml-3 mt-5"
        role="alert"
      >
        <div className="flex p-4">
          {message}
          <div className="ml-auto">
            <button
              type="button"
              className="inline-flex flex-shrink-0 justify-center items-center h-4 w-4 rounded-md text-white/[.5] hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-600 focus:ring-gray-500 transition-all text-sm dark:focus:ring-offset-gray-700 dark:focus:ring-gray-500"
            ></button>
          </div>
        </div>
      </div>
    </div>
  );
};
