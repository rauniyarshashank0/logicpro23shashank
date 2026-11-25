#section D DSA:-

# question 16:-

# def constant_difference(arr):
#     if len(arr) < 2:
#         return True

#     diff = arr[1] - arr[0]

#     for i in range(1, len(arr) - 1):
#         if arr[i + 1] - arr[i] != diff:
#             return False

#     return True


# numbers = [2, 4, 6, 8, 10, 12]

# print(constant_difference(numbers))

# question 20:-

# def max_sum(arr, k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i-k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


# arr = [3, 1, 4, 2, 5, 1, 6]
# k = 3

# print("Maximum Sum:", max_sum(arr, k))

# time complexity is O(n)


#question 19 :-

# def frequency_count(arr):
#     freq = {}

#     for num in arr:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1

#     most_frequent = max(freq, key=freq.get)

#     print("Frequency Count:", freq)
#     print("Most Frequent Number:", most_frequent)
#     print("Frequency:", freq[most_frequent])


# arr = [4, 2, 4, 3, 2, 4, 1]

# frequency_count(arr)

# question 17:-

# def max_sum(arr, k):
#     window_sum = sum(arr[:k])
#     maximum = window_sum

#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i-k]
#         maximum = max(maximum, window_sum)

#     return maximum


# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# print("Maximum Sum:", max_sum(arr, k))