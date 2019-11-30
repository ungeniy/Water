from time import  sleep
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
for sec in range(1,21):
    pos = mc.player.getPos()
    mc.setBlock(pos.x,pos.y - 1,pos.z,8)
    mc.postToChat(str(sec))
    sleep(1)