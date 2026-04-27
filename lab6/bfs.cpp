#include "bfs.h"

void BFS::init(const graph::AList& al, int s) {
    this->al = &al;
    c = new Color[al.n_vertex];
    d = new int[al.n_vertex];
    p = new int[al.n_vertex];
    for (int i = 0; i < al.n_vertex; i++) {
        c[i] = WHITE; d[i] = INF; p[i] = NIL;
    }
    c[s] = GRAY; d[s] = 0;
    q.push(s);
}
BFS::BFS(const graph::AList& al, int s) { init(al, s); }
BFS::BFS(const graph::AMatrix& am, int s) { init(*(new graph::AList(am)), s); }

int BFS::get() {
    int rc = NIL, v = NIL;
    if (!q.empty()) {
        rc = q.front();
        for (int j = 0; j < al->size(rc); j++)
            if (c[v = al->get(rc, j)] == WHITE) {
                c[v] = GRAY;
                d[v] = d[rc] + 1;
                p[v] = rc;
                q.push(v);
            }
        q.pop();
        c[rc] = BLACK;
    }
    return rc;
}