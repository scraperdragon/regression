class Case(object):
    def __init__(self):
        self.set_up()
        for f in self.run_these:
            print f()

