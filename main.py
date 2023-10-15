from numpy import full

#build an array of zeroes
seq1 = "GCATGCT"
seq2 = "GATACCA"
h
n_rows = len("-"+seq1)
n_columns = len("-"+seq2)

scoring_array = full([n_rows,n_columns],0)
print("Scoring array:\n",scoring_array)

traceback_array = full([n_rows,n_columns],"-")
print("Traceback array:\n",traceback_array)



n_rows = len(seq1) + 1  # need an extra row up top
n_columns = len(seq2) + 1  # need an extra column on the left
row_labels = [label for label in "-" + seq1]
column_labels = [label for label in "-" + seq2]

scoring_array = full([n_rows, n_columns], 0)
traceback_array = full([n_rows, n_columns], "-")

# Define Unicode arrows we'll use in the traceback array
up_arrow = "\u2191"
right_arrow = "\u2192"
down_arrow = "\u2193"
left_arrow = "\u2190"
down_right_arrow = "\u2198"
up_left_arrow = "\u2196"

arrow = "-"
gap_penalty = -1
match_bonus = 1
mismatch_penalty = -1
# iterate over columns first because we want to do
# all the columns for row 1 before row 2
for row in range(n_rows):
    for col in range(n_columns):
        if row == 0 and col == 0:
            # We're in the upper right corner
            score = 0
            arrow = "-"
        elif row == 0:
            # We're on the first row
            # but NOT in the corner

            # Look up the score of the previous cell (to the left) in the score array\
            previous_score = scoring_array[row, col - 1]
            # add the gap penalty to it's score
            score = previous_score + gap_penalty
            arrow = left_arrow
        elif col == 0:
            # We're on the first column but not in the first row
            previous_score = scoring_array[row - 1, col]
            score = previous_score + gap_penalty
            arrow = up_arrow
        else:
            # We're in a 'middle' cell of the alignment

            # Calculate the scores for coming from above,
            # from the left, (representing an insertion into seq1)
            cell_to_the_left = scoring_array[row, col - 1]
            from_left_score = cell_to_the_left + gap_penalty

            # or from above (representing an insertion into seq2)
            above_cell = scoring_array[row - 1, col]
            from_above_score = above_cell + gap_penalty

            # diagonal cell, representing a substitution (e.g. A --> T)
            diagonal_left_cell = scoring_array[row - 1, col - 1]

            # NOTE: since the table has an extra row and column (the blank ones),
            # when indexing back to the sequence we want row -1 and col - 1.
            # since row 1 represents character 0 of the sequence.
            if seq1[row - 1] == seq2[col - 1]:
                diagonal_left_cell_score = diagonal_left_cell + match_bonus
            else:
                diagonal_left_cell_score = diagonal_left_cell + mismatch_penalty

            score = max([from_left_score, from_above_score, diagonal_left_cell_score])
            # take the max

            # make note of which cell was the max in the traceback array
            # using Unicode arrows
            if score == from_left_score:
                arrow = left_arrow
            elif score == from_above_score:
                arrow = up_arrow
            elif score == diagonal_left_cell_score:
                arrow = up_left_arrow

        traceback_array[row, col] = arrow
        scoring_array[row, col] = score
    print ((scoring_array, row_labels, column_labels))
    print((traceback_array, row_labels, column_labels))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
