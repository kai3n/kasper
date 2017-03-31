---
layout: post
title: 7 Lines Quick Sort in Python
date: 2017-03-31
categories: Algorithm
published: true
---

What a elegant quick sort in Python!

```python
def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

It's good for you to memorize this elegant code snippet for the future interview.