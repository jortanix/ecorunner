from Util import *
import pytmx
from pytmx.util_pyglet import pyglet_image_loader

key = pyglet.window.key
keys = key.KeyStateHandler()
window = pyglet.window.Window()
window.push_handlers(keys)


map_img = pyglet.resource.image("assets/temp/map_img.png")
map_sprite = pyglet.sprite.Sprite(map_img, 0, 0)
print(map_img.width, map_img.height)

# TMX TEST

# sub_img = map_img.get_region(0, 0, window.width, window.height)

# tmx_data = pytmx.TiledMap("map.tmx", image_loader=pyglet_image_loader, allow_duplicate_names=True)
# tile_width = tmx_data.tilewidth
# tile_height = tmx_data.tileheight
# map_width = tmx_data.width
# map_height = tmx_data.height

# batch = pyglet.graphics.Batch()
# tiles = {}

# layers = 0
# for layer in tmx_data.visible_layers:
#     layers+=1
#     for x, y, gid in layer:
#         tile = tmx_data.get_tile_image_by_gid(gid)
#         if tile:
#             sprite = pyglet.sprite.Sprite(
#                 tile,
#                 x = x * tile_width,
#                 y=(map_height - y - 1) * tile_height,
#             )
#             sprite.base_x = x * tile_width
#             sprite.visible = False
#             sprite.batch = batch
#             tiles[(layer.id, x, y)] = sprite

# print(window.width, window.height)

camera_x = 0
visibleTiles = []
x = 0

v = 0


def step(dt):
    global camera_x

    if (keys[key.A] or keys[key.LEFT]):
        camera_x += clamp(1*MOVEMENT_SPEED_2*dt,0,MAX_X_VELOCITY[1])

    elif (keys[key.D] or keys[key.RIGHT]):
        camera_x += -clamp(1*MOVEMENT_SPEED_2*dt,0,MAX_X_VELOCITY[1])

    camera_x = clamp(camera_x, -(map_img.width - window.width), 0)
    map_sprite.x = camera_x

    # TMX TEST

    # sub_img.delete()
    # sub_img = map_img.get_region(camera_x, 0, window.width, window.height)

    # for tile in visibleTiles:
    #     tile.visible = False
    
    # min_x = int(camera_x // tile_width)
    # max_x = int((camera_x + window.width)//tile_width + 1)

    # visibleTiles = []
    # for layerNum in range(1, 3):
    #     for tile_x in range(min_x, max_x):
    #         for tile_y in range(85,106):
    #             tile = tiles.get((layerNum, tile_x, tile_y))
    #             if tile:
    #                 tile.x = tile.base_x - camera_x
    #                 tile.visible = True
    #                 visibleTiles.append(tile)

    v = 1
    # for i in range(window.width//tile_width):
    #     for j in range(window.height//tile_height):
            
        
@window.event
def on_draw():
    window.clear()
    map_sprite.draw()

pyglet.clock.schedule_interval(step, 1/MAX_FPS)

pyglet.app.run()