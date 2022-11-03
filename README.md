# Pwn Adventure Fun

Infrastructure and tools built for the 4-week Pwn Adventure 3 hacking sessions for ComSec

## Tools Created

- [Example tool](./tools/example_tool): Tool created for x by y

## Accessing the Server

### Connecting to the Server

The server is running with a hostname `game.pwn3`, so you'll need to add this to your `/etc/hosts` file with the IP of the server. For Windows, I think it's `C:\Windows\System32\drivers\etc\hosts`. 

### Default Team Creds

hash: `db1e797da308f027c876c61786682f3b`

## Infrastructure Notes

There are three containers in the stack

- `postgres_database`: The database container. Just uses alpine with postgres, no commands are run directly on this server, but holds volumes on `/var/lib/postgresql/data` for data and `/var/run/postgresql` for connection sockets
- `pwn3_master`: This one basically handles game data, so accounts, mission progress and all that stuff. This is the container that interacts with the database running on `postgres_database`.
- `pwn3_game`: The actual game logic. It's currently set to handle 10 instances, I have no idea if there is a suggested limit beyond apart from the obvious requirements of the host server. This is the container the players should connect to directly
