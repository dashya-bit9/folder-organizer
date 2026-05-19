# 🗂️ AI Folder Organizer

Turn any messy folder into a clean organized system in seconds.
Point it at any folder, AI scans your files, shows you the plan,
then sorts and renames everything automatically.

---

## What It Does

- Scans any folder you choose
- AI understands what each file is and where it belongs
- Shows you the full organization plan before touching anything
- Moves and renames files into clean labeled subfolders
- Works on any folder — Downloads, Desktop, Documents, anywhere

---

## Requirements

You need Python installed on your computer.

Check if you have it by opening terminal and typing:

python --version

If you don't have it, download it free at python.org

---

## Setup (One Time Only)

**Step 1 — Get a free Groq API key**
- Go to console.groq.com
- Sign up free
- Click API Keys and create a new one
- Copy it

**Step 2 — Install the requirements**

Open terminal, navigate to this folder and run:

pip install streamlit groq requests

---

## How To Run It

**Mac/Linux — double click `run.sh`**
Or in terminal:

run.bat

The script installs everything automatically and opens 
the app in your browser. No manual setup needed.

## How To Use It

1. Paste your Groq API key in the sidebar
2. Enter the full path to any messy folder
3. Hit Scan Folder
4. Review the AI organization plan
5. Hit Confirm and watch it organize everything

---

## Finding Your Folder Path

**Windows:**
Open File Explorer, navigate to your folder,
click the address bar at the top, copy the full path.
Example: C:/Users/YourName/Downloads

**Mac:**
Right click your folder, hold Option,
click Copy as Pathname.
Example: /Users/YourName/Downloads

**Linux/Chromebook:**
Open terminal and navigate to your folder, type pwd.
Example: /home/yourname/Downloads

---

## Example

Before:

Downloads/
resume_final_v2_ACTUAL.pdf
screenshot_2024_blurry.png
budget_stuff_march.xlsx
notes_random_misc.txt

After:

Downloads/
Documents/
resume.pdf
Images/
screenshot.png
Spreadsheets/
budget_march.xlsx
Notes/
notes.txt

---

## Built With

- Python
- Streamlit
- Groq AI (llama-3.3-70b-versatile)

---

## Support

Having issues? Email: [ dashyab8@gmail.com ]