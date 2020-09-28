# CS341 Lab 1

This directory contains two python files, `server.py` and `client.py`

The server is a web server implemented in `flask`. It has 3 endpoints. `/hello_word`, `/hash`, and `/collatz`. For detailed specification, check out the PDF file.
The client sends requests to the endpoints of the server.

To install dependencies:
```bash
pip install -r requirements.txt
```

To run the files:
```bash
python server.py
python client.py http://localhost:5000 summer 5
```
