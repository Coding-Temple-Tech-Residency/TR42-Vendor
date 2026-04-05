import { NavLink } from "react-router-dom";
import { 
    HomeIcon,
    ClipboardDocumentListIcon,
    TicketIcon,
    UsersIcon,
    DocumentTextIcon,
    ChartBarIcon,
    ShieldExclamationIcon,
    ChatBubbleLeftRightIcon,
    Cog6ToothIcon,
    UserIcon,
} from "@heroicons/react/24/outline";
import logo from "../../assets/logo.png";



export default function Sidebar() {
    const baseLink = 
        "flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-100 border-l-4 border-transparent";
    const activeLink = 
        "bg-slate-200 text-slate-900 font-semibold border-l-[#1E3A5F]";

        return (
            <aside className="flex h-full w-64 flex-col border-r bg-[#E5E7EB]">
                <div className="flex h-24 items-center justify-center px-4 bg-white">
                    <img src={logo} alt="Vendor Portal" className="w-full max-w-45 h-auto object-contain" />
                </div>

                <div className="border-b border-[#1F2A44]"/>

                <div className="flex flex-1 flex-col px-4 py-6 whitespace-nowrap">
                    <nav className="flex flex-1 flex-col gap-2">
                        <NavLink
                            to="/dashboard"
                            className={({ isActive }) =>    
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <HomeIcon className="h-5 w-5" />
                        Dashboard</NavLink>

                        <NavLink
                            to="/work-orders"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <ClipboardDocumentListIcon className="h-5 w-5" />
                        Work Orders</NavLink>

                        <NavLink
                            to="/tickets"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <TicketIcon className="h-5 w-5" />
                        Tickets</NavLink>

                        <NavLink
                            to="/contractors"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <UsersIcon className="h-5 w-5" />
                        Contractors</NavLink>

                        <NavLink
                            to="/invoices"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <DocumentTextIcon className="h-5 w-5"/>
                        Invoices</NavLink>

                        <NavLink
                            to="/reports"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <ChartBarIcon className="h-5 w-5" />
                        Reports</NavLink>

                        <NavLink
                            to="/fraud-risk"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <ShieldExclamationIcon className="h-5 w-5" />
                        Fraud Risk</NavLink>

                        <NavLink
                            to="/messages"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <ChatBubbleLeftRightIcon className="w-5 h-5" />
                        Messages</NavLink>

                        <NavLink
                            to="/admin"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <UserIcon className="w-5 h-5" />
                        Admin</NavLink>
                    </nav>

                    <nav className="mt-auto pt-6">
                        <NavLink
                            to="/settings"
                            className={({ isActive }) => 
                            `${baseLink} ${isActive ? activeLink : ""}`
                        }
                    >
                        <Cog6ToothIcon className="w-5 h-5" />
                        Settings</NavLink>
                    </nav>
                </div>
            </aside>
        );

}