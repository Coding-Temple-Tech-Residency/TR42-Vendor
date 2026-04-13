from app.extensions import db
from app.blueprints.documents.repositories.repository import DrugTestRepository , BackgroundCheckRepository, ComplianceDocumentRepository




class ComplianceDocumentService:

    @staticmethod
    def get_all_compliance_documents():
        return ComplianceDocumentRepository.get_all()

    @staticmethod
    def get_compliance_document(compliance_document_id):
        return ComplianceDocumentRepository.get_by_id(compliance_document_id)

    @staticmethod
    def create_compliance_document(data):
        return ComplianceDocumentRepository.create(data)

    @staticmethod
    def update_compliance_document(compliance_document_id, data):
        compliance_document = ComplianceDocumentRepository.get_by_id(compliance_document_id)

        if not compliance_document:
            return None

        for key, value in data.items():
            setattr(compliance_document, key, value)

        return ComplianceDocumentRepository.update(compliance_document)

    @staticmethod
    def create_compliance_document(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_compliance_document(compliance_document_id, data):
        compliance_document = ComplianceDocumentRepository.get_by_id(compliance_document_id)

        if not compliance_document:
            return None

        for key, value in data.items():
            setattr(compliance_document, key, value)

        return ComplianceDocumentRepository.update(compliance_document)

    @staticmethod
    def delete_compliance_document(compliance_document_id):
        compliance_document = ComplianceDocumentRepository.get_by_id(compliance_document_id)

        if not compliance_document:
            return None

        db.session.delete(compliance_document)
        db.session.commit()
        return compliance_document



class DrugTestService:

    @staticmethod
    def get_all_drug_tests():
        return DrugTestRepository.get_all()

    @staticmethod
    def get_drug_test(drug_test_id):
        return DrugTestRepository.get_by_id(drug_test_id)

    @staticmethod
    def create_drug_test(data):
        return DrugTestRepository.create(data)

    @staticmethod
    def update_drug_test(drug_test_id, data):
        drug_test = DrugTestRepository.get_by_id(drug_test_id)

        if not drug_test:
            return None

        for key, value in data.items():
            setattr(drug_test, key, value)

        return DrugTestRepository.update(drug_test)

    @staticmethod
    def create_drug_test(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_drug_test(drug_test_id, data):
        drug_test = DrugTestRepository.get_by_id(drug_test_id)

        if not drug_test:
            return None

        for key, value in data.items():
            setattr(drug_test, key, value)

        return DrugTestRepository.update(drug_test)

    @staticmethod
    def delete_drug_test(drug_test_id):
        drug_test = DrugTestRepository.get_by_id(drug_test_id)

        if not drug_test:
            return None

        db.session.delete(drug_test)
        db.session.commit()
        return drug_test
    
    
    
class BackgroundCheckService:

    @staticmethod
    def get_all_background_checks():
        return BackgroundCheckRepository.get_all()

    @staticmethod
    def get_background_check(background_check_id):
        return BackgroundCheckRepository.get_by_id(background_check_id)

    @staticmethod
    def create_background_check(data):
        return BackgroundCheckRepository.create(data)

    @staticmethod
    def update_background_check(background_check_id, data):
        background_check = BackgroundCheckRepository.get_by_id(background_check_id)

        if not background_check:
            return None

        for key, value in data.items():
            setattr(background_check, key, value)

        return BackgroundCheckRepository.update(background_check)

    @staticmethod
    def create_background_check(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_background_check(background_check_id, data):
        background_check = BackgroundCheckRepository.get_by_id(background_check_id)

        if not background_check:
            return None

        for key, value in data.items():
            setattr(background_check, key, value)

        return BackgroundCheckRepository.update(background_check)

    @staticmethod
    def delete_background_check(background_check_id):
        background_check = BackgroundCheckRepository.get_by_id(background_check_id)

        if not background_check:
            return None

        db.session.delete(background_check)
        db.session.commit()
        return background_check
