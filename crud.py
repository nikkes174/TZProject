from datetime import datetime

from sqlalchemy.orm import Session

import models
import schemas


def add_client(db: Session, client: schemas.ClientCreate):
    new_client = models.Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def get_start_date_subscription(db: Session, client_id: int):
    client = (
        db.query(models.Client)
        .filter(models.Client.client_id == client_id)
        .first()
    )
    return client.start_subscription if client else None


def get_all_clients(db: Session):
    return db.query(models.Client).all()


def update_end_subscription(db: Session, client_id: int):
    client = (
        db.query(models.Client)
        .filter(models.Client.client_id == client_id)
        .first()
    )
    if client:
        client.end_subscription = datetime.now().date()
        db.commit()
        db.refresh(client)
    return client


def delete_client(db: Session, client_id: int):
    client = (
        db.query(models.Client)
        .filter(models.Client.client_id == client_id)
        .first()
    )
    if client:
        db.delete(client)
        db.commit()
    return client
