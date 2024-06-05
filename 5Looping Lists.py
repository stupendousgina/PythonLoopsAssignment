# 5. Looping Lists - The Rhythm of Repetition
# Objective:
# Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its unique style and purpose. By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.

# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track = 0
for genre in genres:
    track +=1
    if genre == 'Jazz':
       print(f"Track {track}: {genre} - Chill vibes.")
    elif genre == 'Rock':
       print(f"Track {track}: {genre} - Rockstar dreams.")
    elif genre == 'Hip-hop':
       print(f"Track {track}: {genre} - Bounce with the beat.")
    elif genre == 'Classical':
       print(f"Track {track}: {genre} - Eargasms and brain tickles.")
    


# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track = 0
while True:
       for genre in genres:
              track +=1
              if genre == 'Jazz':
                     print(f"Track {track}: {genre} - Chill vibes.")
              elif genre == 'Rock':
                     print(f"Track {track}: {genre} - Rockstar dreams.")
              elif genre == 'Hip-hop':
                     print(f"Track {track}: {genre} - Bounce with the beat.")
                     break
              elif genre == 'Classical':
                     print(f"Track {track}: {genre} - Eargasms and brain tickles.")
                     
       break

  

# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in range(len(genres)):
       if genres[genre] == 'Classical':
              continue           
       else:
              print("Track " + str(genre+1) + ": " + genres[genre] + " - The light show is ready!")



# for genre in range(len(genres)-1):
#        print("Track " + str(genre+1) + ": " + genres[genre] + " - The light show is ready!")
                            