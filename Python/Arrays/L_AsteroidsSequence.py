def asteroidsDestroyed(mass, asteroids):
    asteroids.sort()
    for ast in asteroids:
        if mass >= ast:
            mass += ast
        else:
            return False
    return True