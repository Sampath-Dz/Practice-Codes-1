from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    mobile = Column(String(15))
    password = Column(String(100))


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50))


class Pool(Base):
    __tablename__ = "pools"

    pool_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    parent_id = Column(Integer, ForeignKey("pools.pool_id"), nullable=True)

    # Self relationship (Parent → Children)
    children = relationship("Pool")


class Organization(Base):
    __tablename__ = "organizations"

    org_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    pool_id = Column(Integer, ForeignKey("pools.pool_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    role_id = Column(Integer, ForeignKey("roles.role_id"))
