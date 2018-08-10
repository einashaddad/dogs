from sqlalchemy import Column, Integer, String

from repository import Base

class UserRepository(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
