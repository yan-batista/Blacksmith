import os
import sys
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser(prog="blacksmith", 
                        description="This is a scripts that initiates a React project with Typescript, TailwindCSS, ESLint and Prettier")
parser.add_argument("-n", "--name", help="Select the name of the project", metavar="NAME", required=True)
args = parser.parse_args()
project_name = args.name

def main():
  current_directory = os.getcwd()
  answer = input(f"""This will create a React project named {project_name} on {current_directory}. 
It will also configure TailwindCSS, ESLint and Prettier. Continue (y/n) ? """) or 'y'
  if answer.lower() in ['y', "yes"]:
    print("running")
    # Commands List
    commands = [
      # create react with vite and install dependencies
      f"npm create vite@latest {project_name} -- --template react-ts",
      f"cd {project_name} && npm install",
      f"cd {project_name} && npm install -D tailwindcss postcss autoprefixer prettier eslint @rocketseat/eslint-config",

      # configure tailwindcss
      f"cd {project_name} && npx tailwindcss init",
      f"copy /Y tailwind.config.js .\\{project_name}",
      f"copy /Y postcss.config.js .\\{project_name}",

      # remove index.css and App.css and updates src folder with base files
      f"cd {project_name}/src && del index.css && del App.css",
      f"xcopy src .\\{project_name}\\src /e /i /y",

      # configure prettier and eslint
      f"copy /Y .eslintrc.cjs .\\{project_name}",
      f"copy /Y .prettierrc .\\{project_name}",
      f"copy /Y .prettierignore .\\{project_name}",
    ]

    # Run Commands
    for command in commands:
      print(command)
      subprocess.run(command, shell=True, check=True, cwd=current_directory)
  else:
    sys.exit()

if __name__ == "__main__":
  main()