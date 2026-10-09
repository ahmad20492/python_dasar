# pip & Virtual Environment

pip      : pengelola paket bawaan Python
PyPI     : gudang paket open source
venv     : lingkungan terisolasi per proyek

## Perintah (Windows)
python -m venv .venv
.venv\Scripts\activate
pip install pandas requests
pip freeze > requirements.txt
pip install -r requirements.txt