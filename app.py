
from source.search import RAGSearch

if __name__ == "__main__":
    rag = RAGSearch()
    query = "What specific biological drop triggers an immediate structural treatment suspension and protocol unblinding evaluation?"
    print(rag.search_and_summarize(query, top_k=3))
     