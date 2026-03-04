from database import engine, Base
from models import User, Role, Pool, Organization

Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully in TiDB Cloud")
