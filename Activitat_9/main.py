import connection
import users_sch
import users


@app.get ("/users", response_model=List[dict])
async def read_users():
    return users_sch.user_schema(users.read())