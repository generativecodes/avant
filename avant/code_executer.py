from avant.vector import Vector
from avant.forms import *

make_functions_global =[
        "global setup\n",
        "global loop\n",
        ]

init_w_and_h_and_center_picture = [
        "    surface = ctx.get_target()\n",
        "    width = surface.get_width()\n",
        "    height = surface.get_height()\n",
        "    ctx.translate(width/2, height/2)\n",
        ]

init_context_everywhere = [
        "    forms_init_context(ctx)\n",
        "    settings_init_context(ctx)\n",
        ]

class code_executer():

    def __init__(self, path):
        with open(path) as f:
            self.code = [line for line in f]
        self.add_at_line(3, make_functions_global)
        loop_inits =  init_context_everywhere
        loop_inits += init_w_and_h_and_center_picture
        self.add_to_function("def loop(ctx):",
                start=loop_inits)
        self.ctx = None
        self.var_and_fncs = None
        self.setup = None
        self.loop = None

    def run(self):
        global setup
        global loop
        self.code = "".join(self.code)
        exec(self.code)
        ignore_list = [
                "self",
                "vector",
                "settings",
                "forms",
                "code_executer",
                "animator",
                "main"
                ]
        self.var_and_fnc = locals()
        

        # run from time to time to check if all gets ignored
        #for name in self.var_and_fnc:
        #    print(name)
        #    print(self.var_and_fnc[name], "\n")
        
        self.setup = setup
        self.loop = loop

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
