import os
from sqlalchemy import create_engine

def db_connect_():
    """
    Connect to Zenith postgress database
    """
    # Load database credentials from environment variables
    db_username = os.getenv("dbuser")
    db_password = os.getenv("dbpassword")
    db_host = os.getenv("host2")
    db_port = os.getenv("dbport")  # Default PostgreSQL port
    db_name = os.getenv("dbname2")
    # Create a connection string
    engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
    return engine

def db_config_():
    # Load database credentials from environment variables
    user = os.getenv("dbuser")
    password = os.getenv("dbpassword")
    host = os.getenv("host")
    port = os.getenv("dbport")  # Default PostgreSQL port
    dbname = os.getenv("dbname2")
    return user,password,host,port,dbname

#user,password,host,port,dbname=db_config_()