from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

db_config = {
    "host": "34.30.5.223",
    "user": "root",
    "password": "PASSWORD",
    "database": "Equipo9",
}


app = FastAPI()

origins = [
    "*",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
    mydb = mysql.connector.connect(**db_config)
except:
    print("Error connecting to db")


@app.get("/")
async def root():
    return "CAR-9 API"


@app.get("/BMP280")
async def root():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM BMP280")
        rows = mycursor.fetchall()  #

        response = {"temp": [], "press": []}

        for row in rows:
            response["press"].append({"id": row[0], "value": row[1], "date": row[3]})
            response["temp"].append({"id": row[0], "value": row[2], "date": row[3]})

        return response

    except:
        return JSONResponse(content="Error getting data from DB", status_code=500)


@app.get("/HC_SR04")
async def root():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM HC_SR04")
        rows = mycursor.fetchall()

        response = []

        for row in rows:
            response.append({"id": row[0], "value": row[1], "date": row[2]})

        return response

    except:
        return JSONResponse(content="Error getting data from DB", status_code=500)


@app.get("/GY_61")
async def root():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM GY_61")
        rows = mycursor.fetchall()

        response = []

        for row in rows:
            response.append({"id": row[0], "value": row[1], "date": row[2]})

        return response

    except:
        return JSONResponse(content="Error getting data from DB", status_code=500)
