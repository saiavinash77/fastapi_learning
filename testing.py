from fastapi import FastAPI
from pydantic import BaseModel  #Pydantic is mainly for data validation 

app = FastAPI()

user_db ={
    1:{"name":"Sai","Age":19},
    2:{"name":"Thalli","Age":21},
    3:{"name":"Thaswi","Age":12}
}
class User(BaseModel):
    name : str
    age :int

@app.put("/user_db/data/update/{user_id}")
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message":"User Updated Successfully","User":user_db[user_id]}
    return {"message": "User Not Found"}


@app.delete("/users_db/users/data/delete/{user_id}")
def delete(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"message":"User deleted successfully"}
    return {"mesaage":"User Not found ...."}

    
