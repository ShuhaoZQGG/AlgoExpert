class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        dic = defaultdict(int)
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                cows += int(dic[secret[i]] < 0) + int(dic[guess[i]] > 0)
                dic[secret[i]] += 1
                dic[guess[i]] -= 1

        return f'{bulls}A{cows}B'