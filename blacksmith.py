import os
import sys
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser(prog="blacksmith", 
                        description="This is a scripts that initiates a React project with Typescript, TailwindCSS, ESLint and Prettier")
parser.add_argument("-n", "--name", help="Select the name of the project", metavar="NAME", required=True)
args = parser.parse_args()
project_name = args.name

COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_RESET = "\033[0m"

def main():
  try:
    current_directory = os.getcwd()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_files_dir = "config_files"

    answer = input(f"""{COLOR_BLUE}This will create a React project named {project_name} on {current_directory}. 
It will also configure TailwindCSS, ESLint and Prettier. Continue (y/n) ? {COLOR_RESET}""") or 'y'
    if answer.lower() in ['y', "yes"]:
      # Commands List
      commands = [
        # create react with vite and install dependencies
        f"npm create vite@latest {project_name} -- --template react-ts",
        f"cd {project_name} && npm install",
        f"cd {project_name} && npm install -D tailwindcss postcss autoprefixer prettier eslint @rocketseat/eslint-config",

        # configure tailwindcss
        f"cd {project_name} && npx tailwindcss init",
        f"copy /Y {script_dir}\\{config_files_dir}\\tailwind.config.js .\\{project_name}",
        f"copy /Y {script_dir}\\{config_files_dir}\\postcss.config.js .\\{project_name}",

        # remove index.css and App.css and updates src folder with base files
        f"cd {project_name}\\src && del index.css && del App.css",
        f"xcopy {script_dir}\\{config_files_dir}\\src .\\{project_name}\\src /e /i /y",

        # configure prettier and eslint
        f"copy /Y {script_dir}\\{config_files_dir}\\.eslintrc.cjs .\\{project_name}",
        f"copy /Y {script_dir}\\{config_files_dir}\\.prettierrc .\\{project_name}",
        f"copy /Y {script_dir}\\{config_files_dir}\\.prettierignore .\\{project_name}",
      ]

      # Run Commands
      for command in commands:
        print(f"{COLOR_MAGENTA}now running: {command}{COLOR_RESET}")
        subprocess.run(command, shell=True, check=True, cwd=current_directory)
    else:
      sys.exit()
  except KeyboardInterrupt:
    exit(0)


if __name__ == "__main__":
  main()