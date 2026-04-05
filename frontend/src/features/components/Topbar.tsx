type TopbarProps = {
    title?: string;
    userName?: string;
    rightContent?: React.ReactNode;
};

export default function Topbar({
    title = "Dashboard",
    userName = "Vendor User",
    rightContent,
}: TopbarProps) {
    return (
        <div className="flex min-h-18 items-center justify-between px-4 sm:px-6 lg:px-8">
            <div>
                <p className="text-sm text-slate-500">Welcome back</p>
                <h2 className="text-xl font-semibold text-slate-900">{title}</h2>
            </div>

            <div className="flex items-center gap-4">
                {rightContent}

                <div className="flex items-center gap-4 rounded-full border border-slate-200 bg-slate-50 px-10 py-2">
                    <div className="flex h-9 w-9 items-center justify-center rounded-full bg-slate-800 text-sm font-semibold text-white">
                        {userName.slice(0, 1).toUpperCase()}
                    </div>
                    <div className="hidden sm:flex items-baseline whitespace-nowrap gap-2">
                        <p className="text-lg font-medium text-slate-900">{userName}</p>
                        <span className="text-sm text-slate-500">Online</span>
                    </div>
                </div>
            </div>
        </div>
    );
}