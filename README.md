# ftp
Basic FTP system built in Python to learn network programming. It includes FTP server and FTP client that communicate over TCP sockets.

Tech Used: Python 3.12.3
Libraries used: 
- socket
- os
- tqdm

Features:
1. Supports multiple clients 
2. Sends any type of file over TCP 
3. Server saves each file in a folder named 'recieved' and duplicate files are saved under unique name
4. Displays a live progress bar in server

To run this on your machine
First, make sure to download the libraries using <br>
```pip install tqdm```

Then start the server (mention how many clients will connect) <br>
Then start the client machines

You can use the test files given to try it out for yourself :3
