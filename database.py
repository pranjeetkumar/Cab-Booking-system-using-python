import sqlite3
conn = sqlite3.connect("cabsbooking.db")
conn.cursor()
try:
    conn.execute('''create table admin
                (admin_id integer primary key,
                admin_username varchar(20) not null,
                admin_password varchar(20) not null)''')
    conn.execute('''create table cab_dealers
                (cab_dealer_id integer primary key,
                cab_dealer_name varchar(20) not null,
                cab_dealer_password varchar(20) not null,
                cab_dealer_email varchar(20) not null,
                cab_dealer_phone varchar(20) not null)''')
    conn.execute('''create table cabs
                (cab_id integer primary key,
                cab_name varchar(20) not null,
                cab_type varchar(20) not null,
                cab_model varchar(20) not null,
                cab_dealer_id integer(11) not null,
                cab_from varchar(20) not null,
                cab_to varchar(20) not null,
                cab_number varchar(20))''')
    conn.execute('''create table users
                (user_id integer primary key,
                user_name varchar(20) not null,
                user_password varchar(20) not null,
                user_email varchar(20) not null,
                user_phone integer(20) not null)''')
    print("Table created............")
except:
    print("Some eroor............")