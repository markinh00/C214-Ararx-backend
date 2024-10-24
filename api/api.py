
from api.helpers.mongo_instance import mongo
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from api.routes import test, register, login, post, user, follow

# Passa o gerenciador de ciclo de vida para o FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test.router)
app.include_router(register.router)
app.include_router(login.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(follow.router)


@app.get("/")
def read_root():
    return
