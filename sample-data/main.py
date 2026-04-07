"""
These are just for creating sample data based on current ERD
Changes to fields are expected in the future. 
"""


import uuid
import random
import csv
import os
from faker import Faker
from datetime import datetime, timedelta
import json

fake = Faker()

def gen_id():
    return str(uuid.uuid4())

def now():
    return datetime.now()

def add_n_days(n):
    one_day = timedelta(days=1)
    return one_day * n

def add_n_hours(n):
    one_day = timedelta(hours=1)
    return one_day * n

def generate_time_span(sd='-1y', ed='now'):
    return fake.date_time_between(start_date=sd, end_date=ed)

USER_TYPES = ["operator", "vendor", "contractor"]
VENDOR_STATUS = ["active", "inactive"]
COMPLIANCE_STATUS = ["expired", "incomplete", "complete"]
ROLE_OPTIONS = ["user", "manager", "admin"]
CONTRACTOR_STATUS = ["active", "inactive"]
ORDER_STATUS = ["unassigned", "assigned", "in progress", "completed"]
PRIORITY = ["routine", "urgent", "emergency"]
TICKET_STATUS = ["assigned", "in progress", "completed"] # need to add unassigned status
INVOICE_STATUS = ["draft", "submitted", "approved", "paid", "rejected"]
WELL_STATUS = ["active", "inactive", "plugged", "drilling"]
WELL_TYPE = ["oil", "gas", "injection", "disposal"]

def generate_users(n=20):
    users = []

    for i in range(n):
        user_id = gen_id()

        users.append({
            "user_id": user_id,
            "username": fake.unique.user_name(),
            "password": fake.password(length=12),  # bcrypt.hashpw(default_password, salt),
            "email": fake.unique.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.first_name(),
            "contact_number": fake.phone_number(),
            "alternate_number": fake.phone_number(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=65),
            "ssn_last_four": fake.bothify("####"),
            "type": random.choice(USER_TYPES),
            "is_active": True,
            "is_admin": random.choice([True, False]),
            "profile_photo": None,
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": user_id,  # may need to change to be created_by the system
            "updated_by": user_id, # may need to change to be updated_by the system to begin
        })
        
        # print(f"User: {i} created")

    return users

def generate_addresses(n=30, users=[]):
    addresses = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]

        addresses.append({
            "address_id": gen_id(),
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip": fake.zipcode(),
            "country": "US",
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": creator
        })

    return addresses

def generate_vendors(n=10, users=[], addresses=[]):
    vendors = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        address = random.choice(addresses)["address_id"]

        vendors.append({
            "vendor_id": gen_id(),
            "company_name": fake.unique.company(),
            "company_code": fake.bothify(text="??-####"),
            "start_date": fake.date_time_between(start_date='-2y', end_date='-1y'),
            "end_date": None,
            "primary_contact_name": fake.name(),
            "contact_email": fake.company_email(),
            "contact_phone": fake.phone_number(),
            "status": random.choice(VENDOR_STATUS),
            "vendor_code": fake.bothify(text="VEND-####"),
            "onboarding": random.choice([True, False]),
            "compliance_status": random.choice(COMPLIANCE_STATUS),
            "description": fake.text(max_nb_chars=100),
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater,
            "address_id": address
        })

    return vendors

def generate_vendor_users(users, vendors, max_ratio=0.6):
    vendor_users = []

    num_vendor_users = int(len(users) * max_ratio) # limits the number of users that can be "vendor_users". 
    selected_users = random.sample(users, num_vendor_users)

    for user in selected_users:
        creator = random.choice(users)["user_id"]

        vendor_users.append({
            "id": gen_id(),
            "user_id": user["user_id"],
            "vendor_id": random.choice(vendors)["vendor_id"],
            "role": random.choices(ROLE_OPTIONS, [80, 15, 5])[0],
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": creator
        })

    return vendor_users

