import mysql.connector
import datetime


db = None
cursor = None


def connect_to_db():
    global db, cursor
    db = mysql.connector.connect(
        host="34.30.5.223",
        user="root",
        password="rippokefan",
        database="Equipo9",
    )

    cursor = db.cursor()


def insert_into_BMP280_table(pressure, temperature):
    if db == None:
        return

    sql = "INSERT INTO BMP280 (presion, temperatura, fecha) VALUES (%s, %s, %s)"
    values = (pressure, temperature, datetime.datetime.now().isoformat())
    cursor.execute(sql, values)
    db.commit()


def insert_into_HC_SR04_table(distance):
    if db == None:
        return

    sql = "INSERT INTO HC_SR04 (distancia, fecha) VALUES (%s, %s)"
    values = (distance, datetime.datetime.now().isoformat())
    cursor.execute(sql, values)
    db.commit()


def insert_into_GY_61_table(acc):
    if db == None:
        return

    sql = "INSERT INTO GY_61 (aceleracion, fecha) VALUES (%s, %s)"
    values = (acc, datetime.datetime.now().isoformat())
    cursor.execute(sql, values)
    db.commit()
