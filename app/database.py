from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

USERNAME = "1bav1XU7FHg7DMZ.root"
PASSWORD = "o9ykHR6wPwgNZ39z"
HOST = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"
PORT = 4000
DATABASE = "my_db"

SSL_CA = r"C:\tidb_python_project\tidb-serverless-ca.pem"

DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {"ca": SSL_CA}}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

print("✅ Connected to TiDB Cloud")
