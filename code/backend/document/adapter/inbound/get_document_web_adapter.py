from flask import Flask, jsonify

from document.application.domain.model.document_id import DocumentID
from document.application.ports.inbound.get_document_uc import GetDocumentUC


class GetDocumentWebAdapter:
    def __init__(self, app: Flask, get_document_uc: GetDocumentUC):
        self.get_document_uc = get_document_uc
        app.add_url_rule(rule="/api/document/<int:requested_document_id>", methods=['GET'], endpoint=self.__class__.__name__,
                         view_func=self.__adapt__)

    def __adapt__(self, requested_document_id: int):
        if not requested_document_id:
            return jsonify({"error": "Document ID is required"}), 400
        try:
            document_id = DocumentID(requested_document_id)
        except ValueError:
            return jsonify({"error": "Invalid document ID"}), 400

        document = self.get_document_uc.get(document_id)

        if document is None:
            return jsonify({"error": f"Document {requested_document_id} not found"}), 404

        return jsonify(document)
