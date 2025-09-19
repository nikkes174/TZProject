from sqlalchemy import Column, Date, Integer, String

from database import Base


class Client(Base):
    __tablename__ = "clients_tz"

    client_id = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    user_name = Column(String, nullable=False)
    start_subscription = Column(Date, nullable=False)
    end_subscription = Column(Date, nullable=False)
    period_subscription = Column(Integer, nullable=False)
