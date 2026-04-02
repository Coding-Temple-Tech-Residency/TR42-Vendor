"""
These are just for creating sample data based on current ERD
Changes to fields are expected in the future. 
"""


import uuid
import random
import csv
import os
from faker import Faker
from datetime import datetime
import json

fake = Faker()

def gen_id():
    return str(uuid.uuid4())

def now():
    return datetime.now()

USER_TYPES = ["operator", "vendor", "contractor"]
VENDOR_STATUS = ["active", "inactive"]
COMPLIANCE_STATUS = ["expired", "incomplete", "complete"]
ROLE_OPTIONS = ["user", "manager", "admin"]
CONTRACTOR_STATUS = ["active", "inactive"]
ORDER_STATUS = ["unassigned", "assigned", "in progress", "completed"]
PRIORITY = ["routine", "urgent", "emergency"]
TICKET_STATUS = ["assigned", "in progress", "completed"]

def generate_users(n=20):
    users = []

    for i in range(n):
        user_id = gen_id()

        users.append({
            "user_id": user_id,
            "username": fake.unique.user_name(),
            "password": fake.password(length=12),  # bcrypt.hashpw(default_password, salt),
            "email": fake.unique.email(),
            "type": random.choice(USER_TYPES),
            "is_active": True,
            "is_admin": random.choice([True, False]),
            "profile_photo": None,
            "created_at": now(),
            "updated_at": now(),
            "created_by": user_id,  # may need to change to be created_by the system
            "updated_by": user_id, # may need to change to be updated_by the system to begin
            "first_name": fake.first_name(),
            "last_name": fake.last_name()
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
            "created_at": now(),
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
            "created_at": now(),
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
            "created_at": now(),
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
            "first_name": user["first_name"],  # keep consistent with user
            "last_name": user["last_name"], # keep consistent with user
            "middle_name": fake.first_name(),
            "contact_number": fake.phone_number(),
            "alternate_number": fake.phone_number(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=65),
            "ssn_last_four": fake.bothify("####"),
            "email": user["email"],  # keep consistent
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
            "created_at": now(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return contractors

def generate_work_orders(n, vendors, users):
    work_orders = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        assigned_vendor = random.choice(vendors)["vendor_id"]

        work_orders.append({
            "work_order_id": gen_id(),
            "assigned_vendor": assigned_vendor,
            "assigned_at": now(),
            "completed_at": None,
            "description": fake.text(max_nb_chars=200),
            "due_date": fake.date_time_between(start_date='now', end_date='+30d'),
            "current_status": random.choice(ORDER_STATUS),
            "comments": fake.text(max_nb_chars=100),
            "location": fake.city(),
            "estimated_cost": round(random.uniform(100, 10000), 2),
            "estimated_duration": random.randint(1, 72),  # hours
            "priority": random.choice(PRIORITY),
            "well_id": None,  # optional for now
            "created_at": now(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return work_orders

def generate_tickets(n, work_orders, contractors, vendors, users):
    tickets = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        wo = random.choice(work_orders)
        contractor = random.choice(contractors)

        tickets.append({
            "ticket_id": gen_id(),
            "work_order_id": wo["work_order_id"],
            "description": fake.text(max_nb_chars=200),
            "assigned_contractor": contractor["contractor_id"],
            "priority": random.choice(PRIORITY),
            "status": random.choice(TICKET_STATUS),
            "vendor_id": contractor["vendor_id"],  # keep consistent
            "start_date": now(),
            "due_date": fake.date_time_between(start_date='now', end_date='+10d'),
            "estimated_duration": random.randint(1, 24),
            "notes": fake.text(max_nb_chars=100),
            "contractor_start_location": f"{fake.latitude()},{fake.longitude()}",
            "contractor_end_location": f"{fake.latitude()},{fake.longitude()}",
            "estimated_quantity": random.randint(1, 100),
            "unit": "hours",
            "special_requirements": fake.sentence(),
            "anomaly_flag": random.choice([True, False]),
            "anomaly_reason": fake.sentence() if random.choice([True, False]) else None,
            "created_at": now(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater
        })

    return tickets

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
    
    work_orders = generate_work_orders(50, vendors, users)
    tickets = generate_tickets(200, work_orders, contractors, vendors, users)
    
    data = {
        "user": users,
        "address": addresses,
        "vendor": vendors,
        "vendor_user": vendor_users,
        "contractors": contractors,
        "work_orders": work_orders,
        "ticket": tickets
    }

    export_to_csv(data)

if __name__ == "__main__":
    main()