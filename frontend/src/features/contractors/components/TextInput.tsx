import React from "react";

type TextInputProps = {
  name: string;
  value: string | number;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  type?: string;
  maxLength?: number;
};

export function TextInput({
  name,
  value,
  onChange,
  type = "text",
  maxLength,
}: TextInputProps) {
  return (
    <input
      name={name}
      type={type}
      value={value}
      maxLength={maxLength}
      onChange={onChange}
      className="mt-2 w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75]"
    />
  );
}
