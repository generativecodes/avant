from time import time

class timer:
    def __init__(self, loop=None, warp = 1):
        self.passed = 0
        self.state  = time()
        self.loop = loop
        self.warp = warp

    def tick(self, warp=None):
        if(warp):
            self.warp = warp
        now = time()
        self.passed += (now - self.state) * self.warp
        self.state = now

    def get(self):
        if(self.loop):
            return self.passed % self.loop
        else:
            return self.passed

    def set_warp(self, warp):
        self.warp = warp
