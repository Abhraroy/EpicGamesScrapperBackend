# from fastapi import FastAPI,Depends,HTTPException
# import services,model,schemas
# from DB import engine,get_DB,create_table
# from sqlalchemy.orm import Session
# from contextlib import asynccontextmanager















# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     print("Server is starting up..")
#     create_table()
#     yield
#     print("app shutting down")




# app = FastAPI(lifespan=lifespan)




# @app.get("/")
# async def getHome():
#     return {"message":"Hello world"}

# @app.get("/get-free-games",response_model=list[schemas.GetFreeGame])
# def get_all_free_games(db:Session = Depends(get_DB)):
#     return services.get_game(db)


# @app.post("/add-free-games",response_model=list[schemas.GameCreate])
# def add_free_games(game:list[schemas.GameCreate],db:Session = Depends(get_DB)):
#     return [services.create_game(db,game) for game in game]

# @app.delete("/delete-all")
# def delete_all(db:Session=Depends(get_DB)):
#     try:
#         services.delete_games(db)
#         return {"message":"Deleted successfully"}
#     except:
#         return {"message":"Error happened while deleting"}
























from fastapi import FastAPI,Request
import services,schemas
from DB import get_supabase_client
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager














@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Server is starting up..")
    app.state.supabase = get_supabase_client()
    yield
    print("app shutting down")




app = FastAPI(lifespan=lifespan)




@app.get("/")
async def getHome():
    return {"message":"Hello world"}

@app.get("/get-free-games")
def get_all_free_games(request:Request):
    supabase = request.app.state.supabase
    return services.get_game(supabase)


@app.post("/add-free-games")
def add_free_games(game:list[schemas.GameCreate],request:Request):
    supabase = request.app.state.supabase
    return [services.create_game(game,supabase) for game in game]

@app.delete("/delete-all")
def delete_all(request:Request):
    try:
        supabase = request.app.state.supabase
        services.delete_games(supabase)
        return {"message":"Deleted successfully"}
    except:
        return {"message":"Error happened while deleting"}



