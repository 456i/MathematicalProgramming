// --- main.cpp ---
#include <iostream>
#include "graph.h"
#include "bfs.h"
#include "dfs.h"

int main() {
    int m[7][7] = {
        {0,1,1,1,0,0,0},
        {0,0,0,1,0,0,0},
        {0,0,0,1,0,1,0},
        {0,0,0,0,0,0,0},
        {0,1,0,1,0,0,0},
        {0,0,0,1,0,0,1},
        {0,0,0,0,1,0,0}
    };

    graph::AMatrix gm(7, (int*)m);

    std::cout << "\n-- Матрица смежности --\n";
    for (int i = 0; i < gm.n_vertex; i++) {
        for (int j = 0; j < gm.n_vertex; j++)
            std::cout << gm.get(i, j) << " ";
        std::cout << "\n";
    }

    graph::AList gl(gm);
    std::cout << "\n-- Список смежности --\n";
    for (int i = 0; i < gl.n_vertex; i++) {
        std::cout << i << ": ";
        for (int j = 0; j < gl.size(i); j++)
            std::cout << gl.get(i, j) << " ";
        std::cout << "\n";
    }

    BFS bfs(gl, 0);
    std::cout << "\n-- Поиск в ширину (BFS, старт=0) --\n";
    int v;
    while ((v = bfs.get()) != BFS::NIL)
        std::cout << v << " ";
    std::cout << "\n";

    DFS dfs(gl);
    std::cout << "\n-- Поиск в глубину (DFS) --\n";
    for (int i = 0; i < gl.n_vertex; i++)
        std::cout << dfs.get(i) << " ";
    std::cout << "\n";

    std::cout << "\n-- Топологическая сортировка --\n";
    for (auto it = dfs.topological_sort.begin(); it != dfs.topological_sort.end(); ++it)
        std::cout << *it << " ";
    std::cout << "\n";

    return 0;
}