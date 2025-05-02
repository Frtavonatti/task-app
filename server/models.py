from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  full_name = Column(String)
  disabled = Column(Boolean, default=False)
  hashed_password = Column(String)
  

class Task(Base):
  __tablename__ = "tasks"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String)
  completed = Column(Boolean, default=False)
  tags = Column(String) # This should be a many-to-many relationship
  priority = Column(Integer, default=1)
  due_date = Column(String) # This should be a date type
  status = Column(String, default="pending")
  user_id = Column(Integer, ForeignKey("users.id"))

  

