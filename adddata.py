from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import database
import aesencrypter

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=10000, hmac_hash_module=SHA512)
def addData(mp, ds, sitename, siteurl, email, username):
    #getting the password
    password = getpass("Password: ")

    mk = computeMasterKey(mp, ds)

    encrypted = aesencrypter.encrypt(key=mk, source=password, keyType="bytes")

    #Add to database
    db = database()
    cursor = db.cursor()
    query = "INSERT INTO pm.entries(sitename varchar(100), siteurl varchar(100), email varchar(50), username(varchar(50)), password varchar(50)) values ('sitename', 'siteurl', 'email', 'username', 'encrypted')"
    db.commit()
    print(" Added entry ")
