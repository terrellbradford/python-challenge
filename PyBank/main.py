#main.py for PyBank 
#Author T. Brafdord 
#May 2021

#import Moldules
import csv 
import os

#Path to data from Resource folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

#initialize variables 
lines = 0
total = 0
decrease = 0
increase = 0
amount = 0
profit_loss = []
dates = []
month_profit_loss = []
change = 0   

# opening the CSV file 
with open(bank_csv, 'r') as csv_file:
      
  # reading the CSV file 
  csv_reader = csv.reader(csv_file, delimiter = ",")
  
  # to skip the header 
  header = next(csv_reader) 
  #get row count
  lines= len(list(csv_reader))
  # reset back to top of cvs
  csv_file.seek(0)
  ## to skip the header 
  header = next(csv_reader) 
 
  #sum of profit/loss
  numbers = (float(row[1]) for row in csv_reader)
  total = sum(numbers)

  # reset back to top of cvs
  csv_file.seek(0)
   # to skip the header 
  header = next(csv_reader) 

  #skip line after header can't calculate monthly change properly with this line
  skip = next(csv_reader) 

  # setting amount the 3rd row of profit/loss. 
  # #Amount variable amount will always be one row ahead of change variable.
  amount = float(skip[1])

  #looping through CSV
  for row in csv_reader:
    #track date column 1
    dates.append(row[0])

    #setting variable change to current row value minus next row value
    change = float(row[1]) - amount
    #tracking monthly change
    month_profit_loss.append(change)
    #setting next amount value
    amount = float(row[1])

    #retrieve monthly min and max change
    decrease = min(month_profit_loss)
    increase = max(month_profit_loss)

    #print(month_profit_loss)
    average_change = round(sum(month_profit_loss) / len(month_profit_loss),2)

  #index methos return finds decrease and return date from preivous column 
  decrease_index = month_profit_loss.index(decrease)
  decrease_date = dates[decrease_index]
  
  #index methos return finds increase and return date from preivous column 
  increase_index = month_profit_loss.index(increase)
  increase_date = dates[increase_index]

  #Printing output to terminal 
  print ("\nFinacial Analysis \n-----------------------------------------\n")

  print(f"Total Months:", lines)

  print (f"Total:, ${float(total)}")

  print (f"Average Change: ${float(average_change)}")

  print (f"Greatest Increase in Profits: {increase_date} ${float(increase)}")

  print (f"Greatest Decrease in Profits: {decrease_date} ${float(decrease)}\n") 

  # name of txt file 
filename = os.path.join('analysis', "PyBank_analysis.txt")
    
# writing to txt file 
with open(filename, 'w') as txtfile:
    # creating lines for output file
    txtfile.write("Finacial Analysis \n-----------------------------------------\n \n")
    txtfile.write("Total Months: ")
    txtfile.write(str(lines))
    txtfile.write(f"\nTotal: ${float(total)}")
    txtfile.write(str(f"\nAverage Change: ${float(average_change)}"))
    txtfile.write(str(f"\nfGreatest Increase in Profits: {increase_date} ${float(increase)}"))
    txtfile.write(str(f"\nGreatest Decrease in Profits: {decrease_date} ${float(decrease)}"))
