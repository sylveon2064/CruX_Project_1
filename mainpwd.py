import hashlib
import secrets
from hashlib import sha256
from getpass import getpass
import random
import string
from database import database
def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))


def config():
    db = database()
    cursor = db.cursor()

    print("Creating new config")

    try:
        cursor.execute("CREATE DATABASE pm")
    
    except Exception as e:
        print("Error in database file",str(e))
    
    print("Database 'pm' created") 

    query = "CREATE TABLE pm.secrets (masterkey_hash varchar(255), device_key varchar(100))"
    res = cursor.execute(query)

    print("Table 'secrets' created")

    query = "CREATE TABLE pm.entries (sitename varchar(100), siteurl varchar(100), email varchar(50), username varchar(50), password varchar(50))"
    res = cursor.execute(query)

    print("Table entries created")

    while 1:
        mp = getpass("Input Master Password: ")
        if mp == getpass("Re-Type the Master Password:") and mp!="":
            break
        else :
            print("Please try again")
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    print("Main Password hashed successfully...")
    

    ds = generateDeviceSecret()
    print("device key generated")
    query = "INSERT INTO pm.secrets (masterkey_hash, device_key) values (%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val)
    db.commit()
    print("master password saved successfully")        
    
    db.close()
config()




 






        
            




       
    
