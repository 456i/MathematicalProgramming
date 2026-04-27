// --- dfs.h ---
#pragma once
#include "graph.h"
#include <vector>

struct DFS {
    const static int NIL = -1;         // нет вершины / нет предшественника

    enum Color { WHITE, GRAY, BLACK }; // WHITE — не посещена
    // GRAY  — в процессе обхода
    // BLACK — обработана полностью

    const graph::AList* al;  // ссылка на граф
    Color* c;                // c[v]  — цвет вершины v
    int* d;                  // d[v]  — время обнаружения (шаг окраски в GRAY)
    int* f;                  // f[v]  — время фиксации (шаг окраски в BLACK)
    int* p;                  // p[v]  — предшественник v в DFS-дереве
    int  t;                  // текущий счётчик времени

    std::vector<int> topological_sort; // результат топологической сортировки
    // заполняется автоматически при init()

    DFS(const graph::AList& al);   // запускает DFS по всем вершинам графа
    DFS(const graph::AMatrix& am); // конвертирует матрицу → список, затем DFS

    void init(const graph::AList& al); // инициализация + запуск visit() для всех WHITE вершин

    void visit(int u); // рекурсивный обход вглубь от вершины u
    // заполняет d, f, p и topological_sort

    int get(int i);    // возвращает вершину с i-м наименьшим f[v]
    // используется для вывода порядка DFS
    // i=0 → вершина с минимальным f, i=n-1 → с максимальным
};