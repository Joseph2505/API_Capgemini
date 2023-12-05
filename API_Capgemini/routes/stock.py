from fastapi import APIRouter
from models.stock import Stock
from config.db import conn
from schemas.stock import stockEntity, stocksEntity
from fastapi import HTTPException
from pymongo.errors import OperationFailure

stock=APIRouter()

@stock.get('/{siret}')

async def find_one_stock(siret):
    try:
        result = stockEntity(conn.capgemini_db.capgemini_clt.find_one({"siret": int(siret)}))
        if result:
            return stockEntity(result)
        else:
            raise HTTPException(status_code=404, detail="Stock not found")
    except OperationFailure as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

@stock.post('/')
async def create_stock(stock: Stock):
    conn.capgemini_db.capgemini_clt.insert_one(dict(stock))
    return stocksEntity(conn.capgemini_db.capgemini_clt.find())

@stock.put('/{siret}')
async def update_stock(siret, stock: Stock):
    conn.capgemini_db.capgemini_clt.find_one_and_update({"siret": int(siret)}, {"$set": dict(stock)})
    return stockEntity(conn.capgemini_db.capgemini_clt.find_one({"siret": int(siret)}))

@stock.delete('/{siret}')
async def delete_stock(siret, stock: Stock):
    return stockEntity(conn.capgemini_db.capgemini_clt.find_one_and_delete({"siret": int(siret)}))