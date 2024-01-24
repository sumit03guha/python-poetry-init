# Python Poetry Init Project

This project demonstrates the use of Poetry for managing Python dependencies and packaging. It includes an example application managed with Poetry, along with documentation on how to use Poetry and the advantages it offers.\

**Go to [init_poetry.md](./init_poetry.md) to setup and start using poetry.**

## Documentation

- [init_poetry.md](./init_poetry.md): Provides detailed instructions on how to install and use Poetry.
- [why_poetry.md](./why_poetry.md): Explains the advantages and key features of using Poetry for Python dependency management and packaging.

## Project Structure

```shell
python-poetry-init/
┣ .gitignore        # Git ignore file
┣ app.py            # Sample Python application
┣ poetry.lock       # Lock file for deterministic builds
┣ pyproject.toml    # Configuration file for Poetry
┣ init_poetry.md    # Documentation on how to initialise and use Poetry
┗ why_poetry.md     # Documentation on the benefits of using Poetry
```

## Getting Started

To get started with this project, you need to have Poetry installed on your system. You can find the installation instructions in `init_poetry.md`.

### Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/your-username/python-poetry-init.git
   ```

2. Navigate to the project directory:

   ```shell
   cd python-poetry-init
   ```

3. Install dependencies using Poetry:

   ```shell
   poetry install --no-root
   ```

### Running the Application

To run the sample application `app.py`, you can use the following steps:

1. Activate the virtual environment managed by Poetry:

   ```shell
   poetry shell
   ```

   This command will spawn a shell within the virtual environment created for your project.

2. Run the application:

   ```shell
   python app.py
   ```

   Inside the Poetry-managed virtual environment, you can run the application directly using Python.

OR

1. The application file can be run directly using the the following Poetry command.

   ```shell
   poetry run python app.py
   ```

### Exiting the Virtual Environment

To exit the virtual environment, simply type `exit` or close the terminal window.
