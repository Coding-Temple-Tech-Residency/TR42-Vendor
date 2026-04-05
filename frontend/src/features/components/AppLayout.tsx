type AppLayoutProps = {
    sidebar: React.ReactNode;
    topbar: React.ReactNode;
    children: React.ReactNode;
};

export default function AppLayout({
    sidebar,
    topbar,
    children
}: AppLayoutProps){
    return (
        <div 
            className="min-h-screen"
            style={{
                background:`
                    radial-gradient(
                                circle at top right,
                                rgba(30, 58, 95, 0.5) 0%,
                                rgba(30, 58, 95, 0.35) 20%,
                                rgba(30, 58, 95, 0.2) 35%,
                                rgba(30, 58, 95, 0.05) 50%,
                                transparent 65%
                            ),
                            #ffffff                    
                            `,                    
                }}>
            <div className="flex min-h-screen">
                <aside className="hidden w-64 shrink-0 lg:block">
                    {sidebar}
                </aside>

                <div className="flex min-w-0 flex-1 flex-col">
                    <div className="sticky top-0 z-20 border-b border-[#1E3A5F] bg-[#E5E7EB]/50">
                        {topbar}
                    </div>

                    <main className="flex-1 p-4 sm:p-6 lg:p-8">
                        <div className="w-full">
                            {children}
                        </div>
                    </main>
                </div>
            </div>
        </div>
    );
}