import pandas as pd

wo = pd.read_csv("data/work_orders.csv")
tickets = pd.read_csv("data/ticket.csv")

wo["created_at"] = pd.to_datetime(wo["created_at"])
tickets["created_at"] = pd.to_datetime(tickets["created_at"])

today = pd.Timestamp.now().normalize()

print("Work orders today:", (wo["created_at"] >= today).sum())
print("Tickets today:", (tickets["created_at"] >= today).sum())

print("Work orders last 30 days:", (wo["created_at"] >= pd.Timestamp.now() - pd.Timedelta(days=30)).sum())
print("Tickets last 30 days:", (tickets["created_at"] >= pd.Timestamp.now() - pd.Timedelta(days=30)).sum())

completed_work_orders = wo[(wo['created_at'] >= pd.Timestamp.now() - pd.Timedelta(days=30)) & (wo['current_status'] == 'COMPLETED')]

print(completed_work_orders.shape[0])