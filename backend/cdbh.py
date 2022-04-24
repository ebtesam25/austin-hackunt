from dataclasses import field
import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
import csv
from turtle import pu
# import pymongo
import psycopg2
from psycopg2.errors import SerializationFailure
import json

def create_users(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, embed VARCHAR(4000), name VARCHAR(30))"
        )
        cur.execute("UPSERT INTO users (id, embed, name) VALUES (1, '-----------------', 'jon stewart'), (2, '---------------, 'joe someone')")
        logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("users table created")



def create_tracking(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS tracks (id INT PRIMARY KEY, name VARCHAR(30), lat VARCHAR(50), lon VARCHAR(50))"
        )
        cur.execute("UPSERT INTO users (id, name, lat,lon) VALUES (1, '-----------------', '-5', '152'), (2,'-----------------', '-24', '115')")
        logging.debug("create_tracks(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("users table created")



def add_users(conn, uname, uembed):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO users (id, embed, name) VALUES (" + i +", '" + uembed + "', '" + uname +"')")
        logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("user added")





def add_tracking(conn, uname, ulat, ulon):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM tracks")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO tracks (id, name, lat, lon) VALUES (" + i +", '" + uname + "', '"+ ulat + "', '"  + ulon +"')")
        logging.debug("create_tracks(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("user added")










def login(conn, uname):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, embed FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        for row in rows:
            print(row)
            print (type(row))
            if row[1] == uname:
                print ("found")
                return True, row[2]
        return False, 'none'

def delete_users(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM defaultdb.users")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE users")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()

    print ("users table deleted")


def connector():
    # conn=psycopg2.connect("dbname='nifty-puma-91.defaultdb' user='muntaser' password='rootpassword' host='free-tier.gcp-us-central1.cockroachlabs.cloud' port='26257'")
    conn=psycopg2.connect("dbname='charging-bull-344.defaultdb' user='hackabull2022' password='eJLA0HSFXiFT3NEnBaBXiQ' host='free-tier11.gcp-us-east1.cockroachlabs.cloud' port='26257'")
    return conn
   

def purgedb(conn):


    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.resp")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE resp")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()

    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.respmeta")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE respmeta")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()


    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.stress")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE stress")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()

    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.stressmeta")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE stressmeta")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    
    
    with conn.cursor() as cur:
        cur.execute("DELETE FROM defaultdb.sweat")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    
    with conn.cursor() as cur:
        cur.execute("DROP TABLE sweat")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()


    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.hrate")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE hrate")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()

    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.hrmeta")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE hrmeta")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()

    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.steps")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE steps")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()

    print ("tables deleted")




##testing
# conn = connector()
# # purgedb(conn)
# # initResp(conn)
# # initHr(conn)
# initSteps(conn)
# initStress(conn)
# initSweat(conn)



# f = open('sweat.json')
# testdata = json.load(f)

# print(testdata)

# addSweat(conn, testdata)


# r = getsweat(conn)

# print(r)



# f = open('respiration.json')
# testdata = json.load(f)

# print(testdata)

# addResp(conn, testdata)

# r = getresp(conn)

# print(r)

# f = open('stress.json')
# testdata = json.load(f)

# print(testdata)

# addStress(conn, testdata)


# r = getstress(conn)

# print(r)


# f = open('hrate.json')
# testdata = json.load(f)

# print(testdata)

# addHr(conn, testdata)

# r = gethrates(conn)

# print(r)


# f = open('steps.json')
# testdata = json.load(f)

# print(testdata)

# addSteps(conn, testdata)


# # purgedb(conn)

