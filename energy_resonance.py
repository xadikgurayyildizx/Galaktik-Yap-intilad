from ursina import *
import math

app = Ursina()
window.color = color.black
camera.orthographic = True
camera.fov = 10

energy = 0
time_flow = 0

core = Entity(
    model='circle',
    color=color.white,
    scale=0.4
)

ground = Entity(
    model='quad',
    y=-4,
    scale=(20,1),
    color=color.white33
)

def update():
    global energy, time_flow

    time_flow += time.dt

    # enerji doğal olarak düşer
    energy *= 0.97

    # rezonans hareketi
    core.y = math.sin(time_flow * 2) * (0.5 + energy * 0.2)

    # nefes alan ölçek
    core.scale = 0.4 + math.sin(time_flow * 4) * 0.05

def input(key):
    global energy
    if key == 'space':
        energy = min(energy + 1, 6)
        print("ENERGY:", round(energy, 2))

app.run()
