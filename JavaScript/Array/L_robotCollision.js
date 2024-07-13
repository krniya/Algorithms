var survivedRobotsHealths = function (positions, healths, directions) {
    let n = positions.length;
    let robots = [];

    for (let i = 0; i < n; ++i) {
        robots.push([positions[i], healths[i], directions[i], i]);
    }

    robots.sort((a, b) => a[0] - b[0]);

    let stack = [];

    for (let robot of robots) {
        if (robot[2] === "R" || stack.length === 0 || stack[stack.length - 1][2] === "L") {
            stack.push(robot);
            continue;
        }

        if (robot[2] === "L") {
            let add = true;
            while (stack.length > 0 && stack[stack.length - 1][2] === "R" && add) {
                let last_health = stack[stack.length - 1][1];
                if (robot[1] > last_health) {
                    stack.pop();
                    robot[1] -= 1;
                } else if (robot[1] < last_health) {
                    stack[stack.length - 1][1] -= 1;
                    add = false;
                } else {
                    stack.pop();
                    add = false;
                }
            }

            if (add) {
                stack.push(robot);
            }
        }
    }

    stack.sort((a, b) => a[3] - b[3]);

    let result = [];
    for (let robot of stack) {
        result.push(robot[1]);
    }

    return result;
};
