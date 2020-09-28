# Lab 2

### About
This lab has 2 tasks. Task 1 is **implementing a client based on a custom specification**, and task 2 is **implementing a server that handles multiple concurrent clients**.

The client connects to a server provided by CS341, sending headers and receiving packets according to the specifications in the PDF.

The server accepts multiple connections from the client binary provided by CS341.

### Requirements
The two python files do not have any external dependencies. These two programs were tested on python 3.6.9 on a Ubuntu 18.04 machine.

### Execution
To run files for each task:

```bash
# Task 1
python client.py --host=143.248.56.39 --port=4000 --studentID=20200000
```

*Warning*: the client binary in this directory is for a linux machine.
```bash
# Task 2
python server.py --port=1234
./client_linux --port=1234 --studentID=20200000 --submit=False
```
