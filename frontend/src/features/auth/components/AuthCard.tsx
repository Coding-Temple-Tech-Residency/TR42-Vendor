export default function AuthCard({
    children,
} : {
    children : React.ReactNode;
}) {
    return (
        // <div className="w-full max-w-md bg-white rounded-xl shadow-lg p-8 flex flex-col gap-6">

        <div className="w-full max-w-2xl bg-white rounded-b-xl shadow-2xl p-10 flex flex-col gap-6">
            {children}
        </div>
    );
}