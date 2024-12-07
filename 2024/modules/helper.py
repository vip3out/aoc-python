from functools import reduce
from math import floor

def open_and_split_into_blocks(file_loc: str) -> list:
  """returns a list of blocks from a document

  Parameters
  ----------
  file_loc : str
      The file location of the input file

  Returns
  -------
  blocks : list
      a list of with list representing the lines divided into blocks
  """
  with open(file_loc) as f:
    blocks = f.read().split("\n\n")
    blocks = [[line.strip() for line in block.split("\n")] for block in blocks]

  return blocks

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

def cycle(l: list):
  """returns a generator of endless list repeat

  Parameters
  ----------
  l : list
      The repeating list
  """
  while True:
    for i in l:
      yield i


def transform_list(l: list, start: int) -> list:
  """returns a new list thats starts from `start` end ends with the items before

  Parameters
  ----------
  l : list
      The list that should be transformed
  start : int
      the index where the transformed list starting

  Returns
  -------
  output : list
      the new transformed list
  """
  return l[start] + l[start+1::] + l[:start]

def print_progress(current: int, all: int, flush: bool = False):
  """ a print helper that prints progress

  Parameters
  ----------
  current : int
      The current process cylce
  all : int
      The length of process
  flush : bool
      flush the stdout of print or not
  """
  value = floor( current / all * 100 )
  left = 100 - value
  end = "\r" if flush == True else "\n"
  print(f"[{"#"*value}{"-"*left}] {value}%", end=end)