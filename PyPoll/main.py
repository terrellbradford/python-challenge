#main.py for PyPoll 
#Author T. Brafdord 
#May 2021

#Import Moldules
import os
import csv

#Initialize Variables
number_of_votes = 0
correy_votes = 0
khan_votes = 0
li_votes = 0
oTooley_votes = 0

#Set Path For File
poll_csv = os.path.join('Resources', 'election_data.csv')

#Read in CSV File
with open(poll_csv, 'r') as csvfile:

    #Reading the CSV file 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #To skip the header 
    csv_header = next(csvfile)

    #Looping through csv
    for row in csvreader:
        
        #Counting votes of each candidate
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            oTooley_votes += 1

        #Sum of all candidates votes
        number_of_votes = khan_votes + correy_votes + li_votes + oTooley_votes
            
    #Percentage votes receiced for each candidate 
    correy_percentage = "{:.3%}".format(correy_votes / number_of_votes)
    kahn_percentage = "{:.3%}".format(khan_votes / number_of_votes)
    li_percentage = "{:.3%}".format(li_votes / number_of_votes)
    oTooley_percentage = "{:.3%}".format(oTooley_votes / number_of_votes)
    
    #Max function to determine candidate with most votes
    most_votes = max(correy_votes, khan_votes, li_votes, oTooley_votes)

    #based on most_vote return Winner
    if most_votes == khan_votes:
        winner = "Khan"
    elif most_votes == correy_votes:
        winner = "Correy"
    elif most_votes == li_votes:
        winner = "Li"
    else:
        winner = "O'Tooley" 

#Printing output to terminal
print(f"\nElection Results")
print(f"--------------------------------")
print(f"Total Votes: {number_of_votes}")
print(f"--------------------------------")
print(f"Kahn: {kahn_percentage:} ({khan_votes})")
print(f"Correy: {correy_percentage:} ({correy_votes})")
print(f"Li: {li_percentage:} ({li_votes})")
print(f"O'Tooley: {oTooley_percentage:} ({oTooley_votes})")
print(f"--------------------------------")
print(f"Winner: {winner}")
print(f"--------------------------------")

#Name of txt file 
output_file = os.path.join('analysis', 'PyPoll_analysis.txt')

#Open the output txt file  
with open(output_file, 'w',) as txtfile:
#Creating lines for output file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {number_of_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percentage:} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percentage:} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percentage:} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {oTooley_percentage:} ({oTooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")