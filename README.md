# Foreign Exchange Project

Foreign Exchange Project is a desktop currency exchange application developed with Python and PySide6.  
The application allows users to register, log in, view live exchange rates, select a base currency, buy currencies, and track their portfolio.

## Features

- User login and registration system
- Single-window GUI flow using PySide6
- Live exchange rate data via Fixer.io API
- Base currency selection
- Dynamic currency rate display
- Buy operation with confirmation dialog
- Insufficient balance warning
- User portfolio display
- Profile photo support
- SQLite database support
- Loading screen while fetching exchange rates
- Packaged Windows executable support with PyInstaller

## Technologies Used

- Python
- PySide6
- SQLite
- Fixer.io API
- Requests
- python-dotenv
- PyInstaller

## Project Structure

```text
Foreign_Exchange_Project/
├── API/
├── assets/
├── Classes/
├── DataBase/
├── Exchange/
├── GUI/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Foreign_Exchange_Project.git
cd Foreign_Exchange_Project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

This project uses the Fixer.io API.  
You need to create a `.env` file in the project root.

Create a file named:

```text
.env
```

Then add your Fixer.io API key:

```env
FIXER_API_KEY=your_fixer_api_key_here
```

An example file is provided as:

```text
.env.example
```

Do not commit your real `.env` file to GitHub.

## Running the Application

After installing the dependencies and creating the `.env` file, run:

```bash
python main.py
```

## Building the Executable

This project can be packaged as a Windows desktop application using PyInstaller.

Recommended build command:

```bash
python -m PyInstaller --noconsole --name FEP --collect-all PySide6 --contents-directory "." --add-data "GUI;GUI" --add-data "assets;assets" --add-data "DataBase;DataBase" --icon "assets/icon.ico" main.py
```

After the build process finishes, the executable will be located in:

```text
dist/FEP/FEP.exe
```

To distribute the application, share the entire `dist/FEP` folder, not only the `.exe` file.

## Notes

- The application creates or uses a local SQLite database.
- The Fixer.io API key is not included in this repository for security reasons.
- If the executable is shared, users must provide their own `.env` file or API key configuration.
- Do not upload `dist/`, `build/`, `.env`, or `.venv` folders to GitHub.

## License

This project is developed for educational and portfolio purposes.
