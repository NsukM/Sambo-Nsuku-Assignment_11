class FileSystemUserRepository:
    def _init_(self, file_path: str):
        self.file_path = file_path

    def save(self, entity):
        pass  # TODO: Save entity to JSON file

    def find_by_id(self, id: str):
        pass  # TODO: Load entity by ID from file

    def find_all(self):
        pass  # TODO: Load all entities

    def delete(self, id: str):
        pass  # TODO: Delete entity from file
