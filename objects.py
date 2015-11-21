class Lockbox():
    KEY = "Open please!"

    def __init__(self, contents):
        self.contents = contents
        # The .locked variable is not private. The double underscore
        # means the variable name is mangled which effectively makes it private.
        # but a determined programmer can access it.
        self.__locked = True

    # @property turns the "locked" property into a getter method
    @property
    def locked(self):
        if self.__locked:
            return True
        else:
            return False
    # Because I established locked as a property I am able to create a setter
    # method.
    @locked.setter
    def locked(self, should_lock):
        if should_lock:
            self.__locked = True

    def unlock(self, proposed_key):
        if proposed_key == self.KEY:
            self.__locked = False

    def print_contents(self):
        if self.__locked:
            print("Sorry, the box is locked.")
        else:
            print(self.contents)



sample_box = Lockbox("Super secret contents!!!")
print(sample_box.locked)
sample_box.locked = False
sample_box.print_contents()
sample_box.unlock("Open please!")
sample_box.print_contents()
sample_box.locked = True
sample_box.print_contents()