# Last updated: 6/4/2025, 9:17:37 PM
power = random.randint(150, 200)
mod = random.getrandbits(24)

powers = [1]
for _ in range(5 * 10 ** 4):
    powers.append(powers[-1] * power % mod)

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        def h(s):
            ans = 0
            for c in s:
                ans *= power
                ans %= mod
                ans += ord(c)
                ans %= mod
            return ans
        
        d = [{} for _ in range(max(len(x) for x in words) + 1)]
        for w, c in zip(words, costs):
            if h(w) not in d[len(w)]: d[len(w)][h(w)] = c
            elif c < d[len(w)][h(w)]: d[len(w)][h(w)] = c
        
        hashing = [0]
        for c in target:
            hashing.append((hashing[-1] * power + ord(c)) % mod)
        
        lengths = [i for i in range(len(d)) if len(d[i])]
        n = len(target)
        
        dp = [10 ** 9] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in lengths:
                if i + j > n: break
                else:
                    try:
                        cost = d[j][(hashing[i+j] - hashing[i] * powers[j]) % mod]
                        if dp[i+j] > dp[i] + cost:
                            dp[i+j] = dp[i] + cost
                    except:
                        pass
        return dp[n] if dp[n] < 10 ** 9 else -1