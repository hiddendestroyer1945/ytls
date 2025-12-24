YouTube Search Engine (Last 12 Months)

A professional, terminal-based Python tool designed for Linux administrators and developers to filter YouTube content by time and relevance. This tool extracts videos uploaded within the last year and lists them in ascending order.
📋 Prerequisites

Before you begin, ensure you have the following installed on your Linux system:

    Python 3 (Version 3.8+)

    Git

    python3-venv

    ca-certificates (Critical for SSL/HTTPS connection to YouTube)

🛠️ Installation & Setup

Follow these steps to get the environment ready and run the program:
1. Update System & Install Dependencies

Open your terminal and run:
Bash

sudo apt update
sudo apt install python3 git python3-venv ca-certificates -y

2. Clone the Repository
Bash

git clone <your-repository-link-here>
cd ytls/

3. Set Up the Virtual Environment

To prevent dependency conflicts (especially with httpx), create and activate a virtual environment:
Bash

# Create the environment
python3 -m venv ytls_env

# Activate the environment
source ytls_env/bin/activate

4. Install Required Packages

Use the requirements.txt file to install the specific versions needed to avoid the "proxy" error:
Bash

pip install -r requirements.txt

💻 Usage

Once the environment is activated, run the program using:
Bash

python3 youtube_search.py

How to use:

    Enter your keyword: Type the topic you want to search for.

    Filter Logic: The program automatically applies a "This Year" filter (EgQIAhAB).

    Output: Results are displayed in ascending order (oldest of the year to newest) with:

        Video Title

        Direct YouTube URL

        Relative Upload Time (e.g., 5 months ago)

To exit the virtual environment when finished:
Bash

deactivate

⚠️ Important Note on Dependencies

This program requires a specific version of the httpx library to function correctly with the YouTube search API. Ensure your requirements.txt contains:

    Youtube-python==1.6.6

    httpx==0.24.1

Contributing

Feel free to modify and improve the search filters. Pull requests are welcome!
License

GNU General Public License v3.0
Author

hiddendestroyer1945