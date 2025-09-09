from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI(title="JWT Authentication")

# Clave secreta para firmar los tokens (mantener segura)
SECRET_KEY = "$2y$10$yTz1VWL.f8qVF.eNJ6T9ZOXDLXmT5G9czqxHAATfOL6kY5H9d7L12" #12345
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2

# Simulación de base de datos de usuarios
fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "Administrador",
        "email": "admin@example.com",
        "password": "admin123",
        "hashed_password": "$2b$12$QyA5mTxWVOeFqMfE5peQ.e5ENXZODjHjElrDBNwKcZn8y3lq5JwX2", # Contraseña: "admin123"
    }
}

# Sistema de autenticación con OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para verificar contraseñas
def verify_password(plain_password, hashed_password):
    print(plain_password, hashed_password)
    if(plain_password == hashed_password):
        return True
    return False

# Función para obtener un usuario de la "base de datos"
def get_user(username: str):
    user = fake_users_db.get(username)
    if user:
        return user
    return None

# Función para generar el token JWT
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.get("/")
async def root():
    return {"message": "Endpoint Inicial de la API"}

# Endpoint para generar token (Login)
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint protegido con JWT
@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    user = get_user(username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")

    return {"username": user["username"], "full_name": user["full_name"] ,"email": user["email"]}