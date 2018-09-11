import db_operations
while True:
	print """
	1. insert
	2. update
	3. delete
	4. show
	q. quit
	"""
	opt = raw_input("Enter an option:")
	if opt.lower()=="q" or opt.lower()=="quit":
		print "thank you!!"
		break
	if opt=="1":
		db_operations.insert()
	elif opt=="2":
		db_operations.update()
	elif opt=="3":
		db_operations.delete()
	elif opt=="4":
		print db_operations.browse()
	else:
		print "wrong option"