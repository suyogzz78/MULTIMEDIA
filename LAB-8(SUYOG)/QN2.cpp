#include <iostream>
#include <cstdlib>  // For malloc and free
using namespace std;

#define MAX_TREE_HT 50

// Huffman Tree Node
struct MinHNode {
    unsigned freq;
    char item;
    struct MinHNode *left, *right;
};

// Min Heap Structure
struct MinH {
    unsigned size;
    unsigned capacity;
    struct MinHNode **array;
};

// Creating Huffman tree node
struct MinHNode *newNode(char item, unsigned freq) {
    struct MinHNode *temp = (struct MinHNode *)malloc(sizeof(struct MinHNode));
    temp->left = temp->right = NULL;
    temp->item = item;
    temp->freq = freq;
    return temp;
}

// Create min heap using given capacity
struct MinH *createMinH(unsigned capacity) {
    struct MinH *minHeap = (struct MinH *)malloc(sizeof(struct MinH));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array = (struct MinHNode **)malloc(minHeap->capacity * sizeof(struct MinHNode *));
    return minHeap;
}

// Print the Huffman Code Array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; ++i)
        cout << arr[i];
    cout << "\n";
}

// Swap function
void swapMinHNode(struct MinHNode **a, struct MinHNode **b) {
    struct MinHNode *t = *a;
    *a = *b;
    *b = t;
}

// Heapify function for min heap
void minHeapify(struct MinH *minHeap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < minHeap->size && minHeap->array[left]->freq < minHeap->array[smallest]->freq)
        smallest = left;
    if (right < minHeap->size && minHeap->array[right]->freq < minHeap->array[smallest]->freq)
        smallest = right;
    if (smallest != idx) {
        swapMinHNode(&minHeap->array[smallest], &minHeap->array[idx]);
        minHeapify(minHeap, smallest);
    }
}

// Check if heap size is 1
int checkSizeOne(struct MinH *minHeap) {
    return (minHeap->size == 1);
}

// Extract minimum node
struct MinHNode *extractMin(struct MinH *minHeap) {
    struct MinHNode *temp = minHeap->array[0];
    minHeap->array[0] = minHeap->array[minHeap->size - 1];
    --minHeap->size;
    minHeapify(minHeap, 0);
    return temp;
}

// Insert node into min heap
void insertMinHeap(struct MinH *minHeap, struct MinHNode *minHeapNode) {
    ++minHeap->size;
    int i = minHeap->size - 1;

    while (i && minHeapNode->freq < minHeap->array[(i - 1) / 2]->freq) {
        minHeap->array[i] = minHeap->array[(i - 1) / 2];
        i = (i - 1) / 2;
    }
    minHeap->array[i] = minHeapNode;
}

// Build min heap
void buildMinHeap(struct MinH *minHeap) {
    int n = minHeap->size - 1;
    for (int i = (n - 1) / 2; i >= 0; --i)
        minHeapify(minHeap, i);
}

// Check if a node is a leaf
int isLeaf(struct MinHNode *root) {
    return !(root->left) && !(root->right);
}

// Create and build min heap
struct MinH *createAndBuildMinHeap(char item[], int freq[], int size) {
    struct MinH *minHeap = createMinH(size);
    for (int i = 0; i < size; ++i)
        minHeap->array[i] = newNode(item[i], freq[i]);
    minHeap->size = size;
    buildMinHeap(minHeap);
    return minHeap;
}

// Build Huffman Tree
struct MinHNode *buildHfTree(char item[], int freq[], int size) {
    struct MinHNode *left, *right, *top;
    struct MinH *minHeap = createAndBuildMinHeap(item, freq, size);

    while (!checkSizeOne(minHeap)) {
        left = extractMin(minHeap);
        right = extractMin(minHeap);
        top = newNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;
        insertMinHeap(minHeap, top);
    }
    return extractMin(minHeap);
}

// Print Huffman Codes
void printHCodes(struct MinHNode *root, int arr[], int top) {
    if (root->left) {
        arr[top] = 0;
        printHCodes(root->left, arr, top + 1);
    }
    if (root->right) {
        arr[top] = 1;
        printHCodes(root->right, arr, top + 1);
    }
    if (isLeaf(root)) {
        cout << root->item << " | ";
        printArray(arr, top);
    }
}

// Huffman Coding Wrapper Function
void HuffmanCodes(char item[], int freq[], int size) {
    struct MinHNode *root = buildHfTree(item, freq, size);
    int arr[MAX_TREE_HT], top = 0;
    printHCodes(root, arr, top);
}

// Main Function
int main() {
    char arr[] = {'A', 'B', 'C', 'D'};
    int freq[] = {8, 2, 5, 2 };
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "Char | Huffman code\n";
    cout << "----------------------\n";
    HuffmanCodes(arr, freq, size);
    return 0;
}
