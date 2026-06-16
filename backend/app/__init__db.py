from app.database import Base, engine
from app.models.recipe import Recipe

def init_db():
    Base.metadata.create_all(bind=engine)