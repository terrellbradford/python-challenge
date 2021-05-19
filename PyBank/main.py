import csv 
import os

#Path to data from Resource folder
bank_csv = os.path.join('Resources', 'Resources_budget_data.csv')

# opening the CSV file 
with open(bank_csv, 'r') as csv_file: 
      
  # reading the CSV file 
  csv_reader = csv.reader(csv_file, delimiter = ",")
  
  # to skip the header 
  header = next(csv_reader) 

  #count number of rows
  lines= len(list(csv_reader))

  #return to top of file
  csv_file.seek(0)

  # Skip header line
  header = next(csv_reader)

  #Add Profit and Loss column
  numbers = (float(row[1]) for row in csv_reader)

  total = sum(numbers)


  print ("Finacial Analysis \n-----------------------------------------\n")

  print(f"Total Months: ", lines)

  print (f"Total: ", float(total))

  print (f"Average Change: ")

  print (f"Greatest Increase in Profits: ")

  print (f"Greatest Decrease in Profits: ")
    

  # name of txt file 
filename = os.path.join('analysis', "records.txt")
    
# writing to txt file 
with open(filename, 'w') as txtfile: 
    # creating a csv writer object 
    txtwriter = csv.writer(txtfile) 
    txtfile.write("Finacial Analysis \n-----------------------------------------\n \n")
    txtfile.write("Total Months: ")
    txtfile.write(str(lines))
    txtfile.write("\nTotal: ")
    txtfile.write(str(total))
    txtfile.write("\nAverage Change: ")
    txtfile.write(str(total))
    txtfile.write("\nGreatest Increase in Profits: ")
    #txtfile.write(str(max(numbers))) 
    txtfile.write("\nGreatest Decrease in Profits: ")
    #txtfile.write(str(decrease)) 
