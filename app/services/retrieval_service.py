from app.retriever.search import Retriever


class RetrievalService:

    def __init__(self):
        self.retriever = Retriever()

    def retrieve(self, query: str):
        return self.retriever.search(query)