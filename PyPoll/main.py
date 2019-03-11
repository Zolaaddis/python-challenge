# Modules
import os
import csv
 
# Set path for file

csvpath = os.path.join("..", "Resources", "election_data.csv")
 
# Open the CSV
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
                
# Create a dictionary called "candidate_information{}":     
        candidate_information = {}
    
        # Create a new list called "candidate_vote_details[]":
        candidate_vote_details = [0, 0]
        
        # Initialize total vote counts to 0
        total_vote_count = 0
 
        for row in csvreader:
            if row[2] not in candidate_information:
                del candidate_vote_details
                candidate_vote_details = [1, 0]       
                candidate_information[row[2]] = candidate_vote_details                   
                total_vote_count = total_vote_count + 1
           
            else:
                candidate_information[row[2]][0] = candidate_information[row[2]][0] + 1
                total_vote_count = total_vote_count + 1
               
#calcualte percentage of votes per candidate 
highest_votes = 0
for candidate, vote_info in candidate_information.items():
    
    percentage_vote = (vote_info[0] / total_vote_count) * 100
    candidate_information[candidate][1] = percentage_vote
 
    if vote_info[0] > highest_votes:
        highest_votes = vote_info[0]
        candidate_with_highest_votes = candidate
 
 
# Create Header Message
print('Election Results\n')
print('---------------------\n')
print(f'Total Votes: {total_vote_count}\n')
print('---------------------\n')
 
# Create Candidate specific message with their voting record
for candidate, vote_info in candidate_information.items():
    print(f'{candidate}: {vote_info[1]:.2f}% ({vote_info[0]})\n')
 
print('---------------------\n')
print(f'Winner: {candidate_with_highest_votes}\n')
print('---------------------\n')

# Write the message to the text file
text_file = open('Election Results.txt', "w")
text_file.write('Election Results.txt'+'\n')