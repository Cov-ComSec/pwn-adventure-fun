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

var player_start_addr = ptr(game_world.add(216)).readPointer();
var player_location = player_start_addr.sub(168);
var Vector3 = Memory.alloc(12); // to store the vector3s
Player.mem_location = player_location;

var set_player_pos = Module.findExportByName("libGameLogic.so", "_ZN5Actor11SetPositionERK7Vector3");
console.log("Actor::SetPosition() @ " + set_player_pos);
var setPosition = new NativeFunction(set_player_pos, 'void', ['pointer', 'pointer']);

function teleport(x, y, z)
{
    Memory.writeFloat(Vector3, x);
    Memory.writeFloat(ptr(Vector3).add(4), y);
    Memory.writeFloat(ptr(Vector3).add(8), z);
    setPosition(Player.mem_location, Vector3);wd
}

console.log("Egg 1: -25045.0, 18085.0, 260.0");
teleport(-25045.0, 18085.0, 260.0);
