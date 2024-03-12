from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session


# Replace the connection details with your Oracle database information
oracle_username = 'PADMA_DMS'
oracle_password = 'Abc_123'
oracle_host = '192.168.200.135'
oracle_port = '1521'
oracle_service = 'TWODB'

# Create the connection string
oracle_connection_str = f"oracle+cx_oracle://{oracle_username}:{oracle_password}@{oracle_host}:{oracle_port}/{oracle_service}"

# Create the SQLAlchemy engine
engine = create_engine(oracle_connection_str)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session to be used in FastAPI endpoints
db_session = scoped_session(SessionLocal)

# Declare a base class for declarative models
Base = declarative_base()
Base.query = db_session.query_property()