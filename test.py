import mysql.connector as mysql 
from mysql.connector import errorcode

config = {
	'user': 'ul35rprgfokcahwh',
	'password': 'KIhphdZ54bTcAVYmtqOk',
	'host': 'bfgvnwc7zu9xkf2qtqpx-mysql.services.clever-cloud.com'
}

try:
	cnx = mysql.connect(**config)
	print("Se establecio la conexión")

except mysql.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Problem in your connection")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database not exists!")
	else: 
		print(err)
else:
	cnx.close()
