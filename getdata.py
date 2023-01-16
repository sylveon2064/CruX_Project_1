from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import database
import aesencrypter
import pyperclip

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=10000, hmac_hash_module=SHA512)

def retrieveEntries(mp, ds, search, decryptPassword = False):
    db = database()
    cursor = db.cursor()

    query = ""

    if len(search) == 0:
        query = "SELECT * FROM pm.entries "
    else:
        query = "SELECT * FROM pm.entries WHERE "
        for i in search:
            query+=f"{i} = '{search[i]}' AND "
        query = query[:-5]
    cursor.execute(query)
    results = cursor.fetchall()

    if len(results) == 0:
        print("No results for the search")
        return

    if (decryptPassword and len(results)>1) or (not decryptPassword):
        print('Site name =', i[0])
        print('URL =', i[1])
        print('Email =', i[2])
        print('Username =', i[3])
        print('Password =', i[4])
    if len(results)==1 and decryptPassword:
        mk = computeMasterKey(mp, ds)
        decrypted = aesencrypter.decrypt(key=mk, source=results[0][4], keyType="bytes")

        pyperclip.copy(decrypted.decode())
        print("Password copied to clipboard")

    db.close()

