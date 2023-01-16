
# Python Password Manager

This project helps you store your userID and passwords for different sites at one place.

This CLI project has been made using Python and mySQL(for database). It uses pbkdf2 to get a 256bit
Master Password and Device Key to use with AES-256 for encrypting and decrypting.

This project also uses pyperclip(for copying password to clipboard), and pycryptodome(for encrypting and decrypting data).




## User Guide

1.You need to make a Master Password by first running the mainpwd.py file. This can be done only once (However, if you want to make a new Master Password you can do so by clearing database in the SQL
workbench although it will erase all your previously stored data).

2.Now for the main project you can do 2 types of tasks in this project - 

  i) Adding Data - 

                   (1)Run the the file pm.py in terminal.

                   (2)Input >python pm.py add -s "Site Name" -u "URL" -e "E-Mail ID" -l "Username" 

                   (3)Enter your Master Password

                   (4)Input the password of the site

     In this way, you will be able to add data to the program.

 ii) Extracting All Data -
 
                            (1)Run the file pm.py in terminal

                            (2)Input >python pm.py e

                            (3)Input the Master Password

      In this way, you can extract all the data stored in the Password Manager.

iii) Extracting Data with a specific Site Name -

                                                   (1)Run the file pm.py in terminal

                                                   (2)Input >python pm.py e/extract -s "Site Name"

                                                   (3)Enter the Master Password

      In this way, you can view all the data stored for one particular Site Name.

 iv) Copying the Password - 
 
                           (1)Run the file pm.py in terminal

                           (2)Input >python pm.py e/extract -s "Site Name" -u "URL" -e "E-Mail ID" -l "Username" -c

                           (3)Enter the Master Password

        You will able to view a statement saying Password copied to clipboard
