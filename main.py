from fastapi import FastAPI
from user.user_api import user_router
from asks.ask_api import ask_router
from answers.answer_api import answer_router


from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url='/',
    title='Reddit Project'
)
app.include_router(user_router)
app.include_router(ask_router)
app.include_router(answer_router)

