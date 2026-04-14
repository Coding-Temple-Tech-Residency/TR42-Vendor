export function getToken(): string {
  const token = localStorage.getItem("token");

  if (!token) {
    throw new Error("No authentication token found. Please log in.");
  }

    return token;
}

export function getAuthHeaders(): { Authorization?: string } {
    const token = getToken();
    return token ? { Authorization: `Bearer ${token}` } : {};
}

export function getVendorId(): string {
    const vendorId = localStorage.getItem("vendor_id");

    if (!vendorId) {
        throw new Error("No vendor ID found. Please log in.");
    }

    return vendorId;
}