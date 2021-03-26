let txt1 = "i enjoy coding and writing code is a lot of fun"
let splittxt = txt1.split(" ")
console.log(splittxt)

let capString = splittxt.map(word => {
    return word.toUpperCase()
})
console.log(capString)

let containsAE = splittxt.filter(word => {
    if (word.includes("a") || word.includes("e")) {
        return true
    }
})

console.log(containsAE)

let countAE = (tot, word) => {
    if (word.includes("a") || word.includes("e")) {
        return tot += 1
    }
    return tot
}

console.log(splittxt.reduce(countAE, 0))

let productMaster = [
    { id: 'A441', name: 'Pepsi', category: 'Soft Drink', price: 15, quantity: 2 },
    { id: 'B234', name: 'Coke', category: 'Soft	Drink', price: 10, quantity: 8 },
    { id: 'A617', name: 'Mirinda', category: 'Soft Drink', price: 20, quantity: 20 },
    { id: 'B003', name: 'Sprite', category: 'Soft Drink', price: 16, quantity: 5 },
    { id: 'B225', name: 'Minute	Maid', category: 'Soft Drink', price: 25, quantity: 12 },
    { id: 'A742', name: '5Star', category: 'Chocloate', price: 10, quantity: 3 },
    { id: 'B388', name: 'Appy', category: 'Soft Drink', price: 35, quantity: 9 },
    { id: 'A899', name: 'Gems', category: 'Chocloate', price: 12, quantity: 11 },
    { id: 'B635', name: 'KitKat', category: 'Chocloate', price: 15, quantity: 7 },
    { id: 'B408', name: 'Perk', category: 'Chocloate', price: 8, quantity: 15 },
    { id: 'A354', name: 'Dairy Milk', category: 'Chocloate', price: 30, quantity: 4 }]


let includesMilk = (prods) => {
    return prods.filter((prod => {
        return prod["name"].toUpperCase().includes("MILK")
    }))
}

console.log(includesMilk(productMaster))

let softDrinks = (prods) => {
    let sd = prods.filter((products) => {
        return products["category"] === "Soft Drink"
    })
    return sd
}

console.log(softDrinks(productMaster))

productMaster.sort((a, b) => {
    if (a["price"] < b["price"]) {
        return 1
    }
    else if (a["price"] > b["price"]) {
        return -1
    }
    return 0
})

console.log(productMaster)

let saleMaster = [
    { id: 'A441', sales: [10, 12, 13, 10, 16, 22, 30] },
    { id: 'B234', sales: [2, 4, 3, 4, 2, 6, 8, 10] },
    { id: 'A617', sales: [5, 5, 5, 5, 5] },
    { id: 'C229', sales: [9, 7, 6, 8, 8, 10, 9, 3, 4, 5, 6] },
    { id: 'D412', sales: [25, 25, 23, 21] },
    { id: 'A054', sales: [2, 2, 3, 1, 5, 6, 7, 11, 2] },
    { id: 'B955', sales: [1, 1, 1, 1, 1, 1] },
    { id: 'M341', sales: [4, 5, 4, 5, 4] },
    { id: 'H103', sales: [3, 2, 2, 3, 1, 1] },
    { id: 'B199', sales: [6, 5, 4] },
    { id: 'D388', sales: [7, 8, 9, 8, 4, 4, 4, 3, 2, 1] }]

let newSales = (sales, newsale) => {
    for (let i = 0; i < sales.length; i++) {
        if (sales[i]["id"] === newsale["id"]) {
            sales[i]["sales"].push(newsale["quantity"])
            return sales
        }
    }
}

console.log(newSales(saleMaster, { "id": "B955", "quantity": 99 }))

let maxDay = (sales) => {
    let max = (m, curr) => {
        if (curr > m) {
            m = curr
        }
        return m
    }
    let arr = sales.map((sale) => {
        return { "id": sale["id"], "total": sale["sales"].reduce(max, 0) }
    })
    return arr
}

console.log(maxDay(saleMaster))

let totalsale = (sales) => {
    let sum = (tot, curr) => {
        return tot + curr
    }
    let tot = sales.map((sale) => {
        return sale["sales"].reduce(sum, 0)
    }).reduce(sum, 0)
    return tot
}

console.log(totalsale(saleMaster))

let idsales = (sales) => {
    let sum = (tot, curr) => {
        return tot + curr
    }
    let arr = sales.map((sale) => {
        return { "id": sale["id"], "total": sale["sales"].reduce(sum, 0) }
    })
    return arr
}

console.log(idsales(saleMaster))