

# import dependencies
import csv
import os

#Add a variable to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")

file_to_save= os.path.join("analysis","election_analysis.txt")

#initialize a total vote counter 
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenges Track the largest county voter turnout and its percentage 
largest_county_turnout = ""
largest_county_votes = 0

# Read the csv and convert it into a list of dictionaries 
with open (file_to_load) as election_data:
    reader = csv.reader(election_data)
    print (reader)

# read the header 
header = next(reader)
#print(header)
