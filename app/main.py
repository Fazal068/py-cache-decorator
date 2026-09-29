def cache(func):
    # Separate cache dictionary created per decorated function
    memo = {}

    def wrapper(*args, **kwargs):
        # Build a unique key combining positional and keyword arguments
        # tuple(sorted(kwargs.items())) ensures keyword arguments are hashable and order-independent
        key = (args, tuple(sorted(kwargs.items())))

        if key in memo:
            print("Getting from cache")
            return memo[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memo[key] = result
            return result

    return wrapper
