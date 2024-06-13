class DocumentID:
    """
    A value object representing a document ID.

    Attributes:
        value (int): The document ID.

    Raises:
        ValueError: If the ID is not a valid string.
    """

    def __init__(self, document_id: str | int):
        if isinstance(document_id, str):
            try:
                self.value = int(document_id)
            except ValueError:
                raise ValueError("Document ID must be a string that can be converted to an integer.")
        elif isinstance(document_id, int):
            self.value = document_id
        else:
            raise ValueError("Document ID must be a string or an integer.")

    def __eq__(self, other):
        if not isinstance(other, DocumentID):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"DocumentID(id='{self.value}')"
