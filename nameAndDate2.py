birthdays = [('Boris', '19 June 1964'),
             ('Harry', '28 July 1993'),
             ('Donald', '14 June 1946'),
             ('Guido', '31 January 1956'),
             ('Guido', '13 April 1570')]
D = dict(birthdays)
for k,v in D.items():
	print(k+ ' was born in '+v)
