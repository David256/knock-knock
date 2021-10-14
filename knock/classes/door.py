class UnknockableDoorError(Exception):
    """
    This exception is raised when try to knock a opened door.
    """
    pass


class Door(object):
    """
    The Door class defines a knockable object.
    """
    def __init__(self, color: int, opened: bool = False) -> None:
        """
        Parameters
        ----------
        color: int
            The color in integer format.
        opened: bool
            Check the door as opened.
        """
        super().__init__()
        self.color = color
        self.opened = opened

    def knock(self):
        """
        Lets knock the door.
        """
        if self.opened:
            raise UnknockableDoorError('Cannot knock the door.')
        print('The door is knocked')
