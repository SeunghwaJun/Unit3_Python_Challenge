#PyBank
#Import Dependencies
import os
import csv

#Open CSV file to read 
csvpath = os.path.join('budgetdata.csv')
with open (csvpath, 'r') as csvfile:
	
	#Read CSV file
	csvreader = csv.reader(csvfile, delimiter=",")
	
	#Skip header
	csvheader = next(csvreader)
	
	#Creat empty lists and dictionary
	months = []
	monthly_pl = []
	monthly_change = {}
	i = 0
	
	#Loop throught each row of CSV file
	for row in csvreader:
		#Store months and revenue in a list
		months.append(row[0])
		monthly_pl.append(int(row[1]))
		#Store revenue changes per month as key:value in a dictionary
		if i == 0:
			monthly_change[0] = months[i]
		else:
			monthly_change[monthly_pl[i] - monthly_pl[i-1]] = months[i]
		i += 1
	
	#The total number of months	
	total_months = len(months)
	#The total net amount of "Profit/Losses" over the entire period
	total_profit_loss = sum(monthly_pl)
	#The average change in "Profit/Losses" between months over the entire period
	average_change = round((sum(monthly_change)/(total_months - 1)),2)
	#Find the greatest increase in profits 
	greatest_inc = max(monthly_change)
	greatest_inc_month = monthly_change.get(greatest_inc,0)
	#The greatest decrease in losses 
	greatest_dec = min(monthly_change)
	greatest_dec_month = monthly_change.get(greatest_dec,0)

	analysis =f"""
	Financial Analysis
	-------------------------
	Total Months: {total_months}
	Total: ${total_profit_loss}
	Average Change: ${average_change}
	Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})
	Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})
	"""
	
	#Print the Financial Analysis 
	print(analysis)

# Open an empty txt file and write the Financial Analysis
with open('financial_analysis.txt', 'w') as text_file:
	text_file.write(analysis)

		