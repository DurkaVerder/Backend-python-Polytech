from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Message": "Hello, World!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"Message": f"Hello, {name}!"}

@app.get("/search/{query}")
def search(query: str):
    return {"Message": f"You searched for: {query}"}

@app.get("/json")
def about_me():
    return {"name": "Timur", "age": 20, "hobby": "Playing guitar"}

@app.get("/file")
def file():
    file_path = "text.txt"
    try:
        return FileResponse(path=file_path, filename="text.txt", media_type="text/plain")
    except FileNotFoundError:
        return {"error": "File not found"}

@app.get("/redirect")
def redirect():
    return RedirectResponse(url="/")

@app.get("/headers")
def headers(request: Request):
    return dict(request.headers)

@app.get("/set_cookie")
def set_cookie():
    response = JSONResponse(content={"Message": "Cookie set"})
    response.set_cookie(key="username", value="Timur")
    return response

@app.get("/get_cookie")
def get_cookie(request: Request):
    username = request.cookies.get("username")
    if username:
        return {"Message": f"Cookie value: {username}"}
    else:
        return {"Message": "No cookie found"}

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: UserLogin):
    if user.username:
        return {"Message": f"Welcome {user.username}"}
    else:
        return {"Message": "Invalid credentials"}

class UserRegister(BaseModel):
    username: str
    password: str
    email: str

@app.post("/register")
def register(user: UserRegister):
    if user.username and user.email:
        return {"Message": f"User {user.username} registered successfully!"}
    else:
        return {"Message": "Invalid registration details"}

class User:
    def __init__(self, id: int, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email, "password": self.password}

users = [
    User(1, "Timur", "timur@example.com", "securepassword").to_dict(),
    User(2, "Alex", "alex@mail.ru", "1234").to_dict()
]

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    return user or {"Message": "User not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
