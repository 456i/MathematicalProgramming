// --- graph.h ---
#pragma once
#include <list>

namespace graph {
    struct AList;

    struct AMatrix {
        int n_vertex;  // количество вершин
        int* mr;       // плоский массив матрицы n×n, индекс: mr[i*n_vertex+j]

        AMatrix(int n);                 // создаёт нулевую матрицу n×n
        AMatrix(int n, int mr[]);       // берёт указатель на готовый массив (без копирования!)
        AMatrix(const AMatrix& am);     // глубокая копия матрицы
        AMatrix(const AList& al);       // конвертация: список смежности → матрица

        void set(int i, int j, int r);  // mr[i][j] = r
        int  get(int i, int j) const;   // возвращает mr[i][j]
    };

    struct AList {
        int n_vertex;          // количество вершин
        std::list<int>* mr;    // массив списков: mr[i] — соседи вершины i

        void create(int n);             // выделяет массив из n пустых списков

        AList(int n);                   // пустой список смежности на n вершин
        AList(int n, int mr[]);         // строит из плоского массива матрицы n×n
        AList(const AMatrix& am);       // конвертация: матрица → список смежности
        AList(const AList& al);         // глубокая копия

        void add(int i, int j);         // добавляет j в список соседей вершины i
        int  size(int i) const;         // количество соседей вершины i
        int  get(int i, int j) const;   // j-й сосед вершины i (0-based)
    };
}