from database import SessionLocal
from models import User, Role, Pool, Organization

session = SessionLocal()

try:
    users = [
        User(name="Alice", email="alice@example.com", mobile="1234567890", password="pass1"),
        User(name="Bob", email="bob@example.com", mobile="2345678901", password="pass2"),
        User(name="Charlie", email="charlie@example.com", mobile="3456789012", password="pass3"),
    ]
    session.add_all(users)

    # ---------- Roles ----------
    roles = [
        Role(role_name="Admin"),
        Role(role_name="Manager"),
        Role(role_name="Developer"),
    ]
    session.add_all(roles)

    pool1 = Pool(name="Pool24", parent_id=None)   
    pool2 = Pool(name="Pool25", parent_id=None)   
    pool3 = Pool(name="Pool26", parent_id=None)   
    session.add_all([pool1, pool2, pool3])
    session.flush()  
    
    pool2.parent_id = pool1.pool_id  
    pool3.parent_id = pool2.pool_id  
    session.commit()

    organizations = [
        Organization(name="Org 1", pool_id=pool1.pool_id, user_id=users[0].user_id, role_id=roles[0].role_id),
        Organization(name="Org 2", pool_id=pool2.pool_id, user_id=users[1].user_id, role_id=roles[1].role_id),
        Organization(name="Org 3", pool_id=pool3.pool_id, user_id=users[2].user_id, role_id=roles[2].role_id),
    ]
    session.add_all(organizations)
    session.commit()

    print("✅ Sample data inserted successfully with exact nested pools and 3 rows per table")

except Exception as e:
    session.rollback()
    print("❌ Error:", e)
finally:
    session.close()
