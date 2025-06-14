from pydantic import BaseModel,AnyHttpUrl

class GameDetail(BaseModel):
    Game_name:str
    Game_status:str
    Game_link:str
    Game_free_timeperiod:str


class GameCreate(GameDetail):
    pass


class GetFreeGame(GameDetail):
    pass
    class config:
        from_attributs=True