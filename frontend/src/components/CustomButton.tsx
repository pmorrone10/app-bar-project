interface CustomButtonProps {
  text: string;
  handleClick: () => void;
}
export const CustomButton: React.FC<CustomButtonProps> = ({
  text,
  handleClick,
}) => {
  return (
    <button
      className="hover:bg-black dark:bg-white dark:text-gray-800 dark:hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 py-5 w-96 md:w-full bg-gray-800 text-base font-medium leading-4 text-white"
      onClick={handleClick}
    >
      {text}
    </button>
  );
};
