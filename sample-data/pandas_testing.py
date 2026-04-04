import pandas as pd
import sqlite3

conn = sqlite3.connect("./my_database.db")

addresses = pd.read_sql_query(
    "select * from address", conn,
    parse_dates=['created_at', 'updated_at']
)

contractors = pd.read_sql_query(
    "select * from contractors", conn,
    parse_dates=['created_at', 'updated_at']
)

invoices = pd.read_sql_query(
    "select * from invoice", conn,
    parse_dates=['invoice_date', 'created_at', 'updated_at']
)

line_items = pd.read_sql_query(
    "select * from line_item", conn,
    parse_dates=['created_at', 'updated_at']
)

tickets = pd.read_sql_query(
    "select * from ticket", conn,
    parse_dates=['assigned_at', 'completed_at', 'created_at', 'updated_at']
)

users = pd.read_sql_query(
    "select * from user", conn,
    parse_dates=['created_at', 'updated_at']
)

vendor_users = pd.read_sql_query(
    "select * from vendor_user", conn,
    parse_dates=['created_at', 'updated_at']
)

vendor_wells = pd.read_sql_query(
    "select * from vendor_well", conn,
    parse_dates=['created_at', 'updated_at']
)

vendors = pd.read_sql_query(
    "select * from vendor", conn,
    parse_dates=['created_at', 'updated_at']
)

well_locations = pd.read_sql_query(
    "select * from well_location", conn,
    parse_dates=['created_at', 'updated_at']
)

wells = pd.read_sql_query(
    "select * from well", conn,
    parse_dates=['created_at', 'updated_at']
)

work_orders = pd.read_sql_query(
    "select * from work_orders", conn,
    parse_dates=['created_at', 'updated_at']
)

# vendor_contractors = pd.merge(vendors, contractors, on='vendor_id', suffixes=['_vendor', '_contractor'])

# contractor_count = vendor_contractors.groupby('company_name')['contractor_id'].count()
# print(contractor_count)

# vendor_work_orders = pd.merge(vendors, work_orders, left_on='vendor_id', right_on='assigned_vendor', suffixes=['_vendor', '_work_order'])
# vendor_work_order_count = vendor_work_orders.groupby('company_name')['work_order_id'].count().sort_values(ascending=False)
# print(vendor_work_order_count)

vendor_tickets = pd.merge(vendors, tickets, on='vendor_id', suffixes=['_vendor', '_ticket'])
# print(vendor_tickets.shape)
# vendor_tickets = vendor_tickets[vendor_tickets['completed_at'] >= pd.Timestamp.now() - pd.Timedelta(days=30)]
# print(vendor_tickets.shape)

# vendor_tickets['completion_time'] = vendor_tickets['completed_at'] - vendor_tickets['assigned_at']


# vendor_time_completion = vendor_tickets.groupby('company_name')['completion_time'].mean().sort_values(ascending=False)
# print(vendor_time_completion)
