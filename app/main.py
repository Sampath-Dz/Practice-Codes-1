from services import UserService, RoleService, PoolService, OrganizationService


# ---------------- USERS ----------------
user_service = UserService()

user_service.add_user("Sampath", "sampath@mail.com", "9999999999", "1234")
user_service.add_user("Ravi", "ravi@mail.com", "8888888888", "5678")
user_service.add_user("Sai", "sai@mail.com", "777777777", "6798")

print("\nUsers:")
for u in user_service.get_all():
    print(u.user_id, u.name)

user_service.close()


# ---------------- ROLES ----------------
role_service = RoleService()

role_service.add_role("Admin")
role_service.add_role("Manager")
role_service.add_role("Employee")

print("\nRoles:")
for r in role_service.get_all():
    print(r.role_id, r.role_name)

role_service.close()


# ---------------- POOLS (Parent → Child → Subchild) ----------------
pool_service = PoolService()

pool_service.add_pool("Main Pool")              # id = 1
pool_service.add_pool("Child Pool 1", 1)       # id = 2
pool_service.add_pool("Sub Child Pool", 2)     # id = 3

print("\nPools:")
for p in pool_service.get_all():
    print(p.pool_id, p.name, "Parent:", p.parent_id)

pool_service.close()


# ---------------- ORGANIZATIONS ----------------
org_service = OrganizationService()

org_service.add_org("Org A", 1, 1, 1)
org_service.add_org("Org B", 2, 2, 2)
org_service.add_org("Org C", 3, 1, 3)

print("\nOrganizations:")
for o in org_service.get_all():
    print(o.org_id, o.name, o.pool_id, o.user_id, o.role_id)

org_service.close()