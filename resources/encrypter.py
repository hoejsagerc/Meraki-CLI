"""
    NAME
        encrypter.py
    CREATED
        31.01.2021
    DESCRIPTITON
        This file contains the methods for managing the userdatabase and
        password encryptions
    UPDATED
        31.01.2021

"""


import base64
import sqlite3
import bcrypt
import time
import getpass
import stdiomask
from sqlite3 import Error
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

__all__ = ['create_connection', 'create_table', 'create_user', 'read_api_key']



def create_connection(db_file):
    """ Create a database connection to a database file """

    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)
    
    finally:
        if conn:
            conn.close()


def create_table(db_file):
    """ Create the table for the databse """

    conn = sqlite3.connect(db_file)
    c = conn.cursor()


    c.execute(""" CREATE TABLE IF NOT EXISTS users (
            username text,
            password text,
            pass_salt text,
            api_key text,
            api_salt text
    )""")

    conn.commit()
    conn.close()



def create_user(db_file):
    username = input("Please enter username: ")
    pass_from_user = stdiomask.getpass(prompt='Please enter password: ')
    second_pass_from_user = stdiomask.getpass(prompt='Please enter password: ')
    if pass_from_user == second_pass_from_user:

        api_key_input  = input("Please enter api_key: ")

        hash_salt = bcrypt.gensalt()
        hash_salt_ascii = hash_salt.decode("utf-8")
        

        hashed = bcrypt.hashpw(pass_from_user.encode('utf-8'), hash_salt)
        ascii_hash = hashed.decode("utf-8")

        password = pass_from_user.encode()
        api_key = api_key_input.encode()

        mysalt = bcrypt.gensalt()
        mysalt_ascii = mysalt.decode("utf-8")

        kdf = PBKDF2HMAC (
            algorithm=hashes.SHA256,
            length=32,
            salt=mysalt,
            iterations=10000,
            backend=default_backend()
        )    

        key = base64.urlsafe_b64encode(kdf.derive(password))

        crypter = Fernet(key)
        encrypt_api = crypter.encrypt(api_key)
        ascii_encrypt_api = encrypt_api.decode("utf-8")
            
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        c.execute(f"INSERT INTO users VALUES ('{username}', '{ascii_hash}', '{hash_salt_ascii}', '{ascii_encrypt_api}', '{mysalt_ascii}')")
        
        sql_query_check = """SELECT username FROM users WHERE username = ?"""
        c.execute(sql_query_check, (username,))
        fetch_user = c.fetchone()
        user = str(fetch_user).strip("()")
        user = user[:-1].strip("'")
        
        if user == username:
            print("")
            print("-------------------------------------------")
            print("User was created succesfully!")
        else:
            print("An error occured user was not created...")

        time.sleep(2)

        conn.commit()
        conn.close
    
    else:
        print("The passwords did not match...")
        time.sleep(2)
        return None




def read_api_key(db_file):
    username = input("Username: ")
    pass_from_user = stdiomask.getpass(prompt='Password: ')
    password = pass_from_user.encode()

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    sql_query_pw_hash = """SELECT pass_salt FROM users WHERE username = ?"""
    c.execute(sql_query_pw_hash, (username,))
    hash_salt_decoded = c.fetchone()
    fetch_salt = str(hash_salt_decoded).strip("()")
    hash_salt = fetch_salt[:-1].strip("'")

    hashed = bcrypt.hashpw(pass_from_user.encode('utf-8'), hash_salt.encode("utf-8"))

    sql_query = """SELECT password FROM users WHERE username = ?"""
    c.execute(sql_query, (username,))
    hashed_pw = c.fetchone()
    fetched_pw = str(hashed_pw).strip("()")
    fetched_pw = fetched_pw[:-1].strip("'")


    if hashed == bytes(fetched_pw, 'utf-8'):
        sql_query = """SELECT api_key FROM users WHERE username = ?"""
        c.execute(sql_query, (username,))
        hashed_api = c.fetchone()
        fetched_api = str(hashed_api).strip("()")
        fetched_api = fetched_api[:-1].strip("'")

        sql_query_api_hash = """SELECT api_salt FROM users WHERE username = ?"""
        c.execute(sql_query_api_hash, (username,))
        hashed_api_salt = c.fetchone()
        fetch_api_salt = str(hashed_api_salt).strip("()")
        mysalt = fetch_api_salt[:-1].strip("'")

        kdf = PBKDF2HMAC (
            algorithm=hashes.SHA256,
            length=32,
            salt=mysalt.encode('utf-8'),
            iterations=10000,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))

        crypter = Fernet(key)
        decrypt_string = crypter.decrypt(fetched_api.encode('utf-8'))
        api_key = decrypt_string.decode()

        return api_key
        
    else:
        print("Password or Username was incorrect...")



