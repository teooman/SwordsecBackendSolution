import json
import os
import psycopg2


POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME','swordsecuser')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD','password')
POSTGRES_DB = os.getenv('POSTGRES_DB','swordsec_test')

def maker(n):
    conn = psycopg2.connect(host="postgres",
                            database=POSTGRES_DB,
                            user=POSTGRES_USERNAME,
                            password=POSTGRES_PASSWORD)

    cur = conn.cursor()

    with open(f"users/{n}.json", "r") as r:
        jsonfile = json.load(r)

        for user in jsonfile:
            first_name = user.get('first_name')
            last_name = user.get('last_name')
            email = user.get('email')
            gender = user.get('gender')
            ip = user.get('ip_address')
            username = user.get('user_name')
            agent = user.get('agent')
            country = user.get('country')

            cur.execute("""INSERT INTO users 
                                (first_name, 
                                last_name,
                                email,
                                gender,
                                ip_address,
                                user_name, 
                                user_agent, 
                                country) 
                                VALUES (
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s);""", (first_name,
                                last_name,
                                email,
                                gender,
                                ip,
                                username,
                                agent,
                                country))

    cur.close()
    conn.commit()
    conn.close()
