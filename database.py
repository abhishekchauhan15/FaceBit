from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import event
from core.config import settings
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the declarative base
Base = declarative_base()

# Ensure DATABASE_URL uses 'postgresql+asyncpg' for async handling
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Add event listener for successful connections
@event.listens_for(engine.sync_engine, "connect")
def receive_connect(dbapi_connection, connection_record):
    logger.info("Connected to database!")

# Add event listener for connection errors
@event.listens_for(engine.sync_engine, "handle_error")
def receive_error(context):
    logger.error(f"Database connection error: {context.original_exception}")

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    try:
        async with AsyncSessionLocal() as session:
            yield session
    except Exception as e:
        logger.error(f"Error creating database session: {e}")
        raise