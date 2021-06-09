def fibonacci(num):
  sequence_list = [0, 1]

  for i in range (2, num + 1):
    next_num = sequence_list[-1] + sequence_list[-2]

    sequence_list.append(next_num)
  
  return sequence_list[num - 1]


def lucas(num):
  sequence_list = [2, 1]

  for i in range (2, num + 1):
    next_num = sequence_list[-1] + sequence_list[-2]

    sequence_list.append(next_num)
  
  return sequence_list[num - 1]