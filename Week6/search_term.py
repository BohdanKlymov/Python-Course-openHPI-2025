# Write a program that asks the user for a search term. 
# Perform a search using the iTunes search service for the entity type album. 
# The program should then print how many search results where returned. 
# For each result print the artist name, the album name and track count.

# Below is an example execution of the program. Note that the output is abbreviated.

#     Please enter a search term: cash
#     The search returned 50 results.
#     Artist: Luke Bryan - Album: Crash My Party - Track Count: 13
#     Artist: Johnny Cash - Album: The Essential Johnny Cash - Track Count: 36
#     Artist: Dave Matthews Band - Album: Crash - Track Count: 12


import requests

search_term = input("Please enter a search term: ")

url = "https://itunes.apple.com/search?term=" + search_term + "&entity=album"

response = requests.get(url)
data = response.json()

count = data["resultCount"]
print(f"The search returned {count} results.")

for result in data["results"]:
    artist = result.get("artistName", "Unknown")
    album = result.get("collectionName", "Unknown")
    tracks = result.get("trackCount", "Unknown")
    print(f"Artist: {artist} - Album: {album} - Track Count: {tracks}")
