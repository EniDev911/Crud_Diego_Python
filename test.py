
import mysql.connector
from dotenv import load_dotenv
import os 

dotenv_values = load_dotenv('BD/.env')
print(os.getenv("DBHOST"))

try:
	cnx = mysql.connector.connect(
			host = os.getenv("DBHOST"),
			user = os.getenv("DBUSER"),
			password = os.getenv("DBPASS"),
			db = os.getenv("DBDATABASE")
			)

	cursor = cnx.cursor()
	sql = 'SELECT * FROM curso;'
	cursor.execute(sql)
	for x in cursor:
		print(x)

except mysql.connector.Error as err:
	print(err)