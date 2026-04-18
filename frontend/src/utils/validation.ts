import type { Contractor, User, Vendor } from "../types/models";

const PHONE_REGEX = /^\d{3}-\d{3}-\d{4}$/;
const ADDRESS_REGEX = /^[A-Za-z0-9\s.'#,-]{5,120}$/;
const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const ZIP_REGEX = /^\d{5}(-\d{4})?$/;
const STATE_REGEX = /^[A-Z]{2}$/;
const CITY_REGEX = /^[A-Za-z\s.'-]{2,50}$/;
const SSN_LAST_FOUR_REGEX = /^\d{4}$/;
const DATE_REGEX = /^\d{4}-\d{2}-\d{2}$/;

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

function validateSsnLastFour(value?: string): string | null {
  if (!value) {
    return null;
  }

  if (!SSN_LAST_FOUR_REGEX.test(value.trim())) {
    return "SSN last four must be exactly 4 digits.";
  }

  return null;
}

function validateDateOfBirth(value?: string): string | null {
  if (!value) {
    return null;
  }

  if (!DATE_REGEX.test(value.trim())) {
    return "Date of birth must be in YYYY-MM-DD format.";
  }

  const parsed = new Date(`${value}T00:00:00`);
  if (Number.isNaN(parsed.getTime())) {
    return "Enter a valid date of birth.";
  }

  const today = new Date();
  if (parsed > today) {
    return "Date of birth cannot be in the future.";
  }

  return null;
}

function getPasswordChecks(
  password: string,
  user: Pick<User, "username" | "firstName" | "lastName">,
) {
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

function validateUserRegisterForm(form: User) {
  const errors: Record<string, string> = {};

  const firstNameError = validateName(form.firstName, "First name");
  if (firstNameError) errors.firstName = firstNameError;

  const lastNameError = validateName(form.lastName, "Last name");
  if (lastNameError) errors.lastName = lastNameError;

  const emailError = validateEmailFormat(form.email);
  if (emailError) errors.email = emailError;

  if (isBlank(form.username)) {
    errors.username = "Username is required.";
  }

  const contactNumberError = validatePhoneFormat(
    toBackendPhoneFormat(form.contactNumber || ""),
  );
  if (contactNumberError) errors.contactNumber = contactNumberError;

  if (!isBlank(form.alternateNumber)) {
    const alternateNumberError = validatePhoneFormat(
      toBackendPhoneFormat(form.alternateNumber || ""),
    );
    if (alternateNumberError) errors.alternateNumber = alternateNumberError;
  }

  const dateOfBirthError = validateDateOfBirth(form.dateOfBirth);
  if (dateOfBirthError) errors.dateOfBirth = dateOfBirthError;

  const ssnLastFourError = validateSsnLastFour(form.ssnLastFour);
  if (ssnLastFourError) errors.ssnLastFour = ssnLastFourError;

  const streetError = validateAddress(form.address);
  if (streetError) errors.street = streetError;

  const cityError = validateCity(form.city);
  if (cityError) errors.city = cityError;

  const stateError = validateState(form.state);
  if (stateError) errors.state = stateError;

  const zipError = validateZip(form.zip);
  if (zipError) errors.zip = zipError;

  const checks = getPasswordChecks(form.password, {
    username: form.username,
    firstName: form.firstName,
    lastName: form.lastName,
  });

  if (!Object.values(checks).every(Boolean)) {
    errors.password =
      "Password must be at least 12 characters long and include uppercase, lowercase, number, and special character, and must not contain more than 2 identical characters in a row or contain your username, first name, or last name.";
  }

  if (!form.confirmPassword) {
    errors.confirmPassword = "Confirm your password";
  } else if (form.password !== form.confirmPassword) {
    errors.confirmPassword = "Passwords do not match";
  }

  return errors;
}

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

function validateVendorRegisterForm(form: Vendor) {
  const errors: Record<string, string> = {};

  const companyNameError = validateName(form.companyName, "Company name");
  if (companyNameError) errors.companyName = companyNameError;

  const contactNameError = validateName(
    form.primaryContactName,
    "Primary contact name",
  );
  if (contactNameError) errors.primaryContactName = contactNameError;

  const addressError = validateAddress(form.address);
  if (addressError) errors.address = addressError;

  const cityError = validateCity(form.city);
  if (cityError) errors.city = cityError;

  const stateError = validateState(form.state);
  if (stateError) errors.state = stateError;

  const zipError = validateZip(form.zip);
  if (zipError) errors.zip = zipError;

  const emailError = validateEmailFormat(form.companyEmail);
  if (emailError) errors.companyEmail = emailError;

  const phoneError = validatePhoneFormat(
    toBackendPhoneFormat(form.companyPhone),
  );
  if (phoneError) errors.companyPhone = phoneError;

  if (isBlank(form.serviceType)) {
    errors.serviceType = "Select a service type.";
  }

  return errors;
}

function validateContractorForm(form: Contractor, mode: "create" | "edit") {
  const errors: Record<string, string> = {};

  const firstNameError = validateName(form.first_name, "First name");
  if (firstNameError) errors.first_name = firstNameError;

  const lastNameError = validateName(form.last_name, "Last name");
  if (lastNameError) errors.last_name = lastNameError;

  if (!isBlank(form.middle_name)) {
    const middleNameError = validateName(form.middle_name, "Middle name", 1);
    if (middleNameError) errors.middle_name = middleNameError;
  }

  const emailError = validateEmailFormat(form.email);
  if (emailError) errors.email = emailError;

  if (isBlank(form.username)) {
    errors.username = "Username is required.";
  }

  const contactNumberError = validatePhoneFormat(
    toBackendPhoneFormat(form.contact_number || ""),
  );
  if (contactNumberError) errors.contact_number = contactNumberError;

  if (!isBlank(form.alternate_number)) {
    const alternateNumberError = validatePhoneFormat(
      toBackendPhoneFormat(form.alternate_number || ""),
    );
    if (alternateNumberError) errors.alternate_number = alternateNumberError;
  }

  const dateOfBirthError = validateDateOfBirth(form.date_of_birth);
  if (dateOfBirthError) errors.date_of_birth = dateOfBirthError;

  const ssnLastFourError = validateSsnLastFour(form.ssn_last_four);
  if (ssnLastFourError) errors.ssn_last_four = ssnLastFourError;

  const streetError = validateAddress(form.address.street);
  if (streetError) errors["address.street"] = streetError;

  const cityError = validateCity(form.address.city);
  if (cityError) errors["address.city"] = cityError;

  const stateError = validateState(form.address.state);
  if (stateError) errors["address.state"] = stateError;

  const zipError = validateZip(form.address.zip);
  if (zipError) errors["address.zip"] = zipError;

  if (mode === "create") {
    if (!form.password) {
      errors.password = "Password is required.";
    } else {
      const checks = getPasswordChecks(form.password, {
        username: form.username,
        firstName: form.first_name,
        lastName: form.last_name,
      });

      if (!Object.values(checks).every(Boolean)) {
        errors.password =
          "Password must be at least 12 characters long and include uppercase, lowercase, number, and special character, and must not contain more than 2 identical characters in a row or contain your username, first name, or last name.";
      }
    }
  }

  return errors;
}

export {
  formatPhoneNumber,
  getPasswordChecks,
  toBackendPhoneFormat,
  validateContractorForm,
  validateUserRegisterForm,
  validateVendorRegisterForm,
};
