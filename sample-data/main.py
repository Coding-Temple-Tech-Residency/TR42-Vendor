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
from werkzeug.security import generate_password_hash

Faker.seed(42)
random.seed(42)
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


def generate_time_span(sd="-1y", ed="now"):
    return fake.date_time_between(start_date=sd, end_date=ed)

def between(start, end):
    return fake.date_time_between(start_date=start, end_date=end)


def after(start, max_days=30):
    return fake.date_time_between(
        start_date=start,
        end_date=start + timedelta(days=max_days)
    )


USER_TYPES = ["OPERATOR", "VENDOR", "CONTRACTOR"]

VENDOR_STATUS = ["ACTIVE", "INACTIVE"]

COMPLIANCE_STATUS = ["EXPIRED", "INCOMPLETE", "COMPLETE"]

ROLE_OPTIONS = ["USER", "MANAGER", "ADMIN"]

CONTRACTOR_STATUS = ["ACTIVE", "INACTIVE"]

ORDER_STATUS = [
    "UNASSIGNED",
    "ASSIGNED",
    "IN_PROGRESS",
    "COMPLETED",
    "HALTED",
    "REJECTED",
    "CANCELLED",
    "CLOSED",
]

PRIORITY = ["LOW", "MEDIUM", "HIGH"]

TICKET_STATUS = [
    "UNASSIGNED",
    "ASSIGNED",
    "IN_PROGRESS",
    "COMPLETED",
]

INVOICE_STATUS = ["DRAFT", "SUBMITTED", "APPROVED", "REJECTED", "PAID"]

WELL_STATUS = [
    "ACTIVE",
    "DRILLING",
    "COMPLETED",
    "INACTIVE",
    "SUSPENDED",
    "ABANDONED",
    "PLUGGED",
]

WELL_TYPE = [
    "OIL",
    "GAS",
    "OIL_AND_GAS",
    "INJECTION",
    "WATER_DISPOSAL",
    "OBSERVATION",
]

LOCATION_TYPES = ["WELL", "GPS", "ADDRESS"]

FREQUENCY_TYPES = ["ONE_TIME", "DAILY", "WEEKLY", "MONTHLY"]

SERVICE_TYPES = [
    "WATER_DELIVERY",
    "CHEMICAL_DELIVERY",
    "INSPECTION",
    "ROUTINE_MAINTENANCE",
    "EQUIPMENT_REPAIR",
    "SITE_CLEANUP",
    "PIPELINE_SERVICE",
    "WELL_INTERVENTION",
]

DEFAULT_PASSWORD = "password"

def generate_users(n=20, addresses=None):
    users = []
    addresses = addresses or []

    for i in range(n):
        user_id = gen_id()
        address_id = random.choice(addresses)["address_id"] if addresses else None

        users.append(
            {
                "user_id": user_id,
                "username": fake.unique.user_name(),
                "password_hash": generate_password_hash(DEFAULT_PASSWORD),
                "email": fake.unique.email(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "middle_name": fake.first_name(),
                "contact_number": fake.phone_number(),
                "alternate_number": fake.phone_number(),
                "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=65),
                "ssn_last_four": fake.bothify("####"),
                "user_type": random.choice(USER_TYPES),
                "is_active": True,
                "is_admin": random.choice([True, False]),
                "profile_photo": None,
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by_user_id": user_id,
                "updated_by_user_id": user_id,
                "address_id": address_id,
            }
        )

    return users


def generate_addresses(n=30, users=[]):
    addresses = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]

        addresses.append(
            {
                "address_id": gen_id(),
                "street": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "zipcode": fake.zipcode(),
                "country": "US",
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by_user_id": creator,
                "updated_by_user_id": creator,
            }
        )

    return addresses


