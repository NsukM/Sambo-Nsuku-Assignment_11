from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from src.user import User

def test_user_repository_crud():
    repo = InMemoryUserRepository()

    user = User("1", "Test User", "test@example.com", "password", "Lose Weight")
    repo.save(user)

    assert repo.find_by_id("1").name == "Test User"
    assert len(repo.find_all()) == 1

    repo.delete("1")
    assert repo.find_by_id("1") is None

