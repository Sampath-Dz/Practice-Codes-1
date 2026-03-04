from database import SessionLocal
from models import User, Role, Pool, Organization


class BaseService:
    def __init__(self):
        self.db = SessionLocal()

    def close(self):
        self.db.close()


# ---------------- USERS ----------------
class UserService(BaseService):

    def add_user(self, name, email, mobile, password):
        user = User(name=name, email=email, mobile=mobile, password=password)
        self.db.add(user)
        self.db.commit()

    def get_all(self):
        return self.db.query(User).all()


# ---------------- ROLES ----------------
class RoleService(BaseService):

    def add_role(self, role_name):
        role = Role(role_name=role_name)
        self.db.add(role)
        self.db.commit()

    def get_all(self):
        return self.db.query(Role).all()


# ---------------- POOLS ----------------
class PoolService(BaseService):

    def add_pool(self, name, parent_id=None):
        pool = Pool(name=name, parent_id=parent_id)
        self.db.add(pool)
        self.db.commit()

    def get_all(self):
        return self.db.query(Pool).all()


# ---------------- ORGANIZATIONS ----------------
class OrganizationService(BaseService):

    def add_org(self, name, pool_id, user_id, role_id):
        org = Organization(
            name=name,
            pool_id=pool_id,
            user_id=user_id,
            role_id=role_id
        )
        self.db.add(org)
        self.db.commit()

    def get_all(self):
        return self.db.query(Organization).all()