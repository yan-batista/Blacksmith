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
    if getattr(sys, 'frozen', False):
      script_dir = os.path.dirname(sys.executable)
      config_files_dir = os.path.join(script_dir, "_internal", "config_files")
    else:
      script_dir = os.path.dirname(os.path.realpath(__file__))
      config_files_dir = os.path.join(script_dir, "config_files")

    answer = input(f"""{COLOR_BLUE}This will create a React project named {project_name} in {current_directory}. 
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
        f"copy {os.path.join(config_files_dir, 'tailwind.config.js')} {os.path.join(current_directory, project_name)}",
        f"copy {os.path.join(config_files_dir, 'postcss.config.js')} {os.path.join(current_directory, project_name)}",

        # remove index.css and App.css and updates src folder with base files
        f"cd {os.path.join(project_name, 'src')} && del index.css && del App.css",
        f"xcopy {os.path.join(config_files_dir, 'src')} {os.path.join(current_directory, project_name, 'src')} /e /i /y",

        # configure prettier and eslint
        f"copy {os.path.join(config_files_dir, '.eslintrc.cjs')} {os.path.join(current_directory, project_name)}",
        f"copy {os.path.join(config_files_dir, '.prettierrc')} {os.path.join(current_directory, project_name)}",
        f"copy {os.path.join(config_files_dir, '.prettierignore')} {os.path.join(current_directory, project_name)}",
      ]

      # Run Commands
      for command in commands:
        print(f"{COLOR_MAGENTA}now running: {command}{COLOR_RESET}")
        subprocess.run(command, shell=True, check=True, cwd=current_directory)
    else:
      sys.exit()
  except KeyboardInterrupt:
    exit(0)
  except Exception as e:
    print(f"{COLOR_MAGENTA}An error occurred: {e}{COLOR_RESET}")
    sys.exit(1)


if __name__ == "__main__":
  main()