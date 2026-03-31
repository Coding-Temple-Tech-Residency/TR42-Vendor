type AuthButtonProps = {
    children: React.ReactNode;
    type?: "button" | "submit";
    onClick?: () => void;
    disabled?: boolean;
};

export default function AuthButton({
    children,
    type = "button",
    onClick,
    disabled = false,
}: AuthButtonProps) {
    return (
        <button
            type={type}
            onClick={onClick}
            disabled={disabled}
            className={`w-full rounded-md py-2 font-medium text-white transition-colors
                ${
                    disabled
                        ? "bg-gray-400 cursor-not-allowed"
                        : "bg-[#3E4C5E] hover:bg-[#2F3B4A] active:bg-[#243041]"
                }`}
                > {children}</button>
    );
}