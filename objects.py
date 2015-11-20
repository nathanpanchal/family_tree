class Lockbox():
    KEY = "Open please!"

    def __init__(self, contents):
        self.contents = contents
        self.__locked = True

    @property
    def locked(self):
        if self.__locked:
            return True
        else:
            return False

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