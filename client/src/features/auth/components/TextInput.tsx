type TextInputProps = {
    label: string;
    name: string;
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    type?: string;
    placeholder?: string;
};

export default function TextInput({
    label,
    name,
    value,
    onChange,
    type = "text",
    placeholder="",
}: TextInputProps) {
    return(
        <div className="flex flex-col gap-1">
            <label
                className="text-sm font-medium text-gray-700"
                htmlFor={name}
                >{label}</label>

                <input
                    className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm text-gray-700 placeholder:text-gray-4-- focus:outline-none focus:ring-2 focus:ring-[#2F3B4A] focus:border-[#2F3B4A]"
                    id={name}
                    name={name}
                    type={type}
                    value={value}
                    onChange={onChange}
                    placeholder={placeholder}
                />
        </div>
    );
}