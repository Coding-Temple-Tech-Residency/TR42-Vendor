import AppLayout from "../components/layout/AppLayout";
import Sidebar from "../components/layout/SideBar";
import Topbar from "../components/layout/Topbar";
import PageHeader from "../components/UI/PageHeader";
import KPICard from "../components/UI/KPICard";
import { Link } from "react-router-dom";
import SectionCard from "../components/UI/SectionCard";
import EmptyState from "../components/UI/EmptyState";

export default function WorkOrdersDashboardPage() {
  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >

      <div className="space-y-6">
        <PageHeader
          title="Work Orders"
          description="Manage, track, and assign work orders."
        />

        <div className="flex gap-4">
          <Link
            to="/vendor/work-orders/overview"
            className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
            >
              Veiw All Work Orders
          </Link>
          
          <Link
            to="/vendor/work-orders/edit"
            className="inline-block rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#1E3A5F]"
            >
              Edit Work Order
          </Link>
        </div>

        {/* KPI Cards */}
        <div className="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
          <KPICard
            title="Overdue"
            value={5}
            subtitle="Work Orders"
            colorVariant="red"
            badge={{ type: "text", value: "Needs Attention" }}
          />

          <KPICard
            title="Unassigned"
            value={12}
            subtitle="Work Orders"
            colorVariant="orange"
            badge={{
              type: "text",
              value: "Needs Assignment",
            }}
          />

          <KPICard
            title="Assigned"
            value={8}
            subtitle="Not Started"
            colorVariant="gray"
            badge={{ type: "text", value: "Scheduled" }}
          />

          <KPICard
            title="In Progress"
            value={21}
            subtitle="Assigned Contractors"
            colorVariant="blue"
            badge={{ type: "text", value: "On Site" }}
          />

          <KPICard
            title="Completed"
            value={45}
            subtitle="This Week"
            colorVariant="green"
            badge={{
              type: "trend",
              value: "12% from last week",
              trendDirection: "up",
            }}
          />

          <KPICard
            title="Inovices Created"
            value="2.4 days"
            subtitle="This month"
            colorVariant="purple"
            badge={{
              type: "trend",
              value: "0.5 days slower",
              trendDirection: "up",
            }}
          />
        </div>

        <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
            <SectionCard title="Work Order Status">
            <EmptyState
              title="Chart coming soon"
              description="This section will display Work Orders and their status in a donut chart form."
            />
          </SectionCard>
  
          <SectionCard title="Work Orders Created">
            <EmptyState
              title="Chart coming soon"
              description="This section will display number of Work Orders created in a month in bar chart form."
            />
          </SectionCard>
        </div>
  
        <div className="mt-6 grid grid-cols-1">
          <SectionCard title="Unassigned Work Orders">
            <EmptyState
              title="No Active Work Orders"
              description="This section will contain a table of unassigned Work Orders."
            />
          </SectionCard>
        </div>
  
  
        <div className="mt-6 grid grid-cols-1 gap-6 xl:grid-cols-2">
            <SectionCard title="Assigned to Ticket">
            <EmptyState
              title="No Tickets Assigned Work Orders"
              description="This section will contain a table of assigned Work Orders."
            />
          </SectionCard>
  
          <SectionCard title="In Progress">
            <EmptyState
              title="No Work Orders In Progress"
              description="This section will contain a table of in progress Work Orders."
            />
          </SectionCard>
        </div>

        <div className="mt-6 grid grid-cols-1">
          <SectionCard title="Recently Completed">
            <EmptyState
              title="No Recently Completed Work Orders"
              description="This section will contain a table of recently completed Work Orders."
            />
          </SectionCard>
        </div>

      </div>
    </AppLayout>
  );
}
