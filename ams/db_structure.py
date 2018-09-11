import psycopg2
con = psycopg2.connect(host="localhost",user="postgres",
						password="root",port=5432,database="batch49")
cur = con.cursor()
cur.execute("create table customer(id int, name varchar(250))")
con.commit()
con.close()