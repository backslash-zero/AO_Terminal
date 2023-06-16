# What is it?
Server.py runs a TCP server to send the _Answer_ to the _Question_.
!['screenshot of the terminal'](/files/img/screenshot.png)

# How to use
```
python server.py --port 7653
```

you can enter `exit` to quit the server

For use on a network with differenet machines:
- find out the ip of the machine running the server
- run the client on the other machine with the ip of the server
- run the server with the ip of the server with the `--host` flag

## Flags
- `--host `: to specify the host to listen on (default: localhost) `python server.py --host localhost --port 7653` 
- `--port` : to specify the port to listen on (default: 7654) `python server.py --port 7653` 
- `--debug` : to enable debug mode (default: False) `python server.py --debug true` 
- `--prefix` : to specify the answer prefix (default: "➜ ") / can be anystring `python server.py --prefix "zum beispiel!: "` 