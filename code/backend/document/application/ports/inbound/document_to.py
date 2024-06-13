from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentTO:
    id: int
    content: str

    def __post_init__(self):
        if not isinstance(self.id, int):
            raise ValueError("ID must be an integer.")
        if not isinstance(self.content, str):
            raise ValueError("Content must be a string.")
