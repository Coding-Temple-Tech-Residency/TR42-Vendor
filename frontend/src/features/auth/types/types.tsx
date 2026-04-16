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
