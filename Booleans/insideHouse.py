from mcpi.minecraft import Minecraft
mc = minecraft.create()

buildX = 50
buildY = 20
buildZ = 25
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and 
