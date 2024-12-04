from functools import reduce

def open_and_readlines(file_loc: str) -> list:
  """returns a list of lines from a document

  Parameters
  ----------
  file_loc : str
      The file location of the input file

  Returns
  -------
  lines : list
      a list of strings representing the lines
  """
  with open(file_loc) as f:
    lines = [line.strip() for line in f.readlines()]

  return lines

def open_and_concatlines(file_loc: str) -> str:
  """returns a str of concateneted lines from a document

  Parameters
  ----------
  file_loc : str
      The file location of the input file

  Returns
  -------
  output : str
      a list of strings representing the lines
  """
  lines = open_and_readlines(file_loc)
  return reduce(lambda p,c: p + c, lines)