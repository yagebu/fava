from fava.beans.ingest import BeanImporterProtocol

class Importer(BeanImporterProtocol):
    def name(self):
        return "duplicate"

    def identify(self, file):
        return True

    def file_account(self, file):
        return "Assets:Test"

CONFIG = [Importer(), Importer()]
