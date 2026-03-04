from fastapi import FastAPI, APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

import crud
from database import SessionLocal
from schemes import ProductResponse, ProductCreate

router=APIRouter(prefix='/products,',tags=['Products'])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@router.get("/", response_model=list[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_one(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product topilmadi")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    updated=crud.update_product(db,product_id,product)
    if not updated:
        raise HTTPException(status_code=404, detail='mahsulot topilmadi')
    return {'messege':'product changed'}


@router.delete('/{product_id',response_model=ProductResponse)
def delete(product_id:int,product:ProductCreate,db:Session=Depends(get_db)):
    deleted=crud.delete_product(db,product_id,product)
    if not deleted:
        raise HTTPException(status_code=404, detail='mahsulot topilmadi')
    return {'mail':'ochirildi'}


