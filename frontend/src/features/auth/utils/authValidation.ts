import type { User, Vendor } from "../types/types";

const PHONE_REGEX = /^\d{3}-\d{3}-\d{4}$/;
const ADDRESS_REGEX = /^[A-Za-z0-9\s.'#,-]{5,120}$/;
const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const ZIP_REGEX = /^\d{5}(-\d{4})?$/;
const STATE_REGEX = /^[A-Z]{2}$/;
const CITY_REGEX = /^[A-Za-z\s.'-]{2,50}$/;

function isBlank(value?: string) {
  return !value || !value.trim();
}

function validateName(
  value: string,
  fieldName = "Name",
  minLength = 2,
): string | null {
  if (!value || value.trim().length < minLength) {
    return `${fieldName} must be at least ${minLength} characters long`;
  }

  return null;
}

function validateEmailFormat(value: string): string | null {
  if (!EMAIL_REGEX.test(value.trim())) {
    return "Invalid email address, must be in format: user@example.com";
  }

  return null;
}

function validatePhoneFormat(value: string): string | null {
  if (!PHONE_REGEX.test(value.trim())) {
    return "Invalid phone number format (XXX-XXX-XXXX)";
  }

  return null;
}

function validateAddress(value: string): string | null {
  if (!ADDRESS_REGEX.test(value.trim())) {
    return "Enter a valid street address (e.g., '123 Main St')";
  }

  return null;
}

function validateCity(value: string): string | null {
  if (!CITY_REGEX.test(value.trim())) {
    return "Enter a valid city.";
  }

  return null;
}

function validateState(value: string): string | null {
  if (!STATE_REGEX.test(value.trim())) {
    return "Enter a valid 2-letter state code.";
  }

  return null;
}

function validateZip(value: string): string | null {
  if (!ZIP_REGEX.test(value.trim())) {
    return "Enter a valid ZIP code.";
  }

  return null;
}

function getPasswordChecks(password: string, user: User) {
  const passwordLower = (password || "").toLowerCase();

  const username = (user.username || "").trim().toLowerCase();
  const firstName = (user.firstName || "").trim().toLowerCase();
  const lastName = (user.lastName || "").trim().toLowerCase();

  return {
    minLength: password.length >= 12,
    hasLowercase: /[a-z]/.test(password),
    hasUppercase: /[A-Z]/.test(password),
    hasDigit: /\d/.test(password),
    hasSpecial: /[^A-Za-z0-9]/.test(password),
    noTripleRepeat: !/(.)\1{2,}/.test(password),
    noUsername: !(username.length >= 4 && passwordLower.includes(username)),
    noFirstName: !(firstName.length >= 4 && passwordLower.includes(firstName)),
    noLastName: !(lastName.length >= 4 && passwordLower.includes(lastName)),
  };
}

// Validate register form
function validateUserRegisterForm(form: User) {
  const errors: any = {};

  // Required fields
  const firstNameError = validateName(form.firstName, "First name");
  if (firstNameError) {
    errors.firstName = firstNameError;
  }

  const lastNameError = validateName(form.lastName, "Last name");
  if (lastNameError) {
    errors.lastName = lastNameError;
  }

  const emailError = validateEmailFormat(form.email);
  if (emailError) {
    errors.email = emailError;
  }

  if (isBlank(form.username)) {
    errors.username = "Username is required.";
  }

  const checks = getPasswordChecks(form.password, form);

  if (!Object.values(checks).every(Boolean)) {
    errors.password =
      "Password must be at least 12 characters long and include uppercase, lowercase, number, and special character, and must not contain more than 2 identical characters in a row or contain your username, first name, or last name.";
  }

  // Confirm password
  if (!form.confirmPassword) {
    errors.confirmPassword = "Confirm your password";
  } else if (form.password !== form.confirmPassword) {
    errors.confirmPassword = "Passwords do not match";
  }

  return errors;
}

// Format phone number (123) 456-7890
function formatPhoneNumber(value: string) {
  const numbers = value.replace(/\D/g, "");
  const trimmed = numbers.slice(0, 10);

  if (trimmed.length < 4) {
    return trimmed;
  } else if (trimmed.length < 7) {
    return "(" + trimmed.slice(0, 3) + ") " + trimmed.slice(3);
  } else {
    return (
      "(" +
      trimmed.slice(0, 3) +
      ") " +
      trimmed.slice(3, 6) +
      "-" +
      trimmed.slice(6)
    );
  }
}

function toBackendPhoneFormat(value: string) {
  const digits = value.replace(/\D/g, "").slice(0, 10);

  if (digits.length !== 10) return value;

  return `${digits.slice(0, 3)}-${digits.slice(3, 6)}-${digits.slice(6)}`;
}

// Validate Profile Setup form
function validateVenderRegisterForm(form: Vendor) {
  const errors: any = {};

  const companyNameError = validateName(form.companyName, "Company name");
  if (companyNameError) {
    errors.companyName = companyNameError;
  }

  const contactNameError = validateName(
    form.primaryContactName,
    "Primary contact name",
  );
  if (contactNameError) {
    errors.primaryContactName = contactNameError;
  }

  const addressError = validateAddress(form.address);
  if (addressError) {
    errors.address = addressError;
  }

  const cityError = validateCity(form.city);
  if (cityError) {
    errors.city = cityError;
  }

  const stateError = validateState(form.state);
  if (stateError) {
    errors.state = stateError;
  }

  const zipError = validateZip(form.zip);
  if (zipError) {
    errors.zip = zipError;
  }

  const emailError = validateEmailFormat(form.companyEmail);
  if (emailError) {
    errors.companyEmail = emailError;
  }

  const phoneError = validatePhoneFormat(
    toBackendPhoneFormat(form.companyPhone),
  );
  if (phoneError) {
    errors.companyPhone = phoneError;
  }

  if (isBlank(form.serviceType)) {
    errors.serviceType = "Select a service type.";
  }

  return errors;
}

// Export functions
export {
  formatPhoneNumber,
  getPasswordChecks,
  toBackendPhoneFormat,
  validateVenderRegisterForm,
  validateUserRegisterForm,
};
