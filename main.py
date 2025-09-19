import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

app = FastAPI()


@app.post("/clients/", response_model=schemas.ClientResponse)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.add_client(db, client)


@app.get("/clients/", response_model=list[schemas.ClientResponse])
def read_clients(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return crud.get_all_clients(db)[skip : skip + limit]


@app.put("/clients/{client_id}", response_model=schemas.ClientResponse)
def update_client(client_id: int, db: Session = Depends(get_db)):
    updated_client = crud.update_end_subscription(db, client_id)
    if not updated_client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    return updated_client


@app.get("/clients/{client_id}", response_model=schemas.ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    return db_client

@app.delete("/clients/{client_id}", response_model=schemas.ClientResponse)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_client(db, client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    return deleted


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
