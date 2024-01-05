from enum import Enum

class CategoryStateUser(Enum):
    """Enum class for category state depending on user."""
    NOT_STARTED = 0
    TO_UPLOAD = 1
    TO_VOTE = 2
    FINISHED = 3
    UPLOADED = 4
    VOTED = 5

    def __str__(self):
        return self.name