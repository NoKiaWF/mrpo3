from classes import RestorationOrder, Workshop, Material, Furniture, Category, Client
from repositories import RepositoryManager

def main():
    # Create repository manager
    repo_manager = RepositoryManager()

    # Add some clients
    repo_manager.get_client_repo().add(Client('Client Registration Data 1'))
    repo_manager.get_client_repo().add(Client('Client Registration Data 2'))

    # Add some orders
    repo_manager.get_order_repo().add(RestorationOrder(5000, '2024-06-03'))
    repo_manager.get_order_repo().add(RestorationOrder(3000, '2024-06-04'))

    # Add some furniture with materials
    repo_manager.get_furniture_repo().add(Furniture('Good', Material('Wood with Leather')))
    repo_manager.get_furniture_repo().add(Furniture('Fair', Material('Iron')))
    repo_manager.get_furniture_repo().add(Furniture('Excellent', Material('Wood with Fabric')))

    # Retrieve all clients, orders, and furniture
    clients = repo_manager.get_client_repo().get_all()
    orders = repo_manager.get_order_repo().get_all()
    furniture = repo_manager.get_furniture_repo().get_all()

    # Output for verification
    for client in clients:
        print(f"Client: {client.registration_data}")

    for order in orders:
        print(f"Order: {order.cost}, {order.order_date}")

    for item in furniture:
        print(f"Furniture: {item.condition}, {item.material.material_type}")

if __name__ == "__main__":
    main()