def numRescueBoats(people, limit):
    people.sort()
    l,boat,r = 0, 0, len(people) - 1
    while l<=r:
        if people[l] + people[r] <= limit:
            l+=1
            r-=1
        else:
            r-=1
        boat+=1
    return boat