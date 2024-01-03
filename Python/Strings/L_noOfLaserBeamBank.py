from typing import List


def numberOfBeams(bank: List[str]) -> int:
    laser_count = []
    empty_floor = "0" * len(bank[0])
    for i, laser in enumerate(bank):
        if laser == empty_floor:
            continue
        laser_count.append(laser.count("1"))
    total_laser = 0
    for i in range(len(laser_count)-1):
        total_laser += (laser_count[i] * laser_count[i+1])
    return total_laser

print(numberOfBeams(["011001","000000","010100","001000"]))