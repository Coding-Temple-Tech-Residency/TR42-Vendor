import { zodResolver } from "@hookform/resolvers/zod";
import { FormProvider, useForm } from "react-hook-form";
import { Link, Outlet } from "react-router-dom";

import PageHeader from "../../../../features/components/UI/PageHeader";
import AppLayout from "../../../../features/components/layout/AppLayout";
import Sidebar from "../../../../features/components/layout/SideBar";
import Topbar from "../../../../features/components/layout/Topbar";

import {
  createContractorSchema,
  type CreateContractorFormValues,
} from "./schemas/createContractorSchema";
import { defaultValues } from "./schemas/defaultValues";

const CreateContractorFlow = () => {
  const methods = useForm<CreateContractorFormValues>({
    resolver: zodResolver(createContractorSchema),
    defaultValues,
    mode: "onBlur",
  });

  return (
    <AppLayout
      sidebar={<Sidebar />}
      topbar={<Topbar title="Vendor Dashboard" userName="Katty" />}
    >
      <FormProvider {...methods}>
        <div className="space-y-6">
          <PageHeader
            title="Create Contractor"
            description="Add a new contractor to your vendor account."
          />

          <div className="flex items-center">
            <Link
              to="/vendor/contractors"
              className="rounded-lg bg-[#2F4F75] px-4 py-3 text-sm font-medium text-white transition hover:bg-[#1E3A5F]"
            >
              Back to Contractors
            </Link>
          </div>

          <div>
            <Outlet />
          </div>
        </div>
      </FormProvider>
    </AppLayout>
  );
};

export { CreateContractorFlow };
