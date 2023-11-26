from functions1_3 import hirschberg

# Read alphabet and scores from text file
with open("scores.txt", 'r') as f:
    alphabet = f.readline().rstrip()
    f.readline()
    gapPenalty = int(f.readline())
    f.readline()
    simMatrix = [list(map(int, line.split())) for line in f]

# Create a 1-1 mapping from characters to integers, for simplicity in the algorithm
alphEnum = {char: i for i, char in enumerate(alphabet)}

# Load input sequences
with open("sequences.txt", 'r') as f, open("alignments_hbg.txt", 'w') as g:
    line = f.readline()

    while line:
        # This loop repeats until no more input sequences are found
        # At each iteration, we read the next two sequences and run the algorithm on them
        A = line.rstrip()
        B = f.readline().rstrip()
        f.readline()
        line = f.readline()

        # Run the Hirschberg algorithm
        print("First sequence:", A)
        print("Second sequence:", B)
        print("Calculating alignment distance by Hirschberg method...")

        z = hirschberg(A, B, simMatrix, gapPenalty, alphEnum)

        print("Alignment of A: ", z[0])
        print("Alignment of B: ", z[1])
        print("Similarity score: ", z[2], '\n')

        # Write outputs to text file
        g.write("Similarity Score: " + str(z[2]) + "\n")
        g.write("Aligned Sequence 1: " + z[0] + "\n")
        g.write("Aligned Sequence 2: " + z[1] + "\n")
        g.write("\n")

# Finish
