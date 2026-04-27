#include "dfs.h"
#define NINF 0x80000000
#define INF  0x7fffffff

void DFS::init(const graph::AList& al) {
    this->al = &al;
    c = new Color[al.n_vertex];
    d = new int[al.n_vertex];
    f = new int[al.n_vertex];
    p = new int[al.n_vertex];
    t = 0;
    for (int i = 0; i < al.n_vertex; i++) {
        c[i] = WHITE; d[i] = f[i] = 0; p[i] = NIL;
    }
    for (int i = 0; i < al.n_vertex; i++)
        if (c[i] == WHITE) {
            visit(i);
            topological_sort.push_back(i);
        }
}
DFS::DFS(const graph::AList& al) { init(al); }
DFS::DFS(const graph::AMatrix& am) { init(*(new graph::AList(am))); }

void DFS::visit(int u) {
    c[u] = GRAY;
    d[u] = ++t;
    for (int j = 0; j < al->size(u); j++) {
        int v = al->get(u, j);
        if (c[v] == WHITE) {
            p[v] = u;
            visit(v);
            topological_sort.push_back(v);
        }
    }
    c[u] = BLACK;
    f[u] = ++t;
}

int DFS::get(int i) {
    int min1 = INF, min2 = NINF, ntx = NIL;
    for (int j = 0; j <= i; j++) {
        for (int k = 0; k < al->n_vertex; k++)
            if (f[k] < min1 && f[k] > min2) { min1 = f[k]; ntx = k; }
        min2 = min1; min1 = INF;
    }
    return ntx;
}