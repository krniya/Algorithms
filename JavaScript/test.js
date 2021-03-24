const arr = [
    { "name": "Mary", "marks": [72, 65, 55, 71] },
    { "name": "Anita", "marks": [66, 70, 75, 53] },
    { "name": "Edward", "marks": [44, 54, 64, 58] },
    { "name": "Thomas", "marks": [62, 55, 65, 81] },
    { "name": "Robin", "marks": [41, 44, 47, 49] },
    { "name": "Sophia", "marks": [71, 73, 67, 77] },
    { "name": "Bruce", "marks": [52, 57, 61, 64] },
];

let total = (arr) => {
    let total = (tot, curr) => {
        return tot + curr
    }
    const totaljson = arr.map(stud => {
        return { "name": stud["name"], "totalMarks": stud["marks"].reduce(total, 0) }
    })
    return totaljson
}

let studentMax = (arr) => {
    let maxm = (maxmark, curr) => {
        if (curr > maxmark) {
            maxmark = curr
        }
        return maxmark
    }
    const stud = arr.map(std => {
        return { "name": std["name"], "maxMark": std["marks"].reduce(maxm, 0) }
    })
    return stud
}

let maxMarks = (arr) => {
    let total = (tot, curr) => {
        return tot + curr
    }
    let maxmark = (maxma, std) => {
        let t = std["marks"].reduce(total, 0)
        if (t > maxma["total"]) {
            maxma["name"] = std["name"]
            maxma["total"] = t
        }
        return maxma
    }
    const maxm = arr.reduce(maxmark, { "name": "", "total": 0 })
    return maxm
}

let sortByMarks = (arr) => {
    arr.sort(function (a, b) {
        let atot = a["marks"].reduce((tot, num) => {
            return tot + num
        }, 0)
        let btot = b["marks"].reduce((tot, num) => {
            return tot + num
        }, 0)
        if (atot < btot) {
            return -1
        }
        if (atot > btot) {
            return 1
        }
        return 0
    })
    return arr
}

let scoreAtLeast = (arr) => {
    let score = (max, curr) => {
        if (curr > max) {
            max = curr
        }
        return max
    }
    return arr.filter(student => {
        student["marks"].reduce(score, 0) > 70
    })
}

// console.log(sortByMarks(arr))
// console.log(scoreAtLeast(arr))
// console.log(maxMarks(arr))
// console.log(total(arr))
console.log(studentMax(arr))