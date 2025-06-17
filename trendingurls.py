import heapq
from collections import Counter

def get_top_k_urls(url_list, k):
    # Step 1: Count frequency of each URL
    url_counts = Counter(url_list)

    # Step 2: Use negative counts to simulate max-heap
    heap = [(-count, url) for url, count in url_counts.items()]

    # Step 3: Heapify the list
    heapq.heapify(heap)

    # Step 4: Extract top k
    top_k = [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]

    return top_k
