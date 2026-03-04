

from sqlalchemy.orm import Session
from model import *
from schemes import ProductCreate


def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db:Session, product_id:int, product:ProductCreate):
    db_product=get_product(db,product_id)
    if not db_product:
        return None

    db_product.name = product.name
    db_product.description=product.description
    db_product.price=product.price

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db:Session,product_id:int):
    db_product=get_product(db,product_id)
    if not db_product:
        None

    db.delete(db_product)
    db.commit()
    return db_product
