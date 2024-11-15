#include <iostream>
#include <fstream>
#include <vector>
#include <climits>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int value) : val(value), left(NULL), right(NULL) {}
};

TreeNode* buildTree(const vector<int>& values, const vector<int>& preorder, int& index, int min, int max) {
    if (index >= preorder.size()) return nullptr;
    int val = preorder[index];
    if (val < min || val > max) return nullptr;
    TreeNode* node = new TreeNode(values[val]);
    index++;
    node->left = buildTree(values, preorder, index, min, val - 1);
    node->right = buildTree(values, preorder, index, val + 1, max);
    return node;
}

int findSumMax(TreeNode* root, int& globalMax) {
    if (!root) return 0;
    if (!root->left && !root->right) return root->val;

    int sumLeft = findSumMax(root->left, globalMax);
    int sumRight = findSumMax(root->right, globalMax);

    if (root->left && root->right) {
        globalMax = max(globalMax, sumLeft + sumRight + root->val);
        return max(sumLeft, sumRight) + root->val;
    }

    return (root->left) ? sumLeft + root->val : sumRight + root->val;
}

int main() {
    ifstream inp("path.inp");
    ofstream out("path.out");

    int T;
    inp >> T;
    while (T--) {
        int n;
        inp >> n;
        vector<int> values(n), preorder(n);
        for (int i = 0; i < n; ++i) inp >> values[i];
        for (int i = 0; i < n; ++i) inp >> preorder[i];

        int index = 0;
        TreeNode* root = buildTree(values, preorder, index, 0, n - 1);

        int globalMax = INT_MIN;
        int singleMax = findSumMax(root, globalMax);
        out << globalMax << endl;
    }
    inp.close();
    out.close();
    return 0;
}
