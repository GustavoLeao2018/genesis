"""Define behaviors for killable objects."""

from engine import Hideable
from .explosion import Explosion


class Killable(Hideable):
    """Define a behavior for objects that could be killed."""

    def __init__(self, explosion_type, time_scale=1.0):
        """Initialize the object."""
        Hideable.__init__(self)
        self.__explosion = None
        self.__dying = False
        self.__type = explosion_type
        self.__time_scale = time_scale

    @property
    def should_update(self):
        """Check if object should be updated."""
        return self.is_alive

    @property
    def is_alive(self):
        """Check if killable object is still alive."""
        return self.visible and not self.__dying

    def update(self, bounds):
        """Update explosion."""
        if self.__dying:
            self.__explosion.update(bounds)
            if not self.__explosion.visible:
                self.__dying = False
                self.hide()

    def draw(self, screen):
        """Draw explosion."""
        if self.__dying:
            self.__explosion.draw(screen)

    def die(self):
        """Mark object to die."""
        self.__dying = True
        self.__explosion = Explosion(self.position, self.__type,
                                     time_scale=self.__time_scale)

    def respawn(self):
        """Respawn player."""
        self.__dying = False
