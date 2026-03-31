import logo from "../../../assets/logo.png";

export default function AuthLayout({
    children,
} : {
    children: React.ReactNode;
}) {
    return(
        <div 
            className="min-h-screen flex flex-col items-center justify-center px-4"
            style={{
                background:
                    "linear-gradient(to top, #243041 0%, #465366 40%, #e5e8ed 100%)",
            }}
        >
            <img src={logo} alt="Field Force Logo" className="w-40 mb-6" />

            {children}
        </div>
    );
}