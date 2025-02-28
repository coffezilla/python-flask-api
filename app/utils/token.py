# pip install PyJWT
import jwt
import datetime
import os


def generate_token(email):
    user = email,
    expiration_time = datetime.datetime.now(
        datetime.timezone.utc) + datetime.timedelta(minutes=30)

    token = jwt.encode({
        'user': user,
        "exp": expiration_time
    }, os.getenv('JWT_SECRET'), algorithm="HS256")

    # have a bug in the way expiration_time comes
    return {
        "token": token,
        "expiration": datetime.datetime.now(
            datetime.timezone.utc) + datetime.timedelta(minutes=-150)
    }
