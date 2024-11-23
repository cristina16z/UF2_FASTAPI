def user_schema(user) -> dict:
    return {"id": user[0],
            "name": user[1],
            "surname": user[2],
            "email": user[3],
            "age": user[4],
            "sex": user[5]
    }

def users_schema(users) -> dict:
    return [user_schema(user) for user in users]