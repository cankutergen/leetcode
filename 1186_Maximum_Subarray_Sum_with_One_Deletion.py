class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        answer = arr[0]
        suf_no_del = arr[0]
        suf_del = 0

        for i in range(1, n):
            suf_del = max(suf_del + arr[i], suf_no_del)
            suf_no_del = max(suf_no_del + arr[i], arr[i])
            answer = max(answer, suf_no_del, suf_del)

        return answer
