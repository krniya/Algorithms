from collections import deque

def predictPartyVictory(senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()
            if rTurn < dTurn:
                R.append(dTurn + len(senate))
            else:
                D.append(rTurn + len(senate))
        
        return "Radiant" if R else "Dire"