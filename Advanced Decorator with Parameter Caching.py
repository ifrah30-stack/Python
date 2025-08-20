from functools import wraps, lru_cache
from typing import Callable, Any, TypeVar, ParamSpec
import time

P = ParamSpec('P')
T = TypeVar('T')

def cached_with_ttl(ttl_seconds: int = 300):
    """Decorator that caches function results with time-to-live."""
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        cache = {}
        
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            # Create a cache key from arguments
            key = (args, frozenset(kwargs.items()))
            
            current_time = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl_seconds:
                    print(f"Cache hit for {func.__name__}")
                    return result
            
            # Cache miss or expired
            print(f"Cache miss for {func.__name__}")
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        
        def clear_cache():
            """Clear the cache manually"""
            cache.clear()
            print(f"Cache cleared for {func.__name__}")
        
        wrapper.clear_cache = clear_cache
        return wrapper
    
    return decorator

@cached_with_ttl(ttl_seconds=2)
def expensive_computation(x: int, y: int = 10) -> int:
    time.sleep(1)  # Simulate expensive operation
    return x * y

# Usage
print(expensive_computation(5))  # Cache miss
print(expensive_computation(5))  # Cache hit (within TTL)
time.sleep(3)
print(expensive_computation(5))  # Cache miss (TTL expired)
expensive_computation.clear_cache()  # Manual cache clear
