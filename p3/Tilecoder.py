﻿import mathnumTilings = 4numTiles = 9*9*4# We get 1.7 from (1.2+0.5) for the position range and we get 0.14 from (0.07+0.07) for the# velocity range. Page 219 of the textbook.def tilecode(pos,vel,tileIndices):    # write your tilecoder here (5 lines or so)	pos = pos + 1.2	vel = vel + 0.07	for n in range(0, numTilings):		distPos = pos + n*(1.8/8)/numTilings		distVel = vel + n*(0.14/8)/numTilings				tileIndices[n] = int(n*(9*9) + math.floor((distPos/(1.8/8)))+ 9*math.floor((distVel/(0.14/8))))#F = [-1]*numTilings#tilecode(-0.4, 0.0, F)#print F