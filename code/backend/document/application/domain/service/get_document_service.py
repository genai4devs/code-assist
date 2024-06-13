from typing import Optional

from document.application.domain.model.document_id import DocumentID
from document.application.ports.inbound.document_to import DocumentTO
from document.application.ports.inbound.get_document_uc import GetDocumentUC


class GetDocumentService(GetDocumentUC):
    def get(self, document_id: DocumentID) -> Optional[DocumentTO]:
        return DocumentTO(
            id=document_id.value,
            content="Dummy Document",
        )
