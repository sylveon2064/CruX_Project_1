import mysql.connector
import requests
def database():
    try:
        db = mysql.connector.connect (
        host='localhost',
        user='root',
        passwd='Amr20062004'
        )
        return db
        
    except:
        print("Error in database file")




        

