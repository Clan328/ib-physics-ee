cd ..
call venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser
