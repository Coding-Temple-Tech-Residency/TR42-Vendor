export async function getDashboardData() {
  const response = await fetch("http://localhost:3000/api/dashboard");
  if (!response.ok) {
    throw new Error("Failed to load dashboard data");
  }
  return response.json();
}
