import pandas as pd
import sqlite3

conn = sqlite3.connect("./my_database.db")

addresses = pd.read_sql_query("select * from address", conn)
contractors = pd.read_sql_query("select * from contractors", conn)
invoices = pd.read_sql_query("select * from invoice", conn)
line_items = pd.read_sql_query("select * from line_item", conn)
tickets = pd.read_sql_query("select * from ticket", conn)
users = pd.read_sql_query("select * from user", conn)
vendor_users = pd.read_sql_query("select * from vendor_user", conn)
vendor_wells = pd.read_sql_query("select * from vendor_well", conn)
vendors = pd.read_sql_query("select * from vendor", conn)
well_locations = pd.read_sql_query("select * from well_location", conn)
wells = pd.read_sql_query("select * from well", conn)
work_orders = pd.read_sql_query("select * from work_orders", conn)

vendor_contractors = pd.merge(vendors, contractors, on='vendor_id', suffixes=['_vendor', '_contractor'])

contractor_count = vendor_contractors.groupby('company_name')['contractor_id'].count()
print(contractor_count)

vendor_work_orders = pd.merge(vendors, work_orders, left_on='vendor_id', right_on='assigned_vendor', suffixes=['_vendor', '_work_order'])
vendor_work_order_count = vendor_work_orders.groupby('company_name')['work_order_id'].count().sort_values(ascending=False)
print(vendor_work_order_count)