import { useState } from "react";

type PasswordInputProps = {
    label: string;
    name: string;
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
};

export default function PasswordInput({
    label,
    name,
    value,
    onChange,
    placeholder = "Enter password",
}: PasswordInputProps) {
    const [showPassword, setShowPassword] = useState(false)
    
    return (
        <div className="flex flex-col gap-1">
            <label
                htmlFor={name}
                className="text-sm font-medium text-gray-700"
                >{label}</label>

            <div className="relative">
                <input
                    className="w-full rounded-md border border-gray-300 px-3 py-2 pr-16 text-sm text-gray-700 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#2F3B4A] focus:border-[#2F3B4A]"
                    id={name}
                    type={showPassword ? "text" : "password"}
                    name={name}
                    value={value}
                    onChange={onChange}
                    placeholder={placeholder}
                />

                <button
                    className="absolute right-3 -translate-y-1/2 top-1/2 text-sm font-medium text-gary-500 hover:text-[#2F3B4A]"
                    type="button"
                    onClick={() =>setShowPassword((prev) => !prev)}
                    >
                        {showPassword ? "Hide" : "Show"}
                    </button>
            </div>

        </div>
    );
}