# 3. Loop Condition Logic
# Objective:
# The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.

puppy_kisses = ["some", "more", "extra", "lots of", "tons of", "too many"]
amount_kisses = 0

while True:
    for kiss in puppy_kisses:
        amount_kisses += 1
        print(f"Puppy giving {kiss} kisses!")
        if amount_kisses == 5:
            break
    break

# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met.

puppy_kisses = ["some", "more", "extra", "lots of", "tons of", "too many"]

while True:
    for kiss in puppy_kisses:
        print(f"Puppy giving {kiss} kisses!")
        if kiss == "too many":
            print("Alright, no more kisses!")
            break
    if kiss == "too many":
        break    