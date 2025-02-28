import jwt
import datetime
import os


def generate_token(email):
    user = email
    # Access token expiration time (30 minutes)
    access_expiration_time = datetime.datetime.now(
        datetime.timezone.utc) + datetime.timedelta(minutes=30)

    # Refresh token expiration time (7 days, for example)
    refresh_expiration_time = datetime.datetime.now(
        datetime.timezone.utc) + datetime.timedelta(days=7)

    # Generate access token
    access_token = jwt.encode({
        'user': user,
        'exp': int(access_expiration_time.timestamp())  # Convert to integer
    }, os.getenv('JWT_SECRET'), algorithm="HS256")

    # Generate refresh token
    refresh_token = jwt.encode({
        'user': user,
        'exp': int(refresh_expiration_time.timestamp())  # Convert to integer
    }, os.getenv('JWT_SECRET'), algorithm="HS256")

    return {
        "access_token": access_token,
        "access_expiration": access_expiration_time.strftime('%Y-%m-%d %H:%M:%S'),
        "refresh_token": refresh_token,
        "refresh_expiration": refresh_expiration_time.strftime('%Y-%m-%d %H:%M:%S')
    }
