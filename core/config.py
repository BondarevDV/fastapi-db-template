from starlette.config import Config


config = Config(".env")

DATABASE_URL = config("GG_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("GG_SECRET_KEY", cast=str, default="47c99645b362584e80689f57fc051bf405338b38dd729886669260a330144e02")