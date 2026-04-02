import uuid
import random
import csv
import os
from faker import Faker
from datetime import datetime

fake = Faker()

def gen_id():
    return str(uuid.uuid4())

def now():
    return datetime.now()

USER_TYPES = ["operator", "vendor", "contractor"]

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
            "created_by": user_id,  # self-created seed data
            "updated_by": user_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name()
        })
        
        # print(f"User: {i} created")

    return users


def main():
    users = generate_users(10)
    
    print(users)

if __name__ == "__main__":
    main()