def generate_vendors(n=10, users=[], addresses=[]):
    vendors = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        address = random.choice(addresses)["address_id"]

        vendors.append(
            {
                "vendor_id": gen_id(),
                "company_name": fake.unique.company(),
                "company_code": fake.bothify(text="??-####"),
                "start_date": fake.date_time_between(start_date="-2y", end_date="-1y"),
                "end_date": None,
                "primary_contact_name": fake.name(),
                "company_email": fake.company_email(),
                "company_phone": fake.phone_number(),
                "service_type": "ANY",
                "status": random.choice(VENDOR_STATUS),
                "vendor_code": fake.bothify(text="VEND-####"),
                "onboarding": random.choice([True, False]),
                "compliance_status": random.choice(COMPLIANCE_STATUS),
                "description": fake.text(max_nb_chars=100),
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by_user_id": creator,
                "updated_by_user_id": updater,
                "address_id": address,
            }
        )

    return vendors


def generate_vendor_users(users, vendors, max_ratio=0.6):
    vendor_users = []

    if not users or not vendors:
        return vendor_users

    num_vendor_users = min(len(users), max(1, int(len(users) * max_ratio)))
    selected_users = random.sample(users, num_vendor_users)

    for user in selected_users:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        vendor = random.choice(vendors)

        # keep base user subtype aligned with membership table
        user["user_type"] = "VENDOR"

        vendor_users.append(
            {
                "id": gen_id(),
                "user_id": user["user_id"],
                "vendor_id": vendor["vendor_id"],
                "vendor_user_role": random.choices(ROLE_OPTIONS, weights=[80, 15, 5])[0],
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by_user_id": creator,
                "updated_by_user_id": updater,
            }
        )

    return vendor_users