def generate_contractors(n, vendors, users, addresses, vendor_users):
    contractors = []

    # ❗ avoid reusing users already tied to vendor_user
    used_user_ids = {vu["user_id"] for vu in vendor_users}
    available_users = [u for u in users if u["user_id"] not in used_user_ids]

    if len(available_users) < n:
        raise ValueError("Not enough unique users to assign to contractors")

    selected_users = random.sample(available_users, n)

    for user in selected_users:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        vendor = random.choice(vendors)

        contractors.append({
            "contractor_id": gen_id(),
            "employee_number": fake.bothify("EMP####"),
            "vendor_id": vendor["vendor_id"],
            "vendor_manager_id": random.choice(users)["user_id"],
            "user_id": user["user_id"],  
            "role": random.choice(ROLE_OPTIONS),
            "status": random.choice(CONTRACTOR_STATUS),
            "biometric_enrolled": random.choice([True, False]),
            "is_onboarded": random.choice([True, False]),
            "is_subcontractor": random.choice([True, False]),
            "is_fte": random.choice([True, False]),
            "is_licensed": random.choice([True, False]),
            "is_insured": random.choice([True, False]),
            "is_certified": random.choice([True, False]),
            "address_id": random.choice(addresses)["address_id"],
            "average_rating": round(random.uniform(1, 5), 2),
            "years_experience": random.randint(0, 40),
            "background_check_id": None,
            "preferred_job_types": json.dumps([fake.job(), fake.job()]),
            "drug_test_id": None,
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return contractors

def generate_work_orders(n, vendor_wells, users, wells):
    work_orders = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        well = random.choice(wells)
        valid_vendor_ids = [
            vw["vendor_id"]
            for vw in vendor_wells
            if vw["well_id"] == well["well_id"]
        ]

        assigned_vendor = random.choice(valid_vendor_ids)
        created_at = generate_time_span()

        work_orders.append({
            "work_order_id": gen_id(),
            "assigned_vendor": assigned_vendor,
            "assigned_at": generate_time_span(created_at),
            "completed_at": None, # Need to figure out way of calcualting this with tickets
            "description": fake.text(max_nb_chars=200),
            "due_date": generate_time_span(created_at, '+7d'),
            "current_status": random.choice(ORDER_STATUS),
            "comments": fake.text(max_nb_chars=100),
            "location": fake.city(),
            "estimated_cost": round(random.uniform(100, 10000), 2),
            "estimated_duration": random.randint(1, 72),  # hours
            "priority": random.choice(PRIORITY),
            "well_id": well["well_id"],
            "created_at": created_at,
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return work_orders

# TODO: 
# continue working on making tickets realistic. 
# - Add business hour limits for creation, assignment, and completion. 
# - maybe utilize estimated_duration for difference between start_time and completed_at 
def generate_tickets(n, work_orders, contractors, vendors, users):
    tickets = []

    for _ in range(n):
        
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        wo = random.choice(work_orders)
        contractor = random.choice(contractors)
        
        status = random.choice(TICKET_STATUS)
        created_at = generate_time_span()
        assigned_at = generate_time_span(created_at, created_at + add_n_days(2))
        estimated_duration = random.randint(1, 24)
        
        start_time = generate_time_span(sd=assigned_at, ed=assigned_at+add_n_days(3))
        completed_at = fake.date_time_between(start_date=start_time, end_date=start_time + add_n_hours(estimated_duration)) if status=='completed' else None
        due_date = generate_time_span(sd=created_at+add_n_days(5), ed=created_at+add_n_days(15))
        tickets.append({
            "ticket_id": gen_id(),
            "work_order_id": wo["work_order_id"],
            "description": fake.text(max_nb_chars=200),
            "assigned_contractor": contractor["contractor_id"],
            "priority": random.choice(PRIORITY),
            "status": status,
            "vendor_id": contractor["vendor_id"],  # keep consistent
            "start_time": start_time,
            "due_date": due_date,
            "assigned_at": assigned_at,
            "completed_at": completed_at,
            "estimated_duration": estimated_duration,
            "notes": fake.text(max_nb_chars=100),
            "contractor_start_location": f"{fake.latitude()},{fake.longitude()}",
            "contractor_end_location": f"{fake.latitude()},{fake.longitude()}",
            "estimated_quantity": random.randint(1, 100),
            "unit": "hours",
            "special_requirements": fake.sentence(),
            "anomaly_flag": random.choice([True, False]),
            "anomaly_reason": fake.sentence() if random.choice([True, False]) else None,
            "created_at": created_at,
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater,
            "additional_information": fake.json()
        })

    return tickets

def generate_invoices(n, work_orders, tickets, users):
    invoices = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        ticket = random.choice(tickets)

        invoice_date = fake.date_time_between(start_date='-30d', end_date='now')
        due_date = fake.date_time_between(start_date=invoice_date, end_date='+30d')

        invoices.append({
            "invoice_id": gen_id(),
            "work_order_id": ticket["work_order_id"],  
            "ticket_id": ticket["ticket_id"],          
            "vendor_id": ticket["vendor_id"],          
            "invoice_date": invoice_date,
            "due_date": due_date,
            "period_start": fake.date_time_between(start_date='-60d', end_date=invoice_date),
            "period_end": invoice_date,
            "total_amount": 0,  # will update after line items
            "invoice_status": random.choice(INVOICE_STATUS),
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return invoices

def generate_line_items(invoices, users):
    line_items = []

    for invoice in invoices:
        num_items = random.randint(1, 5)
        total = 0

        for _ in range(num_items):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            quantity = random.randint(1, 20)
            rate = round(random.uniform(50, 500), 2)
            amount = round(quantity * rate, 2)

            total += amount

            line_items.append({
                "line_item_id": gen_id(),
                "invoice_id": invoice["invoice_id"],
                "quantity": quantity,
                "rate": rate,
                "amount": amount,
                "description": fake.sentence(),
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater
            })

        # ✅ update invoice total AFTER items are created
        invoice["total_amount"] = round(total, 2)

    return line_items



def generate_wells(n, users):
    wells = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        spud_date = fake.date_time_between(start_date='-10y', end_date='-1y')
        completion_date = fake.date_time_between(start_date=spud_date, end_date='now')

        wells.append({
            "well_id": gen_id(),
            "api_number": fake.bothify("##-###-#####"),
            "well_name": f"{fake.last_name()} {fake.random_letter()}-{random.randint(1, 99)}",
            "operator": random.randint(1000, 9999),  # could later FK to company table
            "status": random.choice(WELL_STATUS),
            "type": random.choice(WELL_TYPE),
            "range": fake.bothify("##"),
            "quarter": random.choice(["NE", "NW", "SE", "SW"]),
            "ground_elevation": random.randint(1000, 8000),
            "total_depth": random.randint(2000, 20000),
            "geofence_radius": random.randint(50, 500),
            "spud_date": spud_date,
            "completion_date": completion_date,
            "access_instructions": fake.sentence(),
            "safety_notes": fake.sentence(),
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return wells

def generate_well_locations(wells, users):
    locations = []

    for well in wells:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        surface_lat = float(fake.latitude())
        surface_lon = float(fake.longitude())

        # simulate slight deviation for bottom hole
        bottom_lat = surface_lat + random.uniform(-0.01, 0.01)
        bottom_lon = surface_lon + random.uniform(-0.01, 0.01)

        locations.append({
            "well_location_id": gen_id(),
            "well_id": well["well_id"],
            "surface_latitude": surface_lat,
            "surface_longitude": surface_lon,
            "bottom_latitude": bottom_lat,
            "bottom_longitude": bottom_lon,
            "county": fake.city(),
            "state": fake.state_abbr(),
            "field_name": fake.word().capitalize() + " Field",
            "section": random.randint(1, 36),
            "township": fake.bothify("##"),
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return locations

def generate_vendor_wells(vendors, wells, users):
    vendor_wells = []
    seen = set()

    for well in wells:
        num_vendors = random.randint(1, 3)
        selected_vendors = random.sample(vendors, num_vendors)

        for vendor in selected_vendors:
            key = (vendor["vendor_id"], well["well_id"])
            if key in seen:
                continue

            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            vendor_wells.append({
                "id": gen_id(),
                "vendor_id": vendor["vendor_id"],
                "well_id": well["well_id"],
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater
            })

            seen.add(key)

    return vendor_wells

def generate_contractor_performance(tickets, contractors, users):
    performance = []

    # optional: quick lookup for contractors
    contractor_lookup = {
        c["contractor_id"]: c for c in contractors
    }

    for ticket in tickets:
        # ✅ only rate completed work
        if ticket["status"] != "completed":
            continue

        contractor_id = ticket["assigned_contractor"]

        # safety check (should always pass if your data is good)
        if contractor_id not in contractor_lookup:
            continue

        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        performance.append({
            "rating_id": gen_id(),
            "contractor_id": contractor_id,   # ✅ tied to ticket
            "ticket_id": ticket["ticket_id"], # ✅ correct FK
            "rating": random.randint(1, 5),
            "comments": fake.sentence(),
            "created_at": now(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return performance

def serialize(value):
    if isinstance(value, datetime):
        return value.isoformat()
    return value


def export_to_csv(data_dict, folder="data"):
    os.makedirs(folder, exist_ok=True)

    for table_name, records in data_dict.items():
        if not records:
            continue

        file_path = os.path.join(folder, f"{table_name}.csv")
        headers = records[0].keys()

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for row in records:
                writer.writerow({k: serialize(v) for k, v in row.items()})

        print(f"✅ {table_name} exported to {file_path}")

def main():
    users = generate_users(1000)
    addresses = generate_addresses(30, users)
    vendors = generate_vendors(10, users, addresses)
    vendor_users = generate_vendor_users(users, vendors, max_ratio=0.3)
    
    contractors = generate_contractors(
        n=200,
        vendors=vendors,
        users=users,
        addresses=addresses,
        vendor_users=vendor_users 
    )
    
    wells = generate_wells(50, users)
    well_locations = generate_well_locations(wells, users)
    vendor_wells = generate_vendor_wells(vendors, wells, users)
    
    work_orders = generate_work_orders(1000, vendor_wells, users, wells)
    tickets = generate_tickets(5000, work_orders, contractors, vendors, users)
    
    invoices = generate_invoices(300, work_orders, tickets, users)
    line_items = generate_line_items(invoices, users)
    
    contractor_performance = generate_contractor_performance(
        tickets,
        contractors,
        users
    )
    
    
    data = {
        "user": users,
        "address": addresses,
        "vendor": vendors,
        "vendor_user": vendor_users,
        "contractors": contractors,
        "well": wells,                    
        "well_location": well_locations,   
        "vendor_well": vendor_wells,       
        "work_orders": work_orders,
        "ticket": tickets,
        "invoice": invoices,
        "line_item": line_items,
        "contractor_performance": contractor_performance
    }

    export_to_csv(data)

if __name__ == "__main__":
    main()