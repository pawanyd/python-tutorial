def nextGreaterElement(nums1, nums2):
    stack = []
    mapping = {}

    # Step 1: Build the map of Next Greater Elements using nums2
    for num in nums2:
        # stack[-1] is the Python way to get the "stack top value" (peek)
        while stack and num > stack[-1]:
            # Set the popped element as key and current num as the greater value
            mapping[stack.pop()] = num
        
        stack.append(num)
    breakpoint()
    # Step 2: Anything left in the stack has no next greater element
    while stack:
        mapping[stack.pop()] = -1

    # Step 3: Map the values from nums1 to the results found in our dictionary
    return [mapping.get(num, -1) for num in nums1]

# Example Test
print(nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
# Output: [7, 7, 7, 7, 7]