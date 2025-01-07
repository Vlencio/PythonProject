from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from databases import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    payments = relationship("Payment", back_populates="user")

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="payments")