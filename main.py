from database import SessionLocal
from models import User

db = SessionLocal()

# 1️⃣ ADD NEW USER
new_user = User(
    name="Sampath",
    email="sampath3@gmail.com",
    mobile="7777777777",
    password="sampath@123"
)

db.add(new_user)
db.commit()

print("✅ New user added\n")

# 2️⃣ READ ALL USERS
users = db.query(User).all()

print("📌 Users Table Data:")
for u in users:
    print(u.user_id, u.name, u.email, u.mobile, u.password)

db.close()