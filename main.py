import sys, os, datetime
from aocd import submit

# set default valuies
today = datetime.date.today()
year = today.year
day = today.day

# set playing infos
playing_year = int(input(f"Which year do you want play (default: {year})") or year)
playing_day = int(input(f"Which day do you want play (default: {day})") or day)
playing_part = str(input(f"Which part do you want play (default: a)") or 'a')

# set module
module_folder = os.path.join(
  os.path.dirname(__file__),
  str(playing_year)
)
sys.path.insert(0, module_folder)
puzzle_module = __import__(str(playing_day))

# set puzzle part solution method
puzzle_func = getattr(puzzle_module, f"part_{playing_part}")

# submit solution
solution = puzzle_func()
submit(solution, part=playing_part, day=playing_day, year=playing_year)
