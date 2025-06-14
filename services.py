# from model import FreeGame
# from sqlalchemy.orm import Session

# def create_game(db:Session,data:GameCreate):
#     Game_instance = FreeGame(**data.model_dump())
#     db.add(Game_instance)
#     db.commit()
#     db.refresh(Game_instance)
#     return Game_instance


# def get_game(db:Session):
#     return db.query(FreeGame).all()

# def delete_games(db:Session):
#     try:
#         db.query(FreeGame).delete(synchronize_session=False)
#         db.commit()
#         return {"message": "All games deleted (or none existed)."}
#     except Exception as e:
#         db.rollback()
#         raise Exception(f"Deletion failed: {str(e)}")




from schemas import GameCreate

def create_game(data:GameCreate,supabase)->GameCreate:
    response = supabase.table("Free_Games").insert(data.model_dump()).execute()
    return response.data


def get_game(supabase):
    response = supabase.table("Free_Games").select("*").execute()
    return response.data



def delete_games(supabase):
    try:
        response = supabase.table("Free_Games").delete().neq("Game_name", "").execute()
        return {"message": "All games deleted (or none existed)."}
    except Exception as e:
        raise Exception(f"Deletion failed : {str(e)}")

