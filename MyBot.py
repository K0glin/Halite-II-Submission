import hlt
import logging
from spaceship import Spaceship
from command_center import CommandCenter
from collections import defaultdict

game = hlt.Game("Cok3Zer0")
logging.info("Starting Zer0-Bot")

fighters = defaultdict(Spaceship)
cc = CommandCenter()

#turn = 0
while True:
    game_map = game.update_map()
    cc.set_map(game_map)

    command_queue = []
    for ship in game_map.get_me().all_ships():
        fighter = fighters[ship.id]
        fighter.set_position(ship.x, ship.y)

    for ship in game_map.get_me().all_ships():

        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            # fighters.pop(ship.id)
            continue

        target = cc.select_target(ship)
        fighter = fighters[ship.id]

        obstacles = game_map.all_planets()
        if isinstance(target.entity, hlt.entity.Planet):
            obstacles.remove(target.entity)
            if ship.can_dock(target.entity):
                #fighter.velocity=Vector(0,0)
                command_queue.append(ship.dock(target.entity))
                continue

        target_point = ship.closest_point_to(target.entity)
        fighter.set_target(target_point.x, target_point.y)
        navigate_command = ship.navigate(
            target_point,
            game_map,
            speed=int(hlt.constants.MAX_SPEED),
            ignore_ships=False)
        #other_fighters_position = [fighters[k] for k in fighters.keys() if k != ship.id]
        #fighter.update(other_fighters_position, obstacles)
        if navigate_command:
            command_queue.append(navigate_command)

    game.send_command_queue(command_queue)
    # TURN END
    #turn += 1
# GAME END
