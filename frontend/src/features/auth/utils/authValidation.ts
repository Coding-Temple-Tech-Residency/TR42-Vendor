// check password rules
function getPasswordChecks(password: string) {
  return {
    length: password.length >= 6, // at least 6 characters
    uppercase: /[A-Z]/.test(password), // must include uppercase letter
    lowercase: /[a-z]/.test(password), // must include lowercase letter
    number: /\d/.test(password), // must include a number
    special: /[^A-Za-z0-9]/.test(password), // must include special character
  };
}

// Validate register form
function validateRegisterForm(form: any) {
  const errors: any = {};

  // Required fields
  if (!form.firstName) {
    errors.firstName = "First name is required";
  }

  if (!form.lastName) {
    errors.lastName = "Last name is required";
  }

  if (!form.email) {
    errors.email = "Email is required";
  }

  if (!form.username) {
    errors.username = "Username is required";
  }

  // Password rules
  if (!form.password) {
    errors.password = "Password is required";
  } else {
    const checks = getPasswordChecks(form.password);

    if (!checks.length) {
      errors.password = "Must be at least 8 characters";
    } else if (!checks.uppercase) {
      errors.password = "Must include an uppercase letter";
    } else if (!checks.lowercase) {
      errors.password = "Must include a lowercase letter";
    } else if (!checks.number) {
      errors.password = "Must include a number";
    } else if (!checks.special) {
      errors.password = "Must include a special character";
    }
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

// Validate Profile Setup form
function validateProfileForm(form: any) {
  const errors: any = {};

  if (!form.companyName) {
    errors.companyName = "Company name is required";
  }

  if (!form.address) {
    errors.address = "Address is required";
  }

  if (!form.city) {
    errors.city = "City is required";
  }

  if (!form.state) {
    errors.state = "State is required";
  }

  if (!form.zip) {
    errors.zip = "Zip code is required";
  }

  if (!form.companyEmail) {
    errors.companyEmail = "Email is required";
  }

  if (!form.companyPhone) {
    errors.companyPhone = "Phone is required";
  }

  if (!form.serviceType) {
    errors.serviceType = "Select a service type";
  }

  return errors;
}

// Export functions
export { 
  getPasswordChecks, 
  validateRegisterForm, 
  formatPhoneNumber,
  validateProfileForm
};