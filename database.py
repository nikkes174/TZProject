from datetime import datetime

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.automap import automap_base
from config import Base, engine, session, close_session

Base.metadata.create_all(engine)

class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement = True)
    user_name = Column(String, nullable=False)
    start_subscription = Column(Date, nullable=False)
    end_subscription = Column(Date, nullable=False)
    period_subscription = Column(Integer, nullable=False)

Base.metadata.create_all(engine)
Base = automap_base()
Base.prepare(autoload_with=engine)


CLIENTS = Base.classes.clients

class ActionWithClients:
    def __init__(self):
        self.session = session
        self.close_session = close_session



    def add_client(
            self,
            client_id: int,
            user_name: str,
            start_subscription:,
            end_subscription,
            period_subscription: int

    ):
        new_client = CLIENTS(
            client_id=client_id,
            user_name=user_name,
            start_subscription=start_subscription,
            end_subscription=end_subscription,
            period_subscription=period_subscription
        )
        self.session.add(new_client)
        self.session.commit()

    def get_end_date_subscription(self, client_id):
        try:
            client = self.session.query(CLIENTS).filter_by(client_id=client_id).first()

            if client in None:
                raise ValueError(f'Такого клиента нет')

            return client.end_subscription

        except ValueError as ve:
            print(ve)
            return None
        self.session.close()

    def get_all_clients(self):

        all_clients = self.session.query(CLIENTS.user_name).all()

        if all_clients:
            clent_name = ','.join([client[0] for client in all_clients])
            return f'Полный список клиентов {clent_name}'


        self.session.close()
        print('Список клиентов пуст')

    def update_start_subscription(self, client_id):

        new_date = datetime.now().date()

        client = self.session.query(CLIENTS).filter_by(client_id=client_id).first()

        if client:
            client.start_subscription = new_date
            self.session.commit()
            print('Дата начала подписки обновлена')

        else:
            self.close_session

            print('Клиент не найден')

        self.close_session













