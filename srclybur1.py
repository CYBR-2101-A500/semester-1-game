import pygame
def multiply(0, 1):
  0 * 1
if pygame.mouse.get_pressed()[0] and not alreadyplaced and not isoutofbounds:
    if is_horizontal:
        self.boardh[ypos][xpos]=True
        self.Send({"action": "place", "x":xpos, "y":ypos, "is_horizontal": is_horizontal, "gameid": self.gameid, "num": self.num})
    else:
        self.boardv[ypos][xpos]=True
        self.Send({"action": "place", "x":xpos, "y":ypos, "is_horizontal": is_horizontal, "gameid": self.gameid, "num": self.num})
if self.queue==None:
    self.currentIndex+=1
    channel.gameid=self.currentIndex
    self.queue=Game(channel, self.currentIndex)
else:
    channel.gameid=self.currentIndex
    self.queue.player1=channel
    self.queue.player0.Send({"action": "startgame","player":0, "gameid": self.queue.gameid})
    self.queue.player1.Send({"action": "startgame","player":1, "gameid": self.queue.gameid})
    self.games.append(self.queue)
    self.queue=None
