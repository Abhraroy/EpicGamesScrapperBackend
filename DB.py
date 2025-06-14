from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Base import Base
from dotenv import load_dotenv
import os
import psycopg
import socket
from model import FreeGame


load_dotenv()
def force_ipv4_connect(*args, **kwargs):
    host = kwargs.get("host")
    if host:
        # Resolve to IPv4
        addrinfos = socket.getaddrinfo(host, None, socket.AF_INET)
        if addrinfos:
            ipv4_host = addrinfos[0][4][0]
            kwargs["host"] = ipv4_host
    return psycopg.connect(*args, **kwargs)

# DATABASE_URL = 'postgresql://postgres:abhra12@localhost:5432/Epic_Game_GameDetail'

# DATABASE_URL = 'postgresql+psycopg2://postgres.asszvxtgataryjgvlszh:Ce3oV7nlIz8MDEsf@aws-0-us-east-2.pooler.supabase.com:6543/postgres?sslmode=require'

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL,connect_args={"connection_factory": force_ipv4_connect})

sessionlocal = sessionmaker(autoflush=False,expire_on_commit=False,bind=engine)


def get_DB():
    db = sessionlocal()
    try:
        print("Database connected successfully-session established")
        yield db
    finally:
        db.close()


def create_table():
    print("Connected successfully")
    Base.metadata.create_all(bind=engine)



# if __name__ == "__main__":
#     create_table()