class FakeRepository:
    def __init__(self):
        self.data = []

    def add(self, entity):
        self.data.append(entity)

    def get_all(self):
        return self.data

class ClientRepository(FakeRepository):
    pass

class OrderRepository(FakeRepository):
    pass

class FurnitureRepository(FakeRepository):
    pass

class RepositoryManager:
    def __init__(self):
        self.client_repo = ClientRepository()
        self.order_repo = OrderRepository()
        self.furniture_repo = FurnitureRepository()

    def get_client_repo(self):
        return self.client_repo

    def get_order_repo(self):
        return self.order_repo

    def get_furniture_repo(self):
        return self.furniture_repo