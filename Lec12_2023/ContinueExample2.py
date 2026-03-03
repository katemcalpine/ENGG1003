i = 1
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1

# Prints the numbers 1, 3, 4, so 2 is skipped due to the continue that cycles the loop back to the top for the next iteration, bypassing the print statement.