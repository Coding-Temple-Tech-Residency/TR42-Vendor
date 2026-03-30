import { Link } from "react-router-dom";

type AuthFooterLinkProps = {
  text: string;
  linkText: string;
  to: string;
};

export default function AuthFooterLink({
  text,
  linkText,
  to,
}: AuthFooterLinkProps) {
  return (
    <p className="mt-4 text-center text-sm text-gray-600">
      {text}{" "}
      <Link
        to={to}
        className="font-medium text-[#3E4C5E] hover:text-[#2F3B4A] hover:underline"
      >
        {linkText}
      </Link>
    </p>
  );
}