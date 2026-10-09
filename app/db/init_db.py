from app.database import Base, engine
import app.db.models


def init_db() -> None:
    Base.metadata.create_all(bind=engine)