# Adventure 1: HelloMinecraftWorld.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

#Chapter 1: IMPORTANT NOTE - You should copy the individual code file to the MyAdventures folder and run it from there as the programs will need the api's and libraries which are held in the MyAdventures/mcpi folder.

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft World")
