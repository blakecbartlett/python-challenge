import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#Initialize the variables
votes_total = 0
candidate_votes = {}

#Open the csv file and read the dataset
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    
    #Skip the header row on the csv
    csv_header = next(csvreader)

    #Calculate the total votes as well as the total candidate votes
    for row in csvreader:
        votes_total = votes_total + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

#Calculate the percentage of votes each indivudial candidate won
vote_percentages = {candidate: (votes / votes_total) * 100 for candidate, votes in candidate_votes.items()}

#Find the winner
winner = max(candidate_votes, key = candidate_votes.get)

#Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_total}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Turn the output into a .txt file
with open('analysis/anaylsis.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {votes_total}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        output_file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")