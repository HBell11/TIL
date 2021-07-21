def rotate_a_matrix_by_90_degree_clockwise(a):
  row_len = len(a)
  col_len = len(a[0])
  
  res = [[0]* row_len for _ in range(col_len)]
  for r in range(row_len):
    for c in range(col_len):
      res[c][row_len-1-r] = a[r][c]
      
  return res
