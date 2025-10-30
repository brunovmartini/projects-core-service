def is_invalid_request(obj):
    return any(value is None for value in vars(obj).values())
