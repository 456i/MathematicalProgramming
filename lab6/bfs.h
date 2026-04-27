// --- bfs.h ---
#pragma once
#include "graph.h"
#include <queue>

struct BFS {
    const static int INF = 0x7fffffff;  // "бесконечность" для расстояний
    const static int NIL = -1;          // нет вершины / нет предшественника

    enum Color { WHITE, GRAY, BLACK };  // WHITE — не посещена
    // GRAY  — в очереди
    // BLACK — обработана

    const graph::AList* al;  // ссылка на граф
    Color* c;                // c[v]  — цвет вершины v
    int* d;                  // d[v]  — расстояние от старта до v
    int* p;                  // p[v]  — предшественник v в BFS-дереве
    std::queue<int> q;       // очередь вершин (FIFO)

    BFS(const graph::AList& al, int s);   // запуск BFS от вершины s
    BFS(const graph::AMatrix& am, int s); // конвертирует матрицу → список, затем BFS от s

    void init(const graph::AList& al, int s); // инициализация массивов + старт

    int get(); // возвращает следующую вершину в порядке обхода
    // NIL если очередь пуста (обход завершён)
};