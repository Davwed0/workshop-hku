# Quick Start Guide

Get started with the Python workshop in 5 minutes!

## Option 1: Automated Setup (Recommended)

### Windows:
```bash
setup.bat
```

### Mac/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

The script will:
- Check Python installation
- Create a virtual environment
- Install all required packages
- Run validation tests
- Confirm everything is ready

## Option 2: Manual Setup

### 1. Create virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install packages:
```bash
pip install -r requirements.txt
```

### 3. Verify installation:
```bash
python test_notebooks.py
```

### 4. Start Jupyter:
```bash
jupyter notebook
```

## Starting the Workshop

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. In your browser, navigate to `notebooks/`

3. Open `01_basics.ipynb` to start!

## Troubleshooting

### "Command not found: python"
- Try `python3` instead of `python`
- Or install Python from https://www.python.org/

### "pip: command not found"
- Try `python -m pip` instead of `pip`

### Import errors in notebooks
- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt --upgrade`

### Jupyter notebook won't start
- Try: `pip install --upgrade jupyter notebook`
- Then: `jupyter notebook`

## Need Help?

- Check the main [README.md](README.md)
- Review [CHEATSHEET.md](CHEATSHEET.md) for Pandas syntax
- Open an issue on GitHub

---

**Ready to learn? Let's go! 🚀**
