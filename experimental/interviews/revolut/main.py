"""
1. It should be possible to register a service instance, identified by an address
2. Each address should be unique. Not possible to register the same address more than once
3. Get method chooses and return one random instance
4. Get method returns one instance
"""
from typing import Protocol, Sequence
import random
from threading import RLock


class ServiceInstance(Protocol):
    def address(self) -> str: ...


class KubernetesInstance(ServiceInstance):
    def __init__(self, name: str) -> None:
        self._name = name

    def address(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return hash(self.address())

    def __eq__(self, other) -> bool:
        return self.address() == other.address()

class LBSelectingStrategy(Protocol):
    def select_instance(self, instances: Sequence[ServiceInstance]) -> ServiceInstance: ...

class RandomLBSelecting(LBSelectingStrategy):
    def select_instance(self, instances: Sequence[ServiceInstance]) -> ServiceInstance:
        if len(instances) > 0:
            return random.choice(instances)  # bad algorithm -> need to be changed
        raise NoServiceInstanceError()

class RoundRobinSelectingStrategy(LBSelectingStrategy):
    def __init__(self):
        self._curr_pos = 0

    def select_instance(self, instances: Sequence[ServiceInstance]) -> ServiceInstance:
        if len(instances) == 0:
            raise NoServiceInstanceError()
        self._curr_pos = self._curr_pos % len(instances)
        pos = self._curr_pos
        self._curr_pos = (self._curr_pos + 1) % len(instances)
        return instances[pos]

class LoadBalancer:
    def __init__(self, threshold: int, selecting_strategy: LBSelectingStrategy) -> None:
        self._registered_services = set()
        self._ordered_services = []
        self._threshold = threshold
        self._selecting_strategy = selecting_strategy
        self._lock = RLock()

    def register(self, instance: ServiceInstance) -> None:
        with self._lock:
            if instance in self._registered_services:
                raise ServiceAlreadyRegisteredError()
            if len(self._registered_services) >= self._threshold:
                raise LoadBalancerThresholdExceedError()

            self._registered_services.add(instance)
            self._ordered_services.append(instance)

    def get_instance(self) -> ServiceInstance:
        with self._lock:
            return self._selecting_strategy.select_instance(self._ordered_services)

class LoadBalancerThresholdExceedError(Exception):
    pass

class ServiceAlreadyRegisteredError(Exception):
    pass

class NoServiceInstanceError(Exception):
    pass


if __name__ == '__main__':
    lb = LoadBalancer(threshold=10)