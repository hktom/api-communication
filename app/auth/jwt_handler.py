import time 
from datetime import datetime, timedelta
from jose import JWTError, jwt 
from fastapi import HTTPException, status 

SECRET_KEY : str  = 'xxd23l45MLD3455'
ALGORITHM : str = 'HS256' 
ACCESS_TOKEN_EXPIRES_MINUTES : int = 30 

# def create_access_token(data : dict, expires_delta: timedelta ) -> str : 
#     to_encode = data.copy() 
#     expire = datetime.utcnow() + expires_delta 
#     to_encode.update({'exp': expire }) 
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# def decode_access_token(token : str) -> str: 
#     try: 
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
#         return payload 
#     except JWTError: 
#         return None 


def create_access_token(user: str):
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def verify_access_token(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )
        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        )