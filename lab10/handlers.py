from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db, User, Post, create_tables

app = FastAPI(title="Lab 9")

templates = Jinja2Templates(directory="templates")

create_tables()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users", response_class=HTMLResponse)
async def list_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("users_list.html", {"request": request, "users": users})

@app.get("/users/create", response_class=HTMLResponse)
async def create_user_form(request: Request):
    return templates.TemplateResponse("user_create.html", {"request": request})

@app.post("/users/create")
async def create_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким username или email уже существует")
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)

@app.get("/users/{user_id}/edit", response_class=HTMLResponse)
async def edit_user_form(user_id: int, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return templates.TemplateResponse("user_edit.html", {"request": request, "user": user})

@app.post("/users/{user_id}/edit")
async def edit_user(
    user_id: int,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    existing_user = db.query(User).filter(
        (User.username == username) | (User.email == email),
        User.id != user_id
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким username или email уже существует")
    user.username = username
    user.email = email
    user.password = password
    db.commit()
    return RedirectResponse(url="/users", status_code=303)

@app.post("/users/{user_id}/delete")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    db.delete(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)

@app.get("/posts", response_class=HTMLResponse)
async def list_posts(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).join(User).all()
    return templates.TemplateResponse("posts_list.html", {"request": request, "posts": posts})

@app.get("/posts/create", response_class=HTMLResponse)
async def create_post_form(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("post_create.html", {"request": request, "users": users})

@app.post("/posts/create")
async def create_post(
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="Пользователь не найден")
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)

@app.get("/posts/{post_id}/edit", response_class=HTMLResponse)
async def edit_post_form(post_id: int, request: Request, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Пост не найден")
    users = db.query(User).all()
    return templates.TemplateResponse("post_edit.html", {"request": request, "post": post, "users": users})

@app.post("/posts/{post_id}/edit")
async def edit_post(
    post_id: int,
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Пост не найден")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="Пользователь не найден")
    post.title = title
    post.content = content
    post.user_id = user_id
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)

@app.post("/posts/{post_id}/delete")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Пост не найден")
    db.delete(post)
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)