'''
Challenge 2b
'''

def sequence_align(x, y, c, delta) -> list:
    # Create a matrix to store the alignment scores.
    matrix = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    
    # Initialize the first row and column of the matrix.
    for i in range(len(x) + 1):
        matrix[i][0] = -i * delta
    for j in range(len(y) + 1):
        matrix[0][j] = -j * delta
    
    # Fill in the rest of the matrix.
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
          match_score = matrix[i - 1][j - 1] + c(x[i - 1], y[j - 1])
          delete_score = matrix[i - 1][j] - delta
          insert_score = matrix[i][j - 1] - delta
          matrix[i][j] = max(match_score, delete_score, insert_score)
    
    # Trace back the matrix to find the alignment.
    alignment = []
    i = len(x)
    j = len(y)
    while i > 0 and j > 0:
        if matrix[i][j] == matrix[i - 1][j - 1] + c(x[i - 1], y[j - 1]):
          alignment.append((x[i - 1], y[j - 1]))
          i -= 1
          j -= 1
        elif matrix[i][j] == matrix[i - 1][j] - delta:
          alignment.append((x[i - 1], '-'))
          i -= 1
        else:
          alignment.append((y[j - 1], '-'))
          j -= 1
    
    # Reverse the alignment so that it is in the correct order.
    alignment.reverse()
    
    # Calculate the cost of the alignment.
    cost = 0
    for i in range(len(alignment)):
        if alignment[i][0] != alignment[i][1]:
          cost += delta
    
    return alignment, cost

