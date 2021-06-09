def fibonacci(num):
  """
  Every list item should be the sum of the previous 2 items.
  The list should start with 0 and 1
  """
  sequence_list = [0, 1]

  for i in range (2, num + 1):
    next_num = sequence_list[-1] + sequence_list[-2]

    sequence_list.append(next_num)
  
  return sequence_list[num - 1]


def lucas(num):

  """
  Every list item should be the sum of the previous 2 items.
  The list should start with 2 and 1
  """
  sequence_list = [2, 1]

  for i in range (2, num + 1):
    next_num = sequence_list[-1] + sequence_list[-2]

    sequence_list.append(next_num)
  
  return sequence_list[num - 1]



def sum_series(num, start = 0, second = 1):
  """
  Every list item should be the sum of the previous 2 list items.
  If function is called with no parameters, the list should start with 0, and 1.
  If 2 optional parameters are entered, the list will start with the 2 numbers entered as parameters
  """

  