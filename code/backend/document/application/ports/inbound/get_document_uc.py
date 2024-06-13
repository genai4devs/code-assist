from abc import ABC, abstractmethod
from typing import Optional

from document.application.domain.model.document_id import DocumentID
from document.application.ports.inbound.document_to import DocumentTO


class GetDocumentUC(ABC):
    @abstractmethod
    def get(self, document_id: DocumentID) -> Optional[DocumentTO]:
        pass
