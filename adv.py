from room import Room
from player import Player
from world import World
from util import Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# #get opposite direction 
# def get_opposite_direction(direction):
#   if direction == 'n':
#     return 's'
#   elif direction == 's':
#     return 'n'
#   elif direction == 'w':
#     return 'e'
#   elif direction == 'e':
#     return 'w'
  
traversal_path = []

universe = {}

def traverse_path(player, moves):
  #instantiate a BFS
  q = Queue()
  #add first room to q
  q.enqueue([player.current_room.id])
  visited = set()
  
  while q.size() > 0:
    path = q.dequeue()
    latest_path = path[-1]
    
    if latest_path  not in visited:
      visited.add(latest_path)
      
      for exit in universe[latest_path]:
        if universe[latest_path][exit] == '?':
          return path
        else:
          explored = list(path)
          explored.append(universe[latest_path][exit])
          q.enqueue(explored)
  return []





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


######
# UNCOMMENT TO WALK AROUND
######
player.current_room.print_room_description(player)
while True:
   cmds = input("-> ").lower().split(" ")
   if cmds[0] in ["n", "s", "e", "w"]:
       player.travel(cmds[0], True)
   elif cmds[0] == "q":
       break
   else:
       print("I did not understand that command.")
