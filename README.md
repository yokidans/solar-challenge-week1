# solar-challenge-week1
## **Setup Instructions**
1. Clone the repo:
   ```bash
   git clone https://github.com/yokidans/solar-challenge-week1.git
   cd solar-challenge-week1

## Environment Setup

### Prerequisites
- Python 3.9+ ([Download](https://www.python.org/downloads/))
- Git ([Download](https://git-scm.com/))
- VS Code (Recommended) ([Download](https://code.visualstudio.com/))

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python -c "import pandas as pd; print(pd.__version__)"
# Should output: 1.5.2
```

### 5. Run Jupyter Notebooks (Optional)
```bash
pip install jupyter
jupyter notebook
```

### Folder Structure
```
solar-challenge-week1/
├── .github/workflows/  # CI/CD pipelines
├── notebooks/          # EDA and analysis
├── src/                # Python modules
├── tests/              # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
```

### Troubleshooting
- **`python` not found**: Use `python3` instead
- **Permission errors**: Add `--user` flag to pip commands
- **VS Code integration**:  
  Press `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose `.venv`
   
