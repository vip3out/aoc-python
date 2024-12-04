import sys
import os

_, day, *rest = sys.argv

new_python_file_path = f"{day}.py"
if os.path.exists(new_python_file_path) == False:
  with open("./stubs/solver.stub") as stub_file:
    stub_content = stub_file.read()

    with open(f"{day}.py", "w") as python_file:
      python_file_content = stub_content.replace("######", day)
      python_file.write(python_file_content)

    os.makedirs(f"./inputs/{day}")
    open(f"./inputs/{day}/test.txt", "w")
    open(f"./inputs/{day}/input.txt", "w")

os.system(f"python {new_python_file_path}")
