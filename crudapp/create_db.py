import sqlite3 as sql 

conn = sql.connect('db_web.db')
cur = conn.cursor()

cur.execute('drop table if exists conv;')
cur.execute('drop table if exists msg;')

sql = '''
        create table "conv" ( 
            "id" integer primary key autoincrement not null,
            "id_tel" text not null,
            "nome" text not null,
            "conf" integer not null,
            "doc" text,
            "rest_alim" text,
            "acomp" integer
        );     
'''

cur.execute(sql)
conn.commit()

sql = '''
        create table "msg" (
            "id" integer primary key autoincrement,
            "text" text
        );
'''

cur.execute(sql)
conn.commit()

conn.close()