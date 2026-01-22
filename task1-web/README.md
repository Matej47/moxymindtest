1. Clone the repo
2. Create a virtual environment

   python3 -m venv .venv
   source .venv/bin/activate  # Linux / Mac
   .venv\Scripts\activate     # Windows

    pip install -r requirements.txt
    edit .env.example and rename it to .env
    
    pytest -v
    pytest tests/ --html=report.html --self-contained-html