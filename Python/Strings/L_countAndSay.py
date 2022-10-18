def countAndSay(n: int) -> str:
        ans = "1"
        for i in range(1, n):
            prev, st, carry = ans[0], "", 1
            for j in range(1, len(ans)):
                if prev == ans[j]:
                    carry += 1
                else:
                    st += f"{carry}{prev}"
                    prev = ans[j]
                    carry = 1
            st += f"{carry}{prev}"
            ans = st
        return ans