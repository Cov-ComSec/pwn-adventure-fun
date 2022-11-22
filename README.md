# Pwn Adventure Fun

Infrastructure and tools built for the 4-week Pwn Adventure 3 hacking sessions for ComSec

## Tools Created

- [Running Speed Binary Patch](./tools/patch_speed/): 
    - Description: Permanently increase running speed.
    - Author: @sharkmoos
- [Infinite Jump Binary Patch](./tools/patch_jump/)
    - Description: Why have double jump when you can infinite jump!
    - Author: @sharkmoos

## Accessing the Server

### Connecting to the Server

The server is running with a hostname `game.pwn3`, so you'll need to add this to your `/etc/hosts` file with the IP of the server. For Windows, I think it's `C:\Windows\System32\drivers\etc\hosts`. 

### Default Team Creds

hash: `db1e797da308f027c876c61786682f3b`

## Running on Linux in 2022

Obviously things have progressed since PwnAdventure 3 first released. You may have noticed `libssl.so.1.0.0` and `libcrypto.so.1.0.0` are required but not available on the Ubuntu package manager now. To overcome this, you can do the following:

```bash
cd ./PwnAdventure3/PwnAdventure3/Binaries/Linux/
# download a valid one from http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/
wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5.10_amd64.deb
dpkg-deb -xv libssl1.0.0_1.0.2n-1ubuntu5.10_amd64.deb .
cp ./usr/lib/x86_64-linux-gnu/* .
sudo ./PwnAdventure3-Linux-Shipping
```

## Mouse Pointer Issues

Some users have had trouble using their mouse in Pwn Adventure, the camera does't bind to the mousee. We have 2 solutions for this:

1. If running in a VM, try enabling "optimise the mouse for games"
    - On VMWare Workstation `edit -> preferences -> input -> optimise mouse for games = always`
2. Rebind the Up and Down arrow keys to control the camera. We will post a valid file for this in the near future

## Infrastructure Notes

There are three containers in the stack

- `postgres_database`: The database container. Just uses alpine with postgres, no commands are run directly on this server, but holds volumes on `/var/lib/postgresql/data` for data and `/var/run/postgresql` for connection sockets
- `pwn3_master`: This one basically handles game data, so accounts, mission progress and all that stuff. This is the container that interacts with the database running on `postgres_database`.
- `pwn3_game`: The actual game logic. It's currently set to handle 10 instances, I have no idea if there is a suggested limit beyond apart from the obvious requirements of the host server. This is the container the players should connect to directly
