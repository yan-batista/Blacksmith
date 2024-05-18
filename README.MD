# Blacksmith

Blacksmith is a Python script designed to streamline the initiation of a React TypeScript project with TailwindCSS, ESLint, and Prettier, following a predefined base configuration.

## Features

- **React TypeScript**: Sets up a React project using TypeScript.
- **TailwindCSS**: Integrates TailwindCSS for utility-first CSS styling.
- **ESLint**: Configures ESLint for linting TypeScript and JavaScript files.
- **Prettier**: Sets up Prettier for code formatting, ensuring a consistent style across the project.

## Prerequisites

Before using Blacksmith, ensure you have the following installed:

- Python 3.6 or higher
- Node.js and npm (or yarn)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/blacksmith.git
    cd blacksmith
    ```
2. **Download**

    You can download the executable on the [releases](https://github.com/yan-batista/Blacksmith/releases) page.

## Usage

### Using the Script
If you cloned the repository, to create a new React TypeScript project with TailwindCSS, ESLint, and Prettier, run the Blacksmith script:

```sh
python blacksmith.py -n <project-name>
```

### Using the Executable
If you downloaded the executable from the [releases](https://github.com/yan-batista/Blacksmith/releases) page, you can either open the terminal in the executable folder or add the executable to your PATH variables.

#### Adding to PATH on Windows:
1. Open the System Properties window.
2. Click on "Advanced system settings".
3. Click on the "Environment Variables" button.
4. In the Environment Variables window, select the Path variable in the System Variables section and click "Edit".
5. Add a new line with the Blacksmith executable folder path.
6. Click "OK" on all windows to save your changes.

Then, you can run:
```sh
blacksmith -n <project-name>
```

## Feedback
If you encounter any issues or have suggestions for improvements, please open an [issue](https://github.com/yan-batista/Blacksmith/issues) on GitHub.