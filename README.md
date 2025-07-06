# 🐍 How to Run Python on Windows

Follow these steps to properly install and run Python on a Windows system:

---

### 1. Download and Install Python

- Visit the official Python website:  👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Download the latest version and run the installer.

> ✅ **Important:** Check the box that says **"Add Python to PATH"** during installation.

---

### 2. Verify Environment Variable (PATH)

After installation, confirm that Python is correctly added to your system’s environment variables:

- Open **Command Prompt** and type:

```bash
python --version
```

or

```bash
where python
```

If a version number or path appears, your environment is correctly set up.

---

### 3. Install `pip` (if not already installed)

`pip` (Python's package installer) is usually included with modern Python versions.

If not, follow the official installation guide:👉 [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

To install manually:

1. Download `get-pip.py`
2. Run it with:

```bash
python get-pip.py
```

---

### 4. Install Required Python Packages

Run the following commands in Command Prompt:

```bash
pip install numpy
pip install kanren
```

These install the core libraries needed for the project.

---

### 5. Install Local Package from `.whl` File

If you were given a local `.whl` package file (e.g. `ai_pkg-0.0.1-py3-none-any.whl`), run:

```bash
pip install ai_pkg-0.0.1-py3-none-any.whl
```

> ℹ️ Make sure the `.whl` file is in the current directory, or provide the full path to it.

---

### 💡 Tips

- You can also use tools like **VSCode**, **Jupyter Notebook**, or **IDLE** for running Python more easily.
- Use `pip list` to verify which packages are installed.

---

You are now ready to run Python scripts on Windows! ✨
