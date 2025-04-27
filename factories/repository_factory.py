from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from repositories.inmemory.in_memory_fitness_profile_repository import InMemoryFitnessProfileRepository

class RepositoryFactory:
    @staticmethod
    def get_user_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryUserRepository()
        else:
            raise ValueError("Unsupported storage type for User")

    @staticmethod
    def get_fitness_profile_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryFitnessProfileRepository()
        else:
            raise ValueError("Unsupported storage type for FitnessProfile")
