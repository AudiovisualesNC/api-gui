from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from classes.Token import Token
from methods import token
from methods import user
from database import rooms

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    result = user.authenticate_user(form_data.username, form_data.password)
    if not result:
        raise token.HTTPException(
            status_code=token.status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = token.create_access_token(data={"sub": result["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/rooms")
async def get_inventory_rooms(token: str = Depends(oauth2_scheme)):
    return rooms.get_all_rooms()
