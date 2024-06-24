


# $GOON 👿 Repository

Welcome to the $GOON 👿 repository! This repository contains various scripts designed to perform different tasks to enhance the $GOON Army. This README file will guide you through the process of setting up Git, downloading the repository, and pushing any changes you make back to the repository. Follow the steps below to get started.

## Table of Contents
1. [Installing Git](#installing-git)
2. [Cloning the Repository](#cloning-the-repository)
3. [Making Changes and Committing](#making-changes-and-committing)
4. [Pushing Changes](#pushing-changes)
5. [Contact](#contact)

## Installing Git

### Windows
1. Download the Git installer from [Git for Windows](https://gitforwindows.org/).
2. Run the installer and follow the on-screen instructions.
3. To check if Git is installed, open the Command Prompt and type:
    ```bash
    git --version
    ```

### macOS
1. Open the Terminal.
2. Install Git using Homebrew by typing:
    ```bash
    brew install git
    ```
3. To check if Git is installed, type:
    ```bash
    git --version
    ```

### Linux
1. Open the Terminal.
2. Install Git using the package manager for your distribution. For example, on Ubuntu, type:
    ```bash
    sudo apt-get update
    sudo apt-get install git
    ```
3. To check if Git is installed, type:
    ```bash
    git --version
    ```

## Cloning the Repository

1. Open your Terminal (or Command Prompt on Windows).
2. Navigate to the directory where you want to clone the repository using the `cd` command. For example:
    ```bash
    cd path/to/your/directory
    ```
3. Clone the repository by typing:
    ```bash
    git clone https://github.com/kevinianbrady/goon.git
    ```
4. Navigate into the cloned repository:
    ```bash
    cd your-repo-name
    ```

## Making Changes and Committing

1. Open the Python files in your favorite text editor or IDE and make your changes.
2. After making changes, you need to stage them for the commit. To stage all changes, type:
    ```bash
    git add .
    ```
   Alternatively, you can stage individual files by specifying their names:
    ```bash
    git add filename.py
    ```
3. Commit your changes with a message describing what you did:
    ```bash
    git commit -m "Your commit message"
    ```

## Pushing Changes

1. To push your committed changes to the repository on GitHub, type:
    ```bash
    git push origin main
    ```
   If you are using a branch other than `main`, replace `main` with the name of your branch.

## Contact

If you encounter any issues or have questions, feel free to open an issue in the repository or contact me at [kevinianbrady@gmail.com](mailto:kevinianbrady@gmail.com).

Happy coding!

---