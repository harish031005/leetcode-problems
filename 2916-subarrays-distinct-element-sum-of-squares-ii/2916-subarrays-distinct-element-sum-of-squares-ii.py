class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        class SegTree:
            def __init__(self, n):
                self.n = n
                self.sum = [0] * (4 * n)
                self.sqsum = [0] * (4 * n)
                self.lazy = [0] * (4 * n)
            def push(self, node, l, r):
                if self.lazy[node] != 0:
                    add = self.lazy[node]
                    length = r - l + 1
                    self.sqsum[node] = (self.sqsum[node] + 2 * add * self.sum[node] + add * add * length) % MOD
                    self.sum[node] = (self.sum[node] + add * length) % MOD
                    if l != r:
                        self.lazy[node*2] = (self.lazy[node*2] + add) % MOD
                        self.lazy[node*2+1] = (self.lazy[node*2+1] + add) % MOD
                    self.lazy[node] = 0
            def update(self, node, l, r, ql, qr, val):
                self.push(node, l, r)
                if qr < l or r < ql:
                    return
                if ql <= l and r <= qr:
                    self.lazy[node] = (self.lazy[node] + val) % MOD
                    self.push(node, l, r)
                    return
                mid = (l + r) // 2
                self.update(node*2, l, mid, ql, qr, val)
                self.update(node*2+1, mid+1, r, ql, qr, val)
                self.sum[node] = (self.sum[node*2] + self.sum[node*2+1]) % MOD
                self.sqsum[node] = (self.sqsum[node*2] + self.sqsum[node*2+1]) % MOD
            def range_add(self, l, r, val=1):
                if l <= r:
                    self.update(1, 0, self.n-1, l, r, val)
            def get_sqsum(self):
                self.push(1, 0, self.n-1)
                return self.sqsum[1]
        tree = SegTree(n)
        last = {}
        ans = 0
        for r in range(n):
            x = nums[r]
            left = last.get(x, -1) + 1
            tree.range_add(left, r, 1)
            last[x] = r
            ans = (ans + tree.get_sqsum()) % MOD
        return ans