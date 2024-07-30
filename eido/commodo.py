def unwrap_function(nested_list):
    """Recursively flattens a nested list."""
    unwrapped = []
    for element in nested_list:
        if isinstance(element, list):
            unwrapped.extend(unwrap_function(element))
        else:
            unwrapped.append(element)
    return unwrapped

# Example usage:
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(unwrap_function(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7]
