from database import engine, Base
from models import User, Role, Pool, Organization

# This line creates all tables in TiDB Cloud if they don't exist
Base.metadata.create_all(bind=engine)

print("✅ All tables created in TiDB Cloud")