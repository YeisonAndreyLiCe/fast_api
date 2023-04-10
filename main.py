from fastapi import Depends, FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
import movies
from movie import Movie
from typing import List
from jwt_manager import create_token
from user import User
from jwt_class import JWTBearer

app = FastAPI()
app.title = "My App"
app.version = "1.0.0"

@app.get("/", tags=["Home"])
def message():
    return {"message": "Hello World"}

@app.post("/login", tags=["Login"], response_model=dict)
def login(user: User):
    if user.email == "admin@fast.com":
        token: str = create_token({"email": user.email})
        return JSONResponse(status_code=200, content={"token": token})

@app.get("/movies", tags=["Movies"], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies.MOVIES)

@app.get("/movies/{movie_id}", tags=["Movies"], response_model=Movie)
def get_movie_by_id(movie_id: int = Path(..., gt=0)) -> Movie:
    for movie in movies.MOVIES.values():
        if movie["id"] == movie_id:
            return JSONResponse(content=movie)
    return JSONResponse(content={"movie_id": 'no_found'})

""" @app.get("/movies/", tags=["Movies"])
def get_movie_by_year(year: int):
    return [movie for movie in movies.MOVIES.values() if movie["year"] == year] """

@app.get("/movies/", tags=["Movies"], response_model=List[Movie], status_code=200)
def get_movies_by_year_and_category(year: int = Query(..., gt=1900, lt=2023),
                                   category: str = Query(..., min_length=1, max_length=100)) -> List[Movie]:
    response = [movie for movie in movies.MOVIES.values() if movie["year"] == year and movie["category"] == category]
    return JSONResponse(status_code=200, content=response)

@app.post("/movies/", tags=["Movies"], response_model=Movie, status_code=201)
def add_movie(movie: Movie):
    movies.MOVIES[movie.title] = movie.dict()
    return movies.MOVIES[movie.title]

@app.put("/movies/{movie_id}", tags=["Movies"], response_model=dict, status_code=200)
def update_movie(movie_id: int, movie: Movie) -> dict:
    for movie_ in movies.MOVIES.values():
        if movie_["id"] == movie_id:
            movie_ = movie
            return JSONResponse(status_code=200, content={"message": "movie modified"})
    return JSONResponse(status_code=404, content={"message": "movie not found"})

@app.delete("/movies/{movie_id}", tags=["Movies"], response_model=dict)
def delete_movie(movie_id: int) -> dict:
    for movie in movies.MOVIES.values():
        if movie["id"] == movie_id:
            del movies.MOVIES[movie["title"]]
            return {"message": f"Movie {movie_id} deleted"}
    return {"message": 'no_found'}