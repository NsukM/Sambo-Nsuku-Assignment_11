from repositories.inmemory.in_memory_fitness_profile_repository import InMemoryFitnessProfileRepository
from src.fitness_profile import FitnessProfile

def test_fitness_profile_repository_crud():
    repo = InMemoryFitnessProfileRepository()

    profile = FitnessProfile(age=25, weight=70, height=175, activity_level="Moderate")
    repo.save(profile)

    assert repo.find_by_id(25).weight == 70
    assert len(repo.find_all()) == 1

    repo.delete(25)
    assert repo.find_by_id(25) is None

