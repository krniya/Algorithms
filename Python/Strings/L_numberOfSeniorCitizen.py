def countSeniors(details: List[str]) -> int:
        count = 0
        for data in details:
            if int(data[-4:-2]) > 60:
                count += 1
        return count