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
// console.log("GameWorld: " + game_world);

var player_start_addr = ptr(game_world.add(216)).readPointer();
var player_location = player_start_addr.sub(168);
var Vector3 = Memory.alloc(12); // to store the vector3s
Player.mem_location = player_location;
// console.log("Player: " + player_location);
var get_player_pos = Module.findExportByName("libGameLogic.so", "_ZN5Actor11GetPositionEv");
var getPosition = new NativeFunction(get_player_pos, ['float', 'float', 'float'], ['pointer']);

// Used to teleport the player
var set_player_pos = Module.findExportByName("libGameLogic.so", "_ZN5Actor11SetPositionERK7Vector3");
var setPosition = new NativeFunction(set_player_pos, 'void', ['pointer', 'pointer']);

function teleport(x, y, z)
{
    Memory.writeFloat(Vector3, x);
    Memory.writeFloat(ptr(Vector3).add(4), y);
    Memory.writeFloat(ptr(Vector3).add(8), z);
    setPosition(Player.mem_location, Vector3);
}

console.log("Eggs 4: 60453.0, -17409.0, 2939.0");
teleport(60453.0, -17409.0, 2939.0);
