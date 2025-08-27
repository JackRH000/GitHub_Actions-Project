import sys 

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half
            
    return -1  # Target not found


if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python binary_search.py <num1> <num2> ... --target <number>")
        sys.exit(1)

    # Parse target
    if "--target" not in sys.argv:
        print("Please specify the target number using --target")
        sys.exit(1)

    target_index = sys.argv.index("--target")
    arr = list(map(int, sys.argv[1:target_index]))
    target = int(sys.argv[target_index + 1])

    result = binary_search(arr, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in list")