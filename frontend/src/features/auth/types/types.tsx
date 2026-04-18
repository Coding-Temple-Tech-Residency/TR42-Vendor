export type User = {
  firstName: string;
  middleName?: string;
  lastName: string;
  email: string;
  username: string;
  password: string;
  confirmPassword: string;
  contactNumber: string;
  alternateNumber: string;
  dateOfBirth: string;
  ssnLastFour?: string;
  address: string;
  city: string;
  state: string;
  zip: string;
};

export type Contractor = {
  first_name: string;
  last_name: string;
  middle_name: string;
  date_of_birth: string;
  ssn_last_four: string;
  email: string;
  contact_number: string;
  alternate_number: string;
  username: string;
  password?: string;
  address: {
    street: string;
    city: string;
    state: string;
    zip: string;
  };
  status: "ACTIVE" | "INACTIVE";
  vendor_contractor_role: "DRIVER" | "WORKER" | "PRIVATE_CONTRACTOR";
  tickets_completed: number;
  tickets_open: number;
  biometric_enrolled: boolean;
  is_onboarded: boolean;
  is_subcontractor: boolean;
  is_fte: boolean;
  is_licensed: boolean;
  is_insured: boolean;
  is_certified: boolean;
  average_rating: number;
  years_experience: number;
};

export type Vendor = {
  companyName: string;
  primaryContactName: string;
  address: string;
  city: string;
  state: string;
  zip: string;
  companyEmail: string;
  companyPhone: string;
  serviceType: string;
};
