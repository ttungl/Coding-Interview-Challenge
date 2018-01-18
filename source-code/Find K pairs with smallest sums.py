# Find K pairs with smallest sums
def kSmallestPairs(self, nums1, nums2, k):
	# sol:
	queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0) # init
    pairs = [] # output
    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue) # heappop returns smallest item from the heap
        pairs.append([nums1[i], nums2[j]]) # add to the output
        push(i, j+1) # next pair (next column j) in the same row i gets added to the priority queue.
        if j==0: push(i+1, 0) # if first pair is first column in its row, then first pair in the next row is added to the queue.
    return pairs





