# Hexagonal Architecture (Ports and Adapters) Rules with Python Code Examples

Hexagonal Architecture, also known as Ports and Adapters, is an architectural pattern used to create fully decoupled codebases. It allows us to separate the core business logic from the infrastructure and keeps our systems clean and maintainable.

Here are the rules and some examples in Python to help illustrate them:

## Rules of Hexagonal Architecture

1. **Separation of Concerns**: Separate the core business logic from the details of the outside world like databases, web services, and user interfaces.
2. **Adapters**: Implement different adapters (e.g., repository, service, UI) that communicate with the core business logic.
3. **Ports**: Define ports as interfaces inside your core application that describe what the application can do.
4. **Dependency Inversion**: The core application should not depend on the details but on abstractions (interfaces).
5. **Interaction via Ports**: The core logic interacts with the outside world through defined ports.
6. **Testability**: The decoupled nature allows for easier unit and integration testing.
7. **Configurable via Dependency Injection**: Adapters can be plugged into ports at runtime through dependency injection.

## Components of Hexagonal Architecture

- **Core Domain**: The central part containing the business logic.
- **Ports**: Interfaces that define how the core domain can be interacted with.
- **Adapters**: Implementations of these interfaces for different technologies (databases, web services, etc.).

### Example in Python

#### Core Domain

```python
# services.py
class OrderService:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def create_order(self, order_data):
        # Business logic to create an order
        order = Order(order_data)
        self.order_repository.save(order)
        return order
    
    def get_order(self, order_id):
        return self.order_repository.get(order_id)

# models.py
class Order:
    def __init__(self, data):
        # Initialize order instance with data
        self.data = data
```

#### Ports

```python
# ports.py
from abc import ABC, abstractmethod

class OrderRepositoryPort(ABC):
    @abstractmethod
    def save(self, order):
        pass
    
    @abstractmethod
    def get(self, order_id):
        pass
```

#### Adapters

```python
# repository_adapter.py
from ports import OrderRepositoryPort
from models import Order

class InMemoryOrderRepository(OrderRepositoryPort):
    def __init__(self):
        # Initialize in-memory storage
        self.orders = {}
    
    def save(self, order):
        self.orders[order.data['id']] = order
    
    def get(self, order_id):
        return self.orders.get(order_id)
```

#### Dependency Injection

```python
# main.py
from services import OrderService
from repository_adapter.py import InMemoryOrderRepository

# Setup dependency
order_repository = InMemoryOrderRepository()
order_service = OrderService(order_repository)

# Usage
order_data = {'id': 1, 'item': 'book', 'quantity': 1}
order = order_service.create_order(order_data)
retrieved_order = order_service.get_order(1)
print(retrieved_order.data)
```

### Benefits of Hexagonal Architecture

1. **Decoupling**: The core logic is decoupled from the infrastructure, improving maintainability.
2. **Testability**: Easier unit and integration testing.
3. **Flexibility**: Different adapters can be easily swapped due to dependency inversion.
4. **Resiliency**: Changes in the external systems have minimal impact on the core logic.

By following these rules and principles, you can build a robust and maintainable software system adhering to Hexagonal Architecture.
