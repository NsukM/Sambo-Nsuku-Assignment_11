# Assignment 11 – Persistence Repository Layer (Fitness Tracker)

## Deliverables:
- Generic Repository Interface in /repositories/
- Entity-specific Repositories for User and FitnessProfile
- In-Memory Storage Repositories using dictionaries
- Factory Pattern for repository creation abstraction
- Future storage stub (filesystem) added
- Unit tests for CRUD operations using pytest
- Updated documentation and project structure

## Architecture Design:
- Separation of Concerns: Business logic is separated from persistence.
- Scalability: Easily swap storage backends without changing core logic.
- Testability: Lightweight, fast testing with in-memory repositories.

## Future Enhancement:
- Implement real database storage (e.g., PostgreSQL, MongoDB)
- Implement full filesystem JSON storage
