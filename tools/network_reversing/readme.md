# Notes on Pwn Adventure Protocol

## Ongoing Observations

- Packets are variable length
- Little endian
- Multiple packets can be sent in a single request

### Delimiters

If packets of the same type are variable length, there must be some kind of delim. Probably one of the following

- Delim is a defined byte
- Delim is defined on the fly with some data at a special location

All packets seem to end in "\x00\x00\x00", but this string is also found in the middle of packets. So it is not a delim.

An example location packet seems to be:

```
6d7698211bc76db39dc648dd1d45dc02bbf900000000
```

(the main hint was that 0x6d76 == 'mv') Jumping up and down, 4 bytes seem to change. This could be the Z axis?

```
                    |---Z----|
6d7698211bc76db39dc6 48dd1d45 dc02bbf900000000
```

Moving around a little, the other bytes that change are below. 

```
     |---X----||---Y----||---Z----|
6d76  98211bc7  6db39dc6  48dd1d45 dc02bbf900000000
```

Moving the camera without moving the player changes another set of bytes. Video games often use [aircraft axis](https://en.wikipedia.org/wiki/Aircraft_principal_axes)
so perhaps its those 

```
     |---X----||---Y----||---Z----||-R--|--P-|--Y--|
6d76  98211bc7  6db39dc6  48dd1d45  dc02 bbf9 0000  0000
```

So moving forward or backward, the penultimate byte toggles between 2 values. This could be the forward/backward codes.

```
Forward:  0x7f
Backward: 0x81
Left:     0x7f
Right:    0x81
```

This is it then, and the first bytes are almost certainly the packet type/id

```
|-id-] |---X----||---Y----||---Z----||-R--|--P-|--Y--||F/B||L/R|
 6d76   98211bc7  6db39dc6  48dd1d45  dc02 bbf9 0000    00  00
```

This doesn't explain the delimiter problem though. Perhaps only packets with variable length have delims. Will try another type

This looks like the first packet on a stacked stream of packets. It was sent during when I logged in and part decodes to
`GreatBallsOfFire`, so its probably the location/init packet for the fire spell. This must be variable length
as not all spells are the same length

Something must say the length...

Looking at another packet, just before the string there is a one byte value that is not the same for both.

length of the string is 13, which matches 0xc. So the delim is the string length directly before the string.

```
|-op-| |-id-||------?------||length||---------String------------|
 6d6b   0200  0000000000000   00c0   04c6f7374436176654275736800 2351c700d62cc70000b34300000000000064000000
```

Since its a init packet, it would make sense for there to be coordinates.

Going to the great balls of fire spell in the game, I can get my coords to nearly match the ones in this packet. tells where the 
coords are.

```
|-op-| |-id-||------?------||length||---------String------------||---X----||---Y----||---Z--||-R--|--P-|--Y--|
 6d6b   0200  0000000000000   00c0    04c6f7374436176654275736800  2351c700  d62cc700 00b34300 0000 0000  0064   000000
```

So that lets me create a decode function for packets that create elements.. Usefulfor the egg hunting mission I bet. 

With an understanding of how fixed and variable length packets work, finding out the others should be simple enough
