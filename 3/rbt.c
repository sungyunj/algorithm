#include <stdio.h>
#include <stdlib.h>

typedef enum { RED, BLACK } Color;

typedef struct Node {
    int data;
    Color color;
    struct Node *left, *right, *parent;
} Node;
typedef struct RBT {
    Node *root;
    Node *TNULL; 
} RBT;

void firstTNULL(Node* TNULL) {
    TNULL->data = 0;
    TNULL->color = BLACK;
    TNULL->left = NULL;
    TNULL->right = NULL;
    TNULL->parent = NULL;
}

void firstRBT(RBT* tree) {
    tree->TNULL = (Node *)malloc(sizeof(Node));
    firstTNULL(tree->TNULL);
    tree->root = tree->TNULL;
}

void leftRotate(RBT *tree, Node *x) {
    Node *y = x->right;
    x->right = y->left;
    if (y->left != tree->TNULL)
        y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL)
        tree->root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;
    y->left = x;
    x->parent = y;
}

void rightRotate(RBT *tree, Node *x) {
    Node *y = x->left;
    x->left = y->right;
    if (y->right != tree->TNULL)
        y->right->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL)
        tree->root = y;
    else if (x == x->parent->right)
        x->parent->right = y;
    else
        x->parent->left = y;
    y->right = x;
    x->parent = y;
}

void insertFix(RBT *tree, Node *x) {
    while (x != tree->root && x->parent->color == RED) {
        if (x->parent == x->parent->parent->left) {
            Node *y = x->parent->parent->right;
            if (y->color == RED) {
                x->parent->color = BLACK;
                y->color = BLACK;
                x->parent->parent->color = RED;
                x = x->parent->parent;
            } else {
                if (x == x->parent->right) {
                    x = x->parent;
                    leftRotate(tree, x);
                }
                x->parent->color = BLACK;
                x->parent->parent->color = RED;
                rightRotate(tree, x->parent->parent);
            }
        } else {
            Node *y = x->parent->parent->left;
            if (y->color == RED) {
                x->parent->color = BLACK;
                y->color = BLACK;
                x->parent->parent->color = RED;
                x = x->parent->parent;
            } else {
                if (x == x->parent->left) {
                    x = x->parent;
                    rightRotate(tree, x);
                }
                x->parent->color = BLACK;
                x->parent->parent->color = RED;
                leftRotate(tree, x->parent->parent);
            }
        }
    }
    tree->root->color = BLACK;
}

void insert(RBT *tree, int key) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = key;
    newNode->left = tree->TNULL;
    newNode->right = tree->TNULL;
    newNode->color = RED; 

    Node *parent = NULL;
    Node *current = tree->root;
    while (current != tree->TNULL) {
        parent = current;
        if (newNode->data < current->data)
            current = current->left;
        else
            current = current->right;
    }
    newNode->parent = parent;
    if (parent == NULL) 
        tree->root = newNode;
    else if (newNode->data < parent->data)
        parent->left = newNode;
    else
        parent->right = newNode;
    insertFix(tree, newNode);
}

void transMove(RBT *tree, Node *p, Node *n) {
    if (p->parent == NULL)
        tree->root = n;
    else if (p == p->parent->left)
        p->parent->left = n;
    else
        p->parent->right = n;
    n->parent = p->parent;
}

void deleteNodeFix(RBT *tree, Node *x) {
    while (x != tree->root && x->color == BLACK) {
        if (x == x->parent->left) {
            Node *w = x->parent->right;
            if (w->color == RED) {
                w->color = BLACK;
                x->parent->color = RED;
                leftRotate(tree, x->parent);
                w = x->parent->right;
            }
            if (w->left->color == BLACK && w->right->color == BLACK) {
                w->color = RED;
                x = x->parent;
            } else {
                if (w->right->color == BLACK) {
                    w->left->color = BLACK;
                    w->color = RED;
                    rightRotate(tree, w);
                    w = x->parent->right;
                }
                w->color = x->parent->color;
                x->parent->color = BLACK;
                w->right->color = BLACK;
                leftRotate(tree, x->parent);
                x = tree->root;
            }
        } else {
            Node *c = x->parent->left;
            if (c->color == RED) {
                c->color = BLACK;
                x->parent->color = RED;
                rightRotate(tree, x->parent);
                c = x->parent->left;
            }
            if (c->right->color == BLACK && c->left->color == BLACK) {
                c->color = RED;
                x = x->parent;
            } else {
                if (c->left->color == BLACK) {
                    c->right->color = BLACK;
                    c->color = RED;
                    leftRotate(tree, c);
                    c = x->parent->left;
                }
                c->color = x->parent->color;
                x->parent->color = BLACK;
                c->left->color = BLACK;
                rightRotate(tree, x->parent);
                x = tree->root;
            }
        }
    }
    x->color = BLACK;
}

void deleteNode(RBT *tree, int key) {
    Node *z = tree->root;
    Node *x, *y;
    while (z != tree->TNULL) {
        if (z->data == key)
            break;
        else if (z->data < key)
            z = z->right;
        else
            z = z->left;
    }
    if (z == tree->TNULL) {
        printf("not found\n");
        return;
    }
    y = z;
    Color yColor = y->color;
    if (z->left == tree->TNULL) {
        x = z->right;
        transMove(tree, z, z->right);
    } else if (z->right == tree->TNULL) {
        x = z->left;
        transMove(tree, z, z->left);
    } else {
        y = z->right;
        while (y->left != tree->TNULL)
            y = y->left;
        yColor = y->color;
        x = y->right;
        if (y->parent == z)
            x->parent = y;
        else {
            transMove(tree, y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        transMove(tree, z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    free(z);
    if (yColor == BLACK)
        deleteNodeFix(tree, x);
}

Color colorFix(RBT *tree, int key) {
    Node *current = tree->root;
    while (current != tree->TNULL) {
        if (key == current->data)
            return current->color;
        else if (key < current->data)
            current = current->left;
        else
            current = current->right;
    }
    printf(" %d not found\n", key);
    return BLACK; 
}

int main() {
    FILE *inp = fopen("rbt.inp", "r");
    FILE *out = fopen("rbt.out", "w");
    if (!inp || !out) {
        perror("open error");
        return EXIT_FAILURE;
    }
    RBT tree;
    firstRBT(&tree);
    char operation;
    int key;
    while (fscanf(inp, "%c %d\n", &operation, &key) != EOF) {
        switch (operation) {
            case 'i':
                insert(&tree, key);
                break;
            case 'd':
                deleteNode(&tree, key);
                break;
            case 'c': {
                Color color = colorFix(&tree, key);
                fprintf(out, "color(%d): %s\n", key, color == RED ? "RED" : "BLACK");
                break;
            }
        }
    }
    fclose(inp);
    fclose(out);

    return 0;
}
