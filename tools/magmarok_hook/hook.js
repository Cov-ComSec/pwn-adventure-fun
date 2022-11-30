var Player = {
    m_walkingSpeed : 200,
    mem_location: 0,
    lastX : null,
    lastY : null,
    flying: false,
    current_position: [0,0,0],
    previous_position: [0,0,0],
};

var game_world_location = Module.findExportByName("libGameLogic.so", "GameWorld");
var game_world = ptr(game_world_location).readPointer()
console.log("GameWorld: " + game_world);

var player_start_addr = ptr(game_world.add(216)).readPointer();
var player_location = player_start_addr.sub(168);
var Vector3 = Memory.alloc(12); // to store the vector3s
Player.mem_location = player_location;
console.log("Player: " + player_location);

// Useful for storing the player's position when in useful places
var get_player_pos = Module.findExportByName("libGameLogic.so", "_ZN5Actor11GetPositionEv");
console.log("Actor::GetPosition() @ " + get_player_pos);
var getPosition = new NativeFunction(get_player_pos, ['float', 'float', 'float'], ['pointer']);

// Used to teleport the player
var set_player_pos = Module.findExportByName("libGameLogic.so", "_ZN5Actor11SetPositionERK7Vector3");
console.log("Actor::SetPosition() @ " + set_player_pos);
var setPosition = new NativeFunction(set_player_pos, 'void', ['pointer', 'pointer']);

function get_position()
{
    var player_pos = getPosition(Player.mem_location);
    return [player_pos[0], player_pos[1], player_pos[2]];
}

function teleport(x, y, z)
{
    Memory.writeFloat(Vector3, x);
    Memory.writeFloat(ptr(Vector3).add(4), y);
    Memory.writeFloat(ptr(Vector3).add(8), z);
    setPosition(Player.mem_location, Vector3);
}


var magmarok_tick = Module.findExportByName("libGameLogic.so", "_ZN8Magmarok4TickEf");
console.log("Magmarok::Tick @ " + magmarok_tick);

var magmarok_damage = Module.findExportByName("libGameLogic.so", "_ZN8Magmarok6DamageEP6IActorP5IItemi10DamageType")
console.log("Magmarok::Damage @ " + magmarok_damage);


Interceptor.attach(magmarok_damage,
    {
        onEnter: function (args)
        {
            // var counter = counter + 1;
            console.log("FOOBAR");
            var thiscall_ptr = parseInt(ptr(this.context.rdi));
            console.log("Magmarok: 0x" + thiscall_ptr);
            var health = ptr(thiscall_ptr + 0x38).readInt();

            console.log("Health: " + health);
        }
    });
    



// teleport(-6151.12255859375,-11611.8310546875,10528.150390625) // location of safe zone
teleport( 55625.84375,-8282.11328125,1491.6494140625); // location of magmarok cave

