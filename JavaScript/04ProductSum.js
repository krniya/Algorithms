// O(n) | O(d)
function productSum(array, multi = 1) {
    let sum = 0;
    for(const ele in array) {
        if(Array.isArray(ele)) {
            sum += productSum(ele);
        }
        else {
            sum += ele;
        }
    }
    return sum * multi;
}