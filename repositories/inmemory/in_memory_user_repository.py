from typing import Optional, List
from repositories.user_repository import UserRepository
from src.user import User

class InMemoryUserRepository(UserRepository):
    def _init_(self):
        self._storage = {}

    def save(self, entity: User) -> None:
        self._storage[entity.user_id] = entity

    def find_by_id(self, id: str) -> Optional[User]:
        return self._storage.get(id)

    def find_all(self) -> List[User]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
