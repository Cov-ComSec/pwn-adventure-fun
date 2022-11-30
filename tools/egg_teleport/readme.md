# Good Egg Hunting

If you got the reference, bonus points to you :P

I reverse engineered the network protocol around week 3 of the pwn adventure journey. At time of writing this might not be uploaded to this repo yet, so I'll try to remember to loop back and add a reference. Anyway, with this done the egg locations can be found by doing a traffic capture when spawning into the game and running the data through a script a wrote. The output included this

```
[New Element] ID: 11, Name: b'GoldenEgg1', X: -25045.0, Y: 18085.0, Z: 260.0, R: 0, P: 0, Y: 0
[New Element] ID: 12, Name: b'GoldenEgg2', X: -51570.0, Y: -61215.0, Z: 5020.0, R: 0, P: 0, Y: 0
[New Element] ID: 13, Name: b'GoldenEgg3', X: 24512.0, Y: 69682.0, Z: 2659.0, R: 0, P: 0, Y: 0
[New Element] ID: 14, Name: b'GoldenEgg4', X: 60453.0, Y: -17409.0, Z: 2939.0, R: 0, P: 0, Y: 0
[New Element] ID: 15, Name: b'GoldenEgg5', X: 1522.0, Y: 14966.0, Z: 7022.0, R: 0, P: 0, Y: 0
[New Element] ID: 16, Name: b'GoldenEgg6', X: 11604.0, Y: -13131.0, Z: 411.0, R: 0, P: 0, Y: 0
[New Element] ID: 17, Name: b'GoldenEgg7', X: -72667.0, Y: -53567.0, Z: 1645.0, R: 0, P: 0, Y: 0
[New Element] ID: 18, Name: b'GoldenEgg8', X: 48404.0, Y: 28117.0, Z: 704.0, R: 0, P: 0, Y: 0
[New Element] ID: 19, Name: b'GoldenEgg9', X: 65225.0, Y: -5740.0, Z: 4928.0, R: 0, P: 0, Y: 0
[New Element] ID: 20, Name: b'BallmerPeakEgg', X: -2778.0, Y: -11035.0, Z: 10504.0, R: 0, P: 0, Y: 0
[New Element] ID: 21, Name: b'BallmerPeakPoster', X: -6101.0, Y: -10956.0, Z: 10636.0, R: 0, P: 0, Y: 0
```

With the locations known, we just need to teleport to them. At time of exploit I hadn't figure out how to do automated pickups, so this is semi-automated.

Frida can be used to teleport the player to a new location, so the player just needs to mash the `E` (interact) button to pickup 9 of the eggs. The 10th egg is hidden, so once you hit the final teleport just shoot the picture in the house and then go out onto the balcony the egg is there