import functools
from modules.helper import open_and_readlines

lines = open_and_readlines("2/input.txt")
data = [list(map(int, report.split(" "))) for report in lines]

def check_decreasing(a, b):
  return b if a is not False and b > a and abs(b - a) < 4 else False

def check_increasing(a, b):
  return b if a is not False and b < a and abs(a - b) < 4 else False

def check_report(report) -> tuple:
  return (
    functools.reduce(check_increasing, report),
    functools.reduce(check_decreasing, report)
  )

def report_check(report) -> tuple:
  return (
    functools.reduce(check_increasing, report),
    functools.reduce(check_decreasing, report)
  )

def check_report(report) -> dict:
  check = report_check(report)
  return {
    "report": report,
    "safe": True if check[0] is not False or check[1] is not False else False
  }

def check_report_with_problem_damping(report):
    for (idx, val) in enumerate(report["report"]):
      removed_val_report = [v for (i, v) in enumerate(report["report"]) if i != idx]
      checked = check_report(removed_val_report)
      if checked["safe"] == True:
        report["safe"] = True
        break
    return report

checked_reports = [check_report(report) for report in data]
safe_reports = [report for report in checked_reports if report["safe"] == True]

def part_one(safe_reports):
  return len(safe_reports)

def part_two(safe, checked):
  reports = [r for r in checked if r not in safe]
  checked_reports = [check_report_with_problem_damping(r) for r in reports]
  safe_reports = [r for r in checked_reports if r["safe"] == True]
  return len(safe) + len(safe_reports)

checked_reports = [check_report(report) for report in data]
safe_reports = [report for report in checked_reports if report["safe"] == True]
print(f"Part 1: {part_one(safe_reports)}")
print(f"Part 2: {part_two(safe_reports, checked_reports)}")