def generate_contractors(n, vendors, users, vendor_users):
    contractors = []

    used_user_ids = {vu["user_id"] for vu in vendor_users}
    available_users = [u for u in users if u["user_id"] not in used_user_ids]

    if len(available_users) < n:
        raise ValueError("Not enough unique users to assign to contractors")

    # group vendor users by vendor so contractor.vendor_manager_id can point to vendor_user.id
    vendor_user_by_vendor = {}
    for vu in vendor_users:
        if vu["vendor_id"] is not None:
            vendor_user_by_vendor.setdefault(vu["vendor_id"], []).append(vu)

    valid_vendors = [v for v in vendors if v["vendor_id"] in vendor_user_by_vendor]
    if not valid_vendors:
        raise ValueError(
            "No vendors have vendor_user records. Contractors need a vendor_manager_id "
            "that references vendor_user.id."
        )

    selected_users = random.sample(available_users, n)

    for user in selected_users:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        vendor = random.choice(valid_vendors)
        manager = random.choice(vendor_user_by_vendor[vendor["vendor_id"]])

        # keep base user subtype aligned with membership table
        user["user_type"] = "CONTRACTOR"

        contractors.append(
            {
                "contractor_id": gen_id(),
                "employee_number": fake.unique.bothify("EMP####"),
                "user_id": user["user_id"],
                "vendor_id": vendor["vendor_id"],
                "vendor_manager_id": manager["id"],  # FK -> vendor_user.id
                "role": random.choice(ROLE_OPTIONS),
                "status": random.choice(CONTRACTOR_STATUS),
                "tickets_completed": 0,
                "tickets_open": 0,
                "biometric_enrolled": random.choice([True, False]),
                "is_onboarded": random.choice([True, False]),
                "is_subcontractor": random.choice([True, False]),
                "is_fte": random.choice([True, False]),
                "is_licensed": random.choice([True, False]),
                "is_insured": random.choice([True, False]),
                "is_certified": random.choice([True, False]),
                "average_rating": round(random.uniform(1, 5), 2),
                "years_experience": random.randint(0, 40),
                "background_check_id": None,
                "preferred_job_types": json.dumps([fake.job(), fake.job()]),
                "drug_test_id": None,
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

    return contractors

def update_contractor_ticket_counts(contractors, tickets):
    counts = {
        c["contractor_id"]: {"tickets_completed": 0, "tickets_open": 0}
        for c in contractors
    }

    for ticket in tickets:
        contractor_id = ticket.get("assigned_contractor")
        if not contractor_id or contractor_id not in counts:
            continue

        if ticket["status"] == "COMPLETED":
            counts[contractor_id]["tickets_completed"] += 1
        elif ticket["status"] in ["UNASSIGNED", "ASSIGNED", "IN_PROGRESS"]:
            counts[contractor_id]["tickets_open"] += 1

    for contractor in contractors:
        cid = contractor["contractor_id"]
        contractor["tickets_completed"] = counts[cid]["tickets_completed"]
        contractor["tickets_open"] = counts[cid]["tickets_open"]

def generate_work_orders(n, vendor_wells, users, wells, vendor_services):
    work_orders = []

    vendor_service_map = {}
    for vs in vendor_services:
        vendor_service_map.setdefault(vs["vendor_id"], []).append(vs["service_id"])

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        well = random.choice(wells)

        valid_vendor_ids = [
            vw["vendor_id"]
            for vw in vendor_wells
            if vw["well_id"] == well["well_id"]
        ]
        if not valid_vendor_ids:
            continue

        assigned_vendor = random.choice(valid_vendor_ids)
        valid_service_ids = vendor_service_map.get(assigned_vendor, [])
        if not valid_service_ids:
            continue

        service_type = random.choice(valid_service_ids)
        status = random.choice(ORDER_STATUS)

        created_at = generate_time_span("-2y", "-3d")
        assigned_at = None
        est_start = None
        est_end = None
        completed_at = None
        cancelled_at = None
        cancellation_reason = None

        if status != "UNASSIGNED":
            assigned_at = after(created_at, max_days=3)
            est_start = after(assigned_at, max_days=2)
            est_end = est_start + timedelta(days=random.randint(1, 5))

            if status in ["COMPLETED", "CLOSED"]:
                completed_at = after(est_end, max_days=2)
            elif status == "CANCELLED":
                cancelled_at = after(assigned_at, max_days=2)
                cancellation_reason = random.choice(
                    [
                        "Client cancelled request",
                        "Weather delay",
                        "Resource unavailable",
                        "Duplicate order",
                        "Safety concern",
                    ]
                )
        else:
            # still keep estimated dates even if not yet assigned
            est_start = after(created_at, max_days=5)
            est_end = est_start + timedelta(days=random.randint(1, 5))

        location_type = random.choice(LOCATION_TYPES)
        is_recurring = random.choice([True, False])
        recurrence_type = random.choice(FREQUENCY_TYPES) if is_recurring else None

        work_orders.append(
            {
                "work_order_id": gen_id(),
                "assigned_vendor": assigned_vendor,
                "client_id": well["client_id"],
                "assigned_at": assigned_at,
                "completed_at": completed_at,
                "description": fake.text(max_nb_chars=200),
                "estimated_start_date": est_start,
                "estimated_end_date": est_end,
                "current_status": status,
                "comments": fake.text(max_nb_chars=100),
                "location": fake.city(),
                "location_type": location_type,
                "latitude": float(fake.latitude()),
                "longitude": float(fake.longitude()),
                "estimated_cost": round(random.uniform(500, 50000), 2),
                "estimated_duration": timedelta(days=random.randint(1, 3)),
                "priority": random.choice(PRIORITY),
                "well_id": well["well_id"],
                "service_type": service_type,
                "estimated_quantity": round(random.uniform(1, 100), 2),
                "units": random.choice(["hours", "gallons", "loads", "visits", "days"]),
                "is_recurring": is_recurring,
                "recurrence_type": recurrence_type,
                "cancelled_at": cancelled_at,
                "cancellation_reason": cancellation_reason,
                "created_at": created_at,
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

    return work_orders


# TODO:
# continue working on making tickets realistic.
# - Add business hour limits for creation, assignment, and completion.
def generate_tickets(n, work_orders, contractors, users):
    tickets = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        wo = random.choice(work_orders)

        valid_contractors = [
            c for c in contractors if c["vendor_id"] == wo["assigned_vendor"]
        ]

        created_at = wo["created_at"]
        assigned_at = None
        start_time = None
        completed_at = None
        contractor_id = None

        if wo["current_status"] == "UNASSIGNED":
            status = "UNASSIGNED"
        else:
            if not valid_contractors:
                continue

            contractor = random.choice(valid_contractors)
            contractor_id = contractor["contractor_id"]

            created_at = wo["created_at"]

            if wo["current_status"] in ["COMPLETED", "CLOSED"]:
                status = "COMPLETED"
            elif wo["current_status"] == "IN_PROGRESS":
                status = random.choice(["ASSIGNED", "IN_PROGRESS"])
            elif wo["current_status"] == "ASSIGNED":
                status = "ASSIGNED"
            else:
                # cancelled / halted / rejected do not exist on ticket enum
                status = random.choice(["ASSIGNED", "IN_PROGRESS"])

            if wo["assigned_at"] is not None:
                assigned_at = between(created_at, wo["assigned_at"])
            else:
                assigned_at = after(created_at, max_days=2)

            if status in ["IN_PROGRESS", "COMPLETED"]:
                upper_bound = wo["estimated_start_date"] or (assigned_at + timedelta(days=1))
                start_time = between(assigned_at, upper_bound)

            if status == "COMPLETED":
                completion_upper = wo["completed_at"] or wo["estimated_end_date"] or (start_time + timedelta(days=1))
                completed_at = between(start_time, completion_upper)

        tickets.append(
            {
                "ticket_id": gen_id(),
                "work_order_id": wo["work_order_id"],
                "invoice_id": None,  # nullable FK -> invoice.invoice_id
                "description": wo["description"],
                "assigned_contractor": contractor_id,
                "priority": wo["priority"],
                "status": status,
                "vendor_id": wo["assigned_vendor"],
                "start_time": start_time,
                "due_date": wo["estimated_end_date"],
                "assigned_at": assigned_at,
                "completed_at": completed_at,
                "estimated_duration": wo["estimated_duration"],
                "service_type": wo["service_type"],
                "notes": fake.text(max_nb_chars=100),
                "contractor_start_location": (
                    f"{fake.latitude()},{fake.longitude()}" if contractor_id else None
                ),
                "contractor_end_location": (
                    f"{fake.latitude()},{fake.longitude()}" if contractor_id else None
                ),
                "estimated_quantity": round(random.uniform(1, 100), 2),
                "unit": random.choice(["hours", "gallons", "loads", "visits", "days"]),
                "special_requirements": fake.sentence(),
                "anomaly_flag": random.choice([True, False]),
                "anomaly_reason": fake.sentence() if random.choice([True, False]) else None,
                "created_at": created_at,
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
                "additional_information": json.dumps(
                    {
                        "source": "sample_generator",
                        "has_photo": random.choice([True, False]),
                    }
                ),
            }
        )

    return tickets


def generate_invoices(n, work_orders, tickets, users):
    invoices = []

    work_order_lookup = {wo["work_order_id"]: wo for wo in work_orders}

    eligible_tickets = [
        t for t in tickets
        if t["status"] == "COMPLETED"
        and t["vendor_id"] is not None
        and t["invoice_id"] is None
    ]

    if not eligible_tickets:
        return invoices

    selected_tickets = random.sample(eligible_tickets, min(n, len(eligible_tickets)))

    for ticket in selected_tickets:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        work_order = work_order_lookup[ticket["work_order_id"]]

        base_time = ticket["completed_at"] or ticket["created_at"] or now()
        invoice_date = after(base_time, max_days=10)
        due_date = after(invoice_date, max_days=30)
        invoice_status = random.choice(INVOICE_STATUS)

        approved_at = None
        paid_at = None
        rejected_at = None

        if invoice_status == "APPROVED":
            approved_at = after(invoice_date, max_days=10)
        elif invoice_status == "PAID":
            approved_at = after(invoice_date, max_days=10)
            paid_at = after(approved_at, max_days=20)
        elif invoice_status == "REJECTED":
            rejected_at = after(invoice_date, max_days=10)

        invoice_id = gen_id()

        invoices.append(
            {
                "invoice_id": invoice_id,
                "work_order_id": ticket["work_order_id"],
                "vendor_id": ticket["vendor_id"],
                "client_id": work_order["client_id"],
                "invoice_date": invoice_date,
                "due_date": due_date,
                "period_start": ticket["assigned_at"] or ticket["created_at"],
                "period_end": ticket["completed_at"] or invoice_date,
                "total_amount": 0,
                "invoice_status": invoice_status,
                "paid_at": paid_at,
                "approved_at": approved_at,
                "rejected_at": rejected_at,
                "created_at": now(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

        # relationship now lives on ticket.invoice_id
        ticket["invoice_id"] = invoice_id

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

            line_items.append(
                {
                    "line_item_id": gen_id(),
                    "invoice_id": invoice["invoice_id"],
                    "quantity": quantity,
                    "rate": rate,
                    "amount": amount,
                    "description": fake.sentence(),
                    "created_at": generate_time_span(),
                    "updated_at": now(),
                    "created_by": creator,
                    "updated_by": updater,
                }
            )

        
        invoice["total_amount"] = round(total, 2)

    return line_items


def generate_wells(n, users, clients):
    wells = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        client = random.choice(clients)

        spud_date = fake.date_time_between(start_date="-10y", end_date="-1y")
        completion_date = fake.date_time_between(start_date=spud_date, end_date="now")

        wells.append(
            {
                "well_id": gen_id(),
                "api_number": fake.bothify("##-###-#####"),
                "well_name": f"{fake.last_name()} {fake.random_letter()}-{random.randint(1, 99)}",
                "client_id": client["client_id"],
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
                "updated_by": updater,
            }
        )

    return wells

def generate_well_locations(wells, users):
    locations = []

    for well in wells:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        surface_lat = float(fake.latitude())
        surface_lon = float(fake.longitude())

        
        bottom_lat = surface_lat + random.uniform(-0.01, 0.01)
        bottom_lon = surface_lon + random.uniform(-0.01, 0.01)

        locations.append(
            {
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
                "updated_by": updater,
            }
        )

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

            vendor_wells.append(
                {
                    "id": gen_id(),
                    "vendor_id": vendor["vendor_id"],
                    "well_id": well["well_id"],
                    "created_at": generate_time_span(),
                    "updated_at": now(),
                    "created_by": creator,
                    "updated_by": updater,
                }
            )

            seen.add(key)

    return vendor_wells


def generate_contractor_performance(tickets, contractors, users):
    performance = []

    # optional: quick lookup for contractors
    contractor_lookup = {c["contractor_id"]: c for c in contractors}

    for ticket in tickets:
        
        if ticket["status"] != "COMPLETED":
            continue

        contractor_id = ticket["assigned_contractor"]

        
        if contractor_id not in contractor_lookup:
            continue

        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        performance.append(
            {
                "rating_id": gen_id(),
                "contractor_id": contractor_id,  
                "ticket_id": ticket["ticket_id"],  
                "rating": random.randint(1, 5),
                "comments": fake.sentence(),
                "created_at": now(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

    return performance


def generate_background_checks(contractors, users):
    checks = []

    for contractor in contractors:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        check_id = gen_id()

        checks.append(
            {
                "background_check_id": check_id,
                "background_check_passed": random.choice([True, False]),
                "background_check_date": fake.date_between(
                    start_date="-2y", end_date="today"
                ),
                "background_check_provider": fake.company(),
                "created_at": now(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

        
        contractor["background_check_id"] = check_id

    return checks


def generate_drug_tests(contractors, users):
    tests = []

    for contractor in contractors:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        test_id = gen_id()

        tests.append(
            {
                "drug_test_id": test_id,
                "drug_test_passed": random.choice([True, False]),
                "drug_test_date": fake.date_between(start_date="-1y", end_date="today"),
                "created_at": now(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

       
        contractor["drug_test_id"] = test_id

    return tests


def generate_licenses(contractors, vendors, users):
    licenses = []

    for contractor in contractors:
        num_licenses = random.randint(0, 3)

        for _ in range(num_licenses):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            verified = random.choice([True, False])

            licenses.append(
                {
                    "license_id": gen_id(),
                    "contractor_id": contractor["contractor_id"],
                    "license_type": random.choice(
                        ["Electrical", "Plumbing", "HVAC", "General"]
                    ),
                    "license_number": fake.bothify("LIC-#####"),
                    "license_state": fake.state_abbr(),
                    "license_expiration_date": fake.date_between(
                        start_date="today", end_date="+3y"
                    ),
                    "license_document_url": fake.url(),
                    "license_verified": verified,
                    "license_verified_by": (
                        random.choice(vendors)["vendor_id"] if verified else None
                    ),
                    "license_verified_at": (
                        fake.date_between(start_date="-1y", end_date="today")
                        if verified
                        else None
                    ),
                    "created_at": now(),
                    "updated_at": now(),
                    "created_by": creator,
                    "updated_by": updater,
                }
            )

    return licenses


def generate_certifications(contractors, users):
    certs = []

    for contractor in contractors:
        num_certs = random.randint(0, 3)

        for _ in range(num_certs):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            issue_date = fake.date_time_between(start_date="-5y", end_date="-1y")

            certs.append(
                {
                    "certification_id": gen_id(),
                    "contractor_id": contractor["contractor_id"],
                    "certification_name": random.choice(
                        ["OSHA 10", "OSHA 30", "First Aid", "Confined Space"]
                    ),
                    "certifying_body": fake.company(),
                    "certification_number": random.randint(10000, 99999),
                    "issue_date": issue_date,
                    "expiration_date": fake.date_time_between(
                        start_date="now", end_date="+3y"
                    ),
                    "certification_document_url": fake.url(),
                    "certification_verified": random.choice([True, False]),
                    "created_at": now(),
                    "updated_at": now(),
                    "created_by": creator,
                    "updated_by": updater,
                }
            )

    return certs


def generate_insurance(contractors, users):
    insurance_records = []

    for contractor in contractors:
        num_policies = random.randint(0, 2)

        for _ in range(num_policies):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            effective_date = fake.date_between(start_date="-2y", end_date="-1y")

            insurance_records.append(
                {
                    "insurance_id": gen_id(),
                    "contractor_id": contractor["contractor_id"],
                    "insurance_type": random.choice(
                        ["General Liability", "Workers Comp", "Auto"]
                    ),
                    "policy_number": random.randint(100000, 999999),
                    "provider_name": fake.company(),
                    "provider_phone": fake.phone_number(),
                    "coverage_amount": round(random.uniform(10000, 1000000), 2),
                    "deductible": round(random.uniform(500, 5000), 2),
                    "effective_date": effective_date,
                    "expiration_date": fake.date_between(
                        start_date="today", end_date="+2y"
                    ),
                    "insurance_document_url": fake.url(),
                    "insurance_verified": random.choice([True, False]),
                    "additional_insurance_required": random.choice([True, False]),
                    "additional_insured_certificate_url": fake.url(),
                    "created_at": now(),
                    "updated_at": now(),
                    "created_by": creator,
                    "updated_by": updater,
                }
            )

    return insurance_records

def generate_services(users):
    services = []

    for service_name in SERVICE_TYPES:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        services.append({
            "service_id": gen_id(),
            "service": service_name,
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater,
        })

    return services

def generate_clients(n, users, addresses):
    clients = []

    for _ in range(n):
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]
        address = random.choice(addresses)["address_id"]

        clients.append({
            "client_id": gen_id(),
            "client_name": fake.unique.company(),
            "client_code": fake.unique.bothify(text="CL-####"),
            "primary_contact_name": fake.name(),
            "contact_email": fake.company_email(),
            "contact_phone": fake.phone_number(),
            "created_at": generate_time_span(),
            "updated_at": now(),
            "created_by": creator,
            "updated_by": updater,
            "address_id": address,
        })

    return clients

def generate_client_users(users, clients, vendor_users, contractors, max_ratio=0.15):
    client_users = []

    vendor_user_ids = {vu["user_id"] for vu in vendor_users}
    contractor_user_ids = {c["user_id"] for c in contractors}
    unavailable_user_ids = vendor_user_ids | contractor_user_ids

    available_users = [u for u in users if u["user_id"] not in unavailable_user_ids]

    if not available_users or not clients:
        return client_users

    num_client_users = min(
        len(available_users),
        max(1, int(len(users) * max_ratio))
    )
    selected_users = random.sample(available_users, num_client_users)

    for user in selected_users:
        creator = random.choice(users)["user_id"]
        updater = random.choice(users)["user_id"]

        # client-side users line up best with operator in your current enum
        user["user_type"] = "OPERATOR"

        client_users.append(
            {
                "id": gen_id(),
                "user_id": user["user_id"],
                "client_id": random.choice(clients)["client_id"],
                "role": random.choice(ROLE_OPTIONS),
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            }
        )

    return client_users

def generate_client_vendors(clients, vendors, users):
    client_vendors = []
    seen = set()

    for client in clients:
        num_vendors = random.randint(1, min(4, len(vendors)))
        selected_vendors = random.sample(vendors, num_vendors)

        for vendor in selected_vendors:
            key = (client["client_id"], vendor["vendor_id"])
            if key in seen:
                continue

            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            client_vendors.append({
                "client_vendor_id": gen_id(),
                "client_id": client["client_id"],
                "vendor_id": vendor["vendor_id"],
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            })

            seen.add(key)

    return client_vendors

def generate_compliance_documents(vendors, users):
    compliance_docs = []

    for vendor in vendors:
        num_docs = random.randint(1, 3)

        for _ in range(num_docs):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            is_compliant = random.choice([True, True, True, False])

            compliance_docs.append({
                "compliance_id": gen_id(),
                "vendor_id": vendor["vendor_id"],
                "compliance_document": None,  # blob placeholder
                "compliance_status": is_compliant,
                "expiration_date": fake.date_between(start_date="today", end_date="+3y") if is_compliant else fake.date_between(start_date="-1y", end_date="+6m"),
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            })

    return compliance_docs

def generate_msas(vendors, users):
    msas = []

    for vendor in vendors:
        num_versions = random.randint(1, 3)

        base_date = fake.date_between(start_date="-5y", end_date="-1y")

        for version_num in range(1, num_versions + 1):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]
            uploader = random.choice(users)["user_id"]

            effective_date = base_date + timedelta(days=(version_num - 1) * 365)
            expiration_date = effective_date + timedelta(days=365)

            status = "active" if version_num == num_versions else random.choice(["expired", "terminated"])

            msas.append({
                "msa_id": gen_id(),
                "vendor_id": vendor["vendor_id"],
                "version": f"v{version_num}.0",
                "effective_date": effective_date,
                "expiration_date": expiration_date,
                "status": status,
                "uploaded_by": uploader,
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            })

    return msas

def generate_msa_requirements(msas, users):
    requirement_categories = ["Insurance", "Safety", "Licensing", "Training", "Reporting"]
    rule_types = ["minimum", "maximum", "required", "conditional"]

    requirements = []

    for msa in msas:
        num_requirements = random.randint(3, 8)

        for _ in range(num_requirements):
            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            requirements.append({
                "id": gen_id(),
                "msa_id": msa["msa_id"],
                "category": random.choice(requirement_categories),
                "rule_type": random.choice(rule_types),
                "description": fake.sentence(),
                "value": str(random.randint(1, 100)),
                "unit": random.choice(["days", "hours", "USD", "count", "%"]),
                "source_field_id": fake.bothify(text="SRC-#####"),
                "page_number": random.randint(1, 50),
                "extracted_text": fake.text(max_nb_chars=150),
                "confidence_score": round(random.uniform(0.70, 0.99), 2),
                "metadata": json.dumps({
                    "source": "parsed_msa",
                    "reviewed": random.choice([True, False])
                }),
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            })

    return requirements

# def generate_cancelled_work_orders(work_orders, users):
#     cancelled = []

#     cancellable_work_orders = [
#         wo for wo in work_orders
#         if wo["current_status"] in ["unassigned", "assigned", "in progress"]
#     ]

#     selected_work_orders = random.sample(
#         cancellable_work_orders,
#         k=min(len(cancellable_work_orders), max(1, int(len(work_orders) * 0.08)))
#     ) if cancellable_work_orders else []

#     for wo in selected_work_orders:
#         creator = random.choice(users)["user_id"]
#         updater = random.choice(users)["user_id"]

#         cancelled.append({
#             "id": gen_id(),
#             "work_order_id": wo["work_order_id"],
#             "vendor_id": wo["assigned_vendor"],
#             "cancellation_reason": random.choice([
#                 "Client cancelled request",
#                 "Weather delay",
#                 "Resource unavailable",
#                 "Duplicate order",
#                 "Safety concern",
#             ]),
#             "created_at": generate_time_span(),
#             "updated_at": now(),
#             "created_by": creator,
#             "updated_by": updater,
#         })

#     return cancelled

def generate_vendor_services(vendors, services, users):
    vendor_services = []
    seen = set()

    for vendor in vendors:
        num_services = random.randint(1, min(5, len(services)))
        selected_services = random.sample(services, num_services)

        for service in selected_services:
            key = (vendor["vendor_id"], service["service_id"])
            if key in seen:
                continue

            creator = random.choice(users)["user_id"]
            updater = random.choice(users)["user_id"]

            vendor_services.append({
                "id": gen_id(),
                "vendor_id": vendor["vendor_id"],
                "service_id": service["service_id"],
                "created_at": generate_time_span(),
                "updated_at": now(),
                "created_by": creator,
                "updated_by": updater,
            })

            seen.add(key)

    return vendor_services

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
    # create addresses first so users can reference them
    system_users = generate_users(5)
    addresses = generate_addresses(30, system_users)

    users = generate_users(500, addresses)
    vendors = generate_vendors(10, users, addresses)

    clients = generate_clients(25, users, addresses)

    services = generate_services(users)
    vendor_services = generate_vendor_services(vendors, services, users)

    vendor_users = generate_vendor_users(users, vendors, max_ratio=0.3)

    contractors = generate_contractors(
        n=100,
        vendors=vendors,
        users=users,
        vendor_users=vendor_users,
    )

    client_users = generate_client_users(
        users, clients, vendor_users, contractors, max_ratio=0.1
    )
    client_vendors = generate_client_vendors(clients, vendors, users)

    wells = generate_wells(50, users, clients)
    well_locations = generate_well_locations(wells, users)
    vendor_wells = generate_vendor_wells(vendors, wells, users)

    work_orders = generate_work_orders(
        1000, vendor_wells, users, wells, vendor_services
    )
    tickets = generate_tickets(5000, work_orders, contractors, users)

    update_contractor_ticket_counts(contractors, tickets)

    invoices = generate_invoices(500, work_orders, tickets, users)
    line_items = generate_line_items(invoices, users)

    contractor_performance = generate_contractor_performance(
        tickets, contractors, users
    )

    background_checks = generate_background_checks(contractors, users)
    drug_tests = generate_drug_tests(contractors, users)
    licenses = generate_licenses(contractors, vendors, users)
    certifications = generate_certifications(contractors, users)
    insurance = generate_insurance(contractors, users)

    compliance_documents = generate_compliance_documents(vendors, users)

    msas = generate_msas(vendors, users)
    msa_requirements = generate_msa_requirements(msas, users)

    data = {
        "user": users,
        "address": addresses,
        "client": clients,
        "vendor": vendors,
        "client_user": client_users,
        "vendor_user": vendor_users,
        "client_vendor": client_vendors,
        "contractors": contractors,
        "background_check": background_checks,
        "drug_test": drug_tests,
        "licenses": licenses,
        "certifications": certifications,
        "insurance": insurance,
        "compliance_document": compliance_documents,
        "msa": msas,
        "msa_requirements": msa_requirements,
        "services": services,
        "vendor_services": vendor_services,
        "well": wells,
        "well_location": well_locations,
        "vendor_well": vendor_wells,
        "work_orders": work_orders,
        "ticket": tickets,
        "invoice": invoices,
        "line_item": line_items,
        "contractor_performance": contractor_performance,
    }

    export_to_csv(data)

if __name__ == "__main__":
    main()
