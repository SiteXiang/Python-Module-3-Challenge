import os
import csv

# Set the CSV file path (replace with your absolute path)
csv_path = os.path.join("C:\\Users\\Sy X\\DATA CLASS\\EXCEL-HW\\Python-Module-3-Challenge\\PyPoll\\Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
max_votes = 0
winner = ""

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # Calculate the total number of votes
        total_votes += 1
        candidate = row[2]

        # Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Find the winner
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_path = os.path.join("C:\\Users\\Sy X\\DATA CLASS\\EXCEL-HW\\Python-Module-3-Challenge\\PyPoll\\analysis", "election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
