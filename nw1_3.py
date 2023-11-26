from functions1_3 import nw

# Read alphabet and scores from text file
with open("scores.txt", 'r') as f:
    alphabet = f.readline().rstrip('\n\r')
    f.readline()
    gapPenalty = int(f.readline())
    f.readline()
    simMatrix = []
    line = f.readline()
    while line:
        row = list(int(x) for x in line.split())
        simMatrix.append(row)
        line = f.readline()

# Create a 1-1 mapping from characters to integers, for simplicity in algorithm
alphEnum = {alphabet[i]: i for i in range(len(alphabet))}

# Load input sequences
with open("sequences.txt", 'r') as f:
    # Open output file, in preparation for storing output alignments
    with open("alignments_nw.txt", 'w') as g:
        line = f.readline()
        while line:
            # This loop repeats until no more input sequences are found
            # At each iteration, we read the next two sequences and run the algorithm on them
            A = line.rstrip('\n\r')
            B = f.readline().rstrip('\n\r')
            f.readline()
            line = f.readline()

            # Run the NW algorithm
            print("First sequence:", A)
            print("Second sequence:", B)
            print("Calculating alignment distance by Needleman-Wunsch method...")

            z = nw(A, B, simMatrix, gapPenalty, alphEnum)

            print("Alignment of A: ", z[0])
            print("Alignment of B: ", z[1])
            print("Similarity score: ", z[2], '\n')

            # Write outputs to text file
            g.write(str(z[2]) + "\n")
            g.write(z[0] + "\n")
            g.write(z[1] + "\n")
            g.write("\n")
