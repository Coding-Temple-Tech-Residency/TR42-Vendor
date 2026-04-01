type AuthHeaderProps = {
    title: string;
    subtitle?: string;
};

export default function AuthHeader({ title, subtitle }: AuthHeaderProps) {
    return(
        <div className="text-center mb-6">
            <h1 className="text-2xl font-semibold text-gray-800">{title}</h1>

            {subtitle && (
                <p className="text-sm text-gray-500 mt-1">{subtitle}</p>
            )}
        </div>
    );
}