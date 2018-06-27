def run():
	csv_filepathname='raw_data/combine.csv'
	from polls.models import Combine
	import csv
	reader = csv.reader(open(csv_filepathname))
	for row in reader:
		p=Combine()
		# p.State=row['State']
		# p.District=row['District']
		# p.Crop=['Crop']
		# p.Year=row['Year'] 
		# Season=['Season']
		# p.Area=row['Area'] 
		# p.Production=row['Production']
		# p.Yield=row['Yield']
		# p.Yield_Units=row['Yield_Units']
		p.State=row[0]
		p.District=row[1]
		p.Crop=row[2]
		p.Year= row[3] 
		p.Season= row[4]
		p.Area=row[5] 
		p.Production=row[6]
		p.Yield=row[7]
		p.Yield_Units=row[8]
		p.save()
		print(p.id)
# run()