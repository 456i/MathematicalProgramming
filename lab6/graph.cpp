#include "graph.h"

namespace graph {

    AMatrix::AMatrix(int n) {
        n_vertex = n;
        mr = new int[n * n];
        for (int i = 0; i < n * n; i++) mr[i] = 0;
    }
    AMatrix::AMatrix(int n, int m[]) { n_vertex = n; mr = m; }
    AMatrix::AMatrix(const AMatrix& am) {
        n_vertex = am.n_vertex;
        mr = new int[n_vertex * n_vertex];
        for (int i = 0; i < n_vertex; i++)
            for (int j = 0; j < n_vertex; j++)
                set(i, j, am.get(i, j));
    }
    AMatrix::AMatrix(const AList& al) {
        n_vertex = al.n_vertex;
        mr = new int[n_vertex * n_vertex];
        for (int k = 0; k < n_vertex * n_vertex; k++) mr[k] = 0;
        for (int i = 0; i < n_vertex; i++)
            for (int j = 0; j < al.size(i); j++)
                set(i, al.get(i, j), 1);
    }
    void AMatrix::set(int i, int j, int r) { mr[i * n_vertex + j] = r; }
    int  AMatrix::get(int i, int j) const { return mr[i * n_vertex + j]; }

    void AList::create(int n) { mr = new std::list<int>[n_vertex = n]; }
    AList::AList(int n) { create(n); }
    AList::AList(int n, int m[]) {
        create(n);
        for (int i = 0; i < n_vertex; i++)
            for (int j = 0; j < n_vertex; j++)
                if (m[i * n_vertex + j] != 0) add(i, j);
    }
    AList::AList(const AMatrix& am) {
        create(am.n_vertex);
        for (int i = 0; i < n_vertex; i++)
            for (int j = 0; j < n_vertex; j++)
                if (am.get(i, j) != 0) add(i, j);
    }
    AList::AList(const AList& al) {
        create(al.n_vertex);
        for (int i = 0; i < n_vertex; i++)
            for (int j = 0; j < al.size(i); j++)
                add(i, al.get(i, j));
    }
    void AList::add(int i, int j) { mr[i].push_back(j); }
    int  AList::size(int i) const { return (int)mr[i].size(); }
    int  AList::get(int i, int j) const {
        auto it = mr[i].begin();
        for (int k = 0; k < j; k++) ++it;
        return *it;
    }

} // namespace graph