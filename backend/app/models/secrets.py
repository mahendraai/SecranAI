from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Secret(Base):
    __tablename__ = 'secrets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    value = Column(Text, nullable=False)
    created_at = Column(Integer, nullable=False)  # Timestamp for when the secret was created
    updated_at = Column(Integer, nullable=False)  # Timestamp for when the secret was last updated

    def __repr__(self):
        return f"<Secret(name={self.name}, value={self.value})>"