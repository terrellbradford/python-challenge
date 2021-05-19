import csv 
import os

#Path to data from Resource folder
bank_csv = os.path.join('Resources', 'Resources_budget_data.csv')

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

  lines= len(list(csv_reader))

  csv_file.seek(0)

  header = next(csv_reader) 
  numbers = (float(row[1]) for row in csv_reader)
  total = sum(numbers)

  csv_file.seek(0)

  header = next(csv_reader) 

  #skip line after header can't calculate profit/loss with this line
  skip = next(csv_reader) 
  amount = float(skip[1])

  for row in csv_reader:
    #track date
    dates.append(row[0])

    #add sum and number of lines
    #profit_loss.append(float(row[1]))
    #total = sum(profit_loss)
    #lines = len(profit_loss)
    
    #skip = next(csv_reader)
    change = float(row[1]) - amount
    month_profit_loss.append(change)
    amount = float(row[1])

    #retreive monthly min and max change
    decrease = min(month_profit_loss)
    increase = max(month_profit_loss)

    #print(month_profit_loss)
    average_change = sum(month_profit_loss) / len(month_profit_loss)
  
  print(change)

  print ("Finacial Analysis \n-----------------------------------------\n")

  print(f"Total Months: ", lines)

  print (f"Total: ", float(total))

  print (f"Average Change: ", float(average_change))

  print (f"Greatest Increase in Profits: ", float(increase))

  print (f"Greatest Decrease in Profits: ", float(decrease))

  # name of txt file 
filename = os.path.join('analysis', "records.txt")
    
# writing to txt file 
with open(filename, 'w') as txtfile:
    # creating a csv writer object 
    txtfile.write("Finacial Analysis \n-----------------------------------------\n \n")
    txtfile.write("Total Months: ")
    txtfile.write(str(lines))
    txtfile.write("\nTotal: ")
    txtfile.write(str(total))
    txtfile.write("\nAverage Change: ")
    txtfile.write(str(average_change))
    txtfile.write("\nGreatest Increase in Profits: ")
    txtfile.write(str(increase)) 
    txtfile.write("\nGreatest Decrease in Profits: ")
    txtfile.write(str(decrease)) 
