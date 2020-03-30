from avant.vector import Vector
from avant.forms import *

make_functions_global =[
        "global setup\n",
        "global loop\n",
        "global WIDTH, HEIGHT\n",
        ]

init_w_and_h_and_center_picture = [
        "    surface = ctx.get_target()\n",
        "    global WIDTH, HEIGHT\n",
        "    WIDTH = surface.get_width()\n",
        "    HEIGHT = surface.get_height()\n",
        "    ctx.translate(WIDTH/2, HEIGHT/2)\n",
        "    SIZE = size()\n",
        ]

init_context_everywhere = [
        "    ctx = args[0]\n",
        "    globals().update(kwargs)\n",
        "    forms_init_context(ctx)\n",
        "    settings_init_context(ctx)\n",
        ]

class code_executer():
    """a class that uses exec"""
    def __init__(self, path):
        with open(path) as f:
            self.code = [line for line in f]
        self.replace_line(
                "def setup():\n",
                "def setup(*args, **kwargs):\n",
                )
        self.replace_line(
                "def loop():\n",
                "def loop(*args, **kwargs):\n",
                )
        self.add_at_line(2, make_functions_global)
        loop_inits =  init_context_everywhere
        loop_inits += init_w_and_h_and_center_picture
        self.add_to_function("def loop(*args, **kwargs):",
                start=loop_inits)
        self.var_and_fnc = None
        self.setup = None
        self.setup_executed = False
        self.loop = None

    def loop_(self, ctx):
        self.loop(*(ctx,),**(self.var_and_fnc))

    def setup_(self, ctx):
        if not self.setup_executed:
            self.setup(*(ctx,),**(self.var_and_fnc))
            self.setup_executed = True

    def run(self):
        global setup
        global loop
        self.code = "".join(self.code)
        exec(self.code)
        self.var_and_fnc = locals()
        self.setup = setup
        self.loop = loop

    def replace_line(self, old, new):
        for i,line in enumerate(self.code):
            if old in line:
                self.code[i] = new

    def add_at_line(self, line, new_code):
        before = self.code[:line+1]
        after  = self.code[line+1:]
        self.code = before  + new_code + after

    def add_to_function(self, name,
                        start = None, end = None,
                        mid = None, mid_idx = 0 ):
        start_idx = 0
        end_idx = 0
        for i, line in enumerate(self.code):
            if name in line:
                start_idx = i
                mid_idx = i + mid_idx
            if start_idx is not 0:
                if  line[0] is not "\t" and \
                    line[0] is not " ":
                    end_idx = i
        if(start): self.add_at_line(start_idx, start)
        if(mid):   self.add_at_line(mid_idx, mid)
        if(end):   self.add_at_line(end_idx, end)
