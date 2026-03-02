from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    mobile = Column(String(15))
    password = Column(String(100))


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50))


class Pool(Base):
    __tablename__ = "pools"

    pool_id = Column(Integer, primary_key=True)
    pool_name = Column(String(100))
    parent_id = Column(Integer, ForeignKey("pools.pool_id"), nullable=True)


class Organization(Base):
    __tablename__ = "organizations"

    org_id = Column(Integer, primary_key=True)
    org_name = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    role_id = Column(Integer, ForeignKey("roles.role_id"))
    pool_id = Column(Integer, ForeignKey("pools.pool_id"))