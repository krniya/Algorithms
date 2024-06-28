var maximumImportance = function (n, roads) {
    let degree = new Array(n).fill(0);

    // Calculate the degree of each city
    for (const road of roads) {
        degree[road[0]]++;
        degree[road[1]]++;
    }

    // Create a list of cities and sort by degree
    let cities = Array.from({ length: n }, (_, i) => i);
    cities.sort((a, b) => degree[b] - degree[a]);

    // Assign values to cities starting from the highest degree
    let totalImportance = 0;
    for (let i = 0; i < n; i++) {
        totalImportance += (n - i) * degree[cities[i]];
    }

    return totalImportance;
};
