import argparse
import hashlib
from getpass import getpass
import database
import adddata
import getdata
import pyperclip

parser = argparse.ArgumentParser(description='Description')

parser.add_argument('option', help='(a)dd / (e)xtract ')
parser.add_argument("-s", "--name", help="Site name")
parser.add_argument("-u", "--url", help="Site URL")
parser.add_argument("-e", "--email", help="Email")
parser.add_argument("-l", "--login", help="Username")
parser.add_argument("-c", "--copy", action='store_true', help='Copy password to clipboard')

args = parser.parse_args()

def inputAndValidateMasterPassword():
	mp = getpass("MASTER PASSWORD: ")
	hashed_mp = hashlib.sha256(mp.encode()).hexdigest()

	db = database.database()
	cursor = db.cursor()
	query= " SELECT * FROM pm.secrets"

	cursor.execute(query)

	result = cursor.fetchall()[0]
	if hashed_mp != result[0]:
		print("please try again")
		return None

	return [mp,result[1]]


def main():
	if args.option in ["add","a"]:
		if args.name == None or args.url == None or args.login == None:
			if args.name == None:
				print("Site Name (-s) required ")
			if args.url == None:
				print("Site URL (-u) required ")
			if args.login == None:
				print("Site Login (-l) required ")
			return

		if args.email == None:
			args.email = ""

		res = inputAndValidateMasterPassword()
		if res is not None:
			adddata.addEntry(res[0],res[1],args.name,args.url,args.email,args.login)


	if args.option in ["extract","e"]:
		res = inputAndValidateMasterPassword()

		search = {}
		if args.name is not None:
			search["sitename"] = args.name
		if args.url is not None:
			search["siteurl"] = args.url
		if args.email is not None:
			search["email"] = args.email
		if args.login is not None:
			search["username"] = args.login

		if res is not None:
			getdata.retrieveEntries(res[0],res[1],search,decryptPassword = args.copy)

main()
