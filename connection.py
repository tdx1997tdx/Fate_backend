import psycopg2
conn = psycopg2.connect(database="ubuntu", user="ubuntu", password="123456", host="122.152.251.171", port="5432")
print("connection success")