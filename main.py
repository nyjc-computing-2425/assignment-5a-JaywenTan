def to_hms(seconds):
  """
  Converts seconds to hours, minutes, and seconds, and returns it as a list.

  Parameters
  ---------
  seconds: int
      the seconds to be calculated

  Returns
  ---------
  list
      a list of integers representing hours, minutes, seconds

  Example:
  >>> to_hms(10)
  [0, 0, 10]
  >>> to_hms(61)
  [0, 1, 1]
  >>> to_hms(7199)
  [1, 59, 59]
  """

    # Type your code below
  lst = []
  if type(seconds) == int and seconds >= 0:
    seconds = divmod(seconds,3600)
    hours = seconds[0]
    seconds = divmod(seconds[1],60)
    minutes = seconds[0]
    seconds = seconds[1]
    lst.append(hours)
    lst.append(minutes)
    lst.append(seconds)
    return lst 
  else:
    print("Unsupported input type.")


