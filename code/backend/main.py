import os

from flask import Flask

from document.adapter.inbound.get_document_web_adapter import GetDocumentWebAdapter
from document.application.domain.service.get_document_service import GetDocumentService

app = Flask("Sample API")

GetDocumentWebAdapter(app, GetDocumentService())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
