from sqlalchemy import Column, Integer, String

from model import Preferences
from repository import Base
from repository.sqlalchemy import session


class PreferencesRepository(Base):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
