# pyPoll

print("\nElection Results")
print("\n---------------------------------------------------------------------")

#Module
import os
import csv

#Lists to store the ballot Id and Candidates data
ballotId = []
candidates = []

#Set path for the file
csv_path = os.path.join("Resources","election_data.csv")

#open the file 
with open(csv_path) as csvfile:
    
    # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # append the content of each row in the ballotId and candidates list
    for anyrow in csvreader:
        ballotId.append(anyrow[0])
        candidates.append(anyrow[2])


#calulate the total number of casted vote & print the result
total_vote_cast = len(ballotId)

print("\n Total Votes: " + str(total_vote_cast))        

print("\n---------------------------------------------------------------------")


# calculate the total number of vote Charles Casper Stockham recieved
Charles_Casper_Stockham_vote = candidates.count("Charles Casper Stockham")

# calculate the percentage of vote Charles Casper Stockham got from the total
Charles_Casper_Stockham_perentage = round((Charles_Casper_Stockham_vote/total_vote_cast * 100),3)

print("\n Charles Casper Stockham: " + str(Charles_Casper_Stockham_perentage) + "% (" + str(Charles_Casper_Stockham_vote) + ")")        


# calculate the total number of vote Diana DeGette recieved
Diana_DeGette_vote = candidates.count("Diana DeGette")

# calculate the percentage of vote Diana DeGette got from the total
Diana_DeGette_perentage = round((Diana_DeGette_vote/total_vote_cast * 100),3)

print("\n Diana DeGette: " + str(Diana_DeGette_perentage) + "% (" + str(Diana_DeGette_vote) + ")")


# calculate the total number of vote Raymon Anthony Doane recieved
Raymon_Anthony_Doane_vote = candidates.count("Raymon Anthony Doane")

# calculate the percentage of vote Raymon Anthony Doane got from the total
Raymon_Anthony_Doane_perentage = round((Raymon_Anthony_Doane_vote/total_vote_cast * 100),3)

print("\n Raymon Anthony Doane: " + str(Raymon_Anthony_Doane_perentage) + "% (" + str(Raymon_Anthony_Doane_vote) + ")")  

print("\n---------------------------------------------------------------------")

# check who got the most/ maximum vote count and print out the winner
if max(Charles_Casper_Stockham_vote, Diana_DeGette_vote, Raymon_Anthony_Doane_vote) == Charles_Casper_Stockham_vote : 
    print ("\n Winner: Charles Casper Stockham")
elif max(Charles_Casper_Stockham_vote, Diana_DeGette_vote, Raymon_Anthony_Doane_vote) == Diana_DeGette_vote : 
    print ("\n Winner: Diana DeGette")
elif max(Charles_Casper_Stockham_vote, Diana_DeGette_vote, Raymon_Anthony_Doane_vote) == Raymon_Anthony_Doane_vote : 
    print ("\n Winner: Raymon Anthony Doane")

print("\n---------------------------------------------------------------------")   