from errno import ENOMSG
from importlib.metadata import metadata
from anyio import create_event
from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_URL


database = Database(DATABASE_URL)

metadata = MetaData()

engine = create_engine(
    DATABASE_URL,
)