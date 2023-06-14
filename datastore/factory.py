from datastore.datastore import DataStore
import os


async def get_datastore() -> DataStore:
    datastore = os.environ.get("DATASTORE")
    assert datastore is not None

    match datastore:
        case "llama":
            from datastore.providers.llama_datastore import LlamaDataStore
            return LlamaDataStore()
        case "pinecone":
            from datastore.providers.pinecone_datastore import PineconeDataStore
            return PineconeDataStore()
        case _:
            raise ValueError(
                f"Unsupported vector database: {datastore}. "
                f"Try one of the following: llama, pinecone, weaviate, milvus, zilliz, redis, or qdrant"
            )