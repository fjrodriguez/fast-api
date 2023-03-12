from fastapi import FastAPI
import model.books
from router.routes import router
from config.db import engine

model.books.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/book", tags=["book"])


