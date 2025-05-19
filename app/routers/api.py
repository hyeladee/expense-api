from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/api", tags=["API"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.get("/categories/", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

@router.get("/expenses/", response_model=list[schemas.Expense])
def read_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)