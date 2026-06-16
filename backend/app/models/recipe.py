from sqlalchemy import Column, Integer, String, JSON, DateTime
from datetime import datetime
from app.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String)
    title = Column(String)
    cuisine = Column(String)
    difficulty = Column(String)

    recipe_json = Column(JSON)
    generated_json = Column(JSON)

    created_at = Column(DateTime, default=datetime.utcnow)