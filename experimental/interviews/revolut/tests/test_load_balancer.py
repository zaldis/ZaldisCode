import random

from main import (
    LoadBalancer, KubernetesInstance, LoadBalancerThresholdExceedError, ServiceAlreadyRegisteredError,
    RandomLBSelecting, RoundRobinSelectingStrategy
)
import pytest


def test_exceed_threshold_raise_exception():
    lb = LoadBalancer(2, RandomLBSelecting())
    service_a = KubernetesInstance(name="sa")
    service_b = KubernetesInstance(name="sb")
    service_c = KubernetesInstance(name="sc")

    lb.register(service_a)
    lb.register(service_b)
    with pytest.raises(LoadBalancerThresholdExceedError):
        lb.register(service_c)

def test_registering_same_service_raise_exception():
    lb = LoadBalancer(3, RandomLBSelecting())
    service_a = KubernetesInstance(name="sa")

    lb.register(service_a)
    with pytest.raises(ServiceAlreadyRegisteredError):
        lb.register(service_a)

def test_random_selecting():
    lb = LoadBalancer(3, RandomLBSelecting())
    service_a = KubernetesInstance(name="sa")
    service_b = KubernetesInstance(name="sb")
    service_c = KubernetesInstance(name="sc")
    lb.register(service_a)
    lb.register(service_b)
    lb.register(service_c)

    random.seed(10)
    assert lb.get_instance() == service_c
    assert lb.get_instance() == service_a
    assert lb.get_instance() == service_b
    assert lb.get_instance() == service_b

def test_random_selecting_agnostic():
    lb = LoadBalancer(3, RandomLBSelecting())
    service_a = KubernetesInstance(name="sa")
    service_b = KubernetesInstance(name="sb")
    service_c = KubernetesInstance(name="sc")
    lb.register(service_a)
    lb.register(service_b)
    lb.register(service_c)

    service_calls = {
        service_a: 0,
        service_b: 0,
        service_c: 0
    }
    requests_count = 9000
    while requests_count > 0:
        service = lb.get_instance()
        service_calls[service] += 1
        requests_count -= 1

    expected_shift = 0.02
    assert abs(1 - service_calls[service_a]/3000) < expected_shift
    assert abs(1 - service_calls[service_b]/3000) < expected_shift
    assert abs(1 - service_calls[service_c]/3000) < expected_shift

def test_round_robin_selecting():
    lb = LoadBalancer(3, RoundRobinSelectingStrategy())
    service_a = KubernetesInstance(name="sa")
    service_b = KubernetesInstance(name="sb")
    service_c = KubernetesInstance(name="sc")
    lb.register(service_a)
    lb.register(service_b)
    lb.register(service_c)

    assert lb.get_instance() == service_a
    assert lb.get_instance() == service_b
    assert lb.get_instance() == service_c
    assert lb.get_instance() == service_a