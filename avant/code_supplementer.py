class code_supplementer():
    """supplement needed things into the users code"""

    def __init__(self, code):
        self.code = code

    def run(self):
        init_args = "    ctx = args[0]\n" +\
                    "    globals().update(kwargs)\n"

        self.replace_line("def setup():",
                "def setup(*args, **kwargs):\n"+init_args)

        self.replace_line("def loop():",
                "def loop(*args, **kwargs):\n"+init_args)

    def get(self):
        return "".join(self.code)

    def replace_line(self, old, new):
        for i, line in enumerate(self.code):
            if old in line:
                self.code[i] = new

    def add_at_line(self, line, new_code):
        before = self.code[:line+1]
        after  = self.code[line+1:]
        self.code = before  + new_code + after
