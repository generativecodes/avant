from avant.vector import Vector
from avant.forms import *
from avant.timer import timer
from avant.code_supplementer import code_supplementer

class code_executer():
    """Execute the code written by the user."""

    def __init__(self, path):
        """Initialise Code-Executer

        path -- The Filepath to the user code.
        """
        with open(path) as f:
            self.code = [line for line in f]
        self.supplementer = code_supplementer(self.code)
        self.setup_executed = False

    def run(self):
        self.supplementer.run()
        exec(self.supplementer.get())
        self.var_and_fnc = locals()
        self.setup = self.var_and_fnc["setup"]
        self.loop = self.var_and_fnc["loop"]

    def display(self, ctx, width, height):
        settings_init_context(ctx)
        forms_init_context(ctx)
        self.var_and_fnc.update([ ("WIDTH",width),
                                  ("HEIGHT",height),
                                  ("SIZE",size())   ])
        ctx.translate(width/2, height/2)
        if not self.setup_executed:
            self.setup(*(ctx,),**(self.var_and_fnc))
            self.setup_executed = True
        else:
            self.loop(*(ctx,),**(self.var_and_fnc))
