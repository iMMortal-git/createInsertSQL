
filename = input('\nName of new SQL file: ')

f1 = open(filename, "w+")

tableName = None
while tableName != '':

	tableName = input('Table name: ')

	if tableName != '':
		f1.write("INSERT INTO ")
		f1.write(tableName)
		f1.write(" VALUES(")

		data = None
		isFirstVal = True
		while data != '':
			
			data = input('Data: ')

			if data == '':
				f1.write(");\n")
			elif data != '' and isFirstVal == True:
				f1.write("'")
				f1.write(data)
				f1.write("'")
				isFirstVal = False
			elif data != '' and isFirstVal == False:
				f1.write(", '")
				f1.write(data)
				f1.write("'")
	else:
			pass

f1.close()