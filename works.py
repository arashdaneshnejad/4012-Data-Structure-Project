from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import psycopg2

connection =psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="2135", port="5432")
cursor = connection.cursor()
postgreSQL_select_Query = "select * from works"

cursor.execute(postgreSQL_select_Query)
work = cursor.fetchall()
print(work)