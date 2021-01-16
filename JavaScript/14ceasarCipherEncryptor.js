function ceasarCipherEncryptor(str, key) {
    let newletter = [];
    let newKey = key % 26;
    for(const letter of str) {
        newletter.push(encryptor(letter, newKey));
    }
    return newletter.join("");
}

function encryptor(letter, key) {
    let newletter = letter.charCodeAt() + key;
    return newletter <= 122 ? String.fromCharCode(newletter) : String.fromCharCode(newletter % 122);
}

