from modules.helper import open_and_readlines

def search_words(list, query) -> list:
  reversed_query = "".join(query[::-1])
  return [w for w in list if w == query or w == reversed_query]

def select_chars(rows, search_word_offset, axis = "hvd") -> list:
  list_of_chars = list()
  for row, columns in enumerate(rows):
    for col, _ in enumerate(columns):

      if row + search_word_offset <= len(rows):
        if "v" in axis:
          list_of_chars.append([row[col] for row in rows[row:row+search_word_offset]])

        if "d" not in axis: continue

        if col + search_word_offset <= len(columns):
          sequence = rows[row:row+search_word_offset]
          list_of_chars.append([row[col+i] for i, row in enumerate(sequence)])
          list_of_chars.append([row[col+(search_word_offset-1)-i] for i, row in enumerate(sequence)])

      if "h" not in axis: continue

      if col + search_word_offset <= len(columns):
        list_of_chars.append([chars for chars in rows[row][col:col+search_word_offset]])

  return list_of_chars

def part_one(rows):
  search = "XMAS"
  words = ["".join(chars) for chars in select_chars(rows, len(search))]
  return len(search_words(words, search))

def part_two(rows):
  search = "MAS"

  words = ["".join(chars) for chars in select_chars(rows, len(search), "d")]
  chunk_words = [words[i:i + 2] for i in range(0, len(words), 2)]
  founds = [chunk for chunk in chunk_words if len(search_words(list(chunk), search)) == 2]

  return len(founds)

example_file_path = "4/example.txt"
input_file_path = "4/input.txt"

input = open_and_readlines(input_file_path)

rows = [list(line) for line in input]
print(f"Part 1: {part_one(rows)}")
print(f"Part 2: {part_two(rows)}")