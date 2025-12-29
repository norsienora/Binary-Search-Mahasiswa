def binary_search_iterative(data, target_nim):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid]["nim"] == target_nim:
            return data[mid]
        elif data[mid]["nim"] < target_nim:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_recursive(data, target_nim, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if data[mid]["nim"] == target_nim:
        return data[mid]
    elif data[mid]["nim"] < target_nim:
        return binary_search_recursive(data, target_nim, mid + 1, high)
    else:
        return binary_search_recursive(data, target_nim, low, mid - 1)
