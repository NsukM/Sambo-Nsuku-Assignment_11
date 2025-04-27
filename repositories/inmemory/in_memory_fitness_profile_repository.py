from typing import Optional, List
from repositories.fitness_profile_repository import FitnessProfileRepository
from src.fitness_profile import FitnessProfile

class InMemoryFitnessProfileRepository(FitnessProfileRepository):
    def _init_(self):
        self._storage = {}

    def save(self, entity: FitnessProfile) -> None:
        self._storage[entity.age] = entity  # Using 'age' as ID for simplicity

    def find_by_id(self, id: str) -> Optional[FitnessProfile]:
        return self._storage.get(id)

    def find_all(self) -> List[FitnessProfile]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
