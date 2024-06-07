class TrieNode {
    constructor() {
        this.children = {};
        this.isEnd = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEnd = true;
    }

    search(word) {
        let node = this.root;
        let prefix = "";
        for (const char of word) {
            if (!node.children[char]) {
                return word;
            }
            prefix += char;
            if (node.children[char].isEnd) {
                return prefix;
            }
            node = node.children[char];
        }
        return word;
    }
}

var replaceWords = function (dictionary, sentence) {
    const trie = new Trie();
    for (const word of dictionary) {
        trie.insert(word);
    }

    const words = sentence.split(" ");
    const result = words.map((word) => trie.search(word));

    return result.join(" ");
};
