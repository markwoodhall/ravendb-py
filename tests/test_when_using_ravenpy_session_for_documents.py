import unittest
import test_base

class test_when_using_ravenpy_session_for_documents(test_base.TestCase):

    def setUp(self):
        self.session = self.get_store().createSession()
        pass

    def tearDown(self):
        pass


    def test_it_is_possible_to_store_and_load_documents(self):

        documentIds = self.session.store([self.session.createDocument('Test', {
            "title": "test document"
        }), self.session.createDocument('Test', {
            "title": "test document 2"
        })])

        self.session.save()

        documents = self.session.load(documentIds)

        self.assertEqual(documents[0]['title'], "test document")
        self.assertEqual(documents[1]['title'], "test document 2")

        self.session.delete(documentIds)
        self.session.save()

    def test_it_is_possible_to_store_and_delete_documents(self):

        documentIds = self.session.store([self.session.createDocument('Test', {
            "title": "test document"
        }), self.session.createDocument('Test', {
            "title": "test document 2"
        })])

        self.session.save()

        self.session.delete(documentIds)
        self.session.save()

        results = self.session.load(documentIds)

        self.assertEqual(len(results), 0)

    def test_it_is_possible_to_update_stored_documents(self):

        doc = [self.session.createDocument('Test', {
            "title": "test document"
        })]

        documentIds = self.session.store(doc)

        results = None

        docId = documentIds[0]

        doc[0]['title'] = "test document update"

        updatedDoc = self.session.createDocument('Test', {
            "title": "test document update"
        })

        self.session.update([{
            "id": docId,
            "doc": updatedDoc
        }])

        self.session.save()

        results = None
        results = self.session.load(documentIds)

        self.assertEqual("test document update", results[0]['title'])
        self.session.delete(documentIds)
        self.session.save()

    def test_it_is_possible_to_update_loaded_documents(self):

        documentIds = self.session.store([self.session.createDocument('Test', {
            "title": "test document"
        })])

        self.session.save()

        results = None
        results = self.session.load(documentIds)

        doc = results[0]
        docId = documentIds[0]

        doc['title'] = "test document update"

        self.session.update([{
            "id": docId,
            "doc": doc
        }])
        self.session.save()

        results = None
        results = self.session.load(documentIds)

        self.assertEqual("test document update", results[0]['title'])
        self.session.delete(documentIds)
        self.session.save()
