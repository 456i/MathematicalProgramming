import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

os.makedirs("output", exist_ok=True)


def prettify_xml(elem):
    """Красивое форматирование XML"""
    rough_string = ET.tostring(elem, encoding="unicode")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def create_topological_sort():
    """
    Создаёт полную визуализацию топологической сортировки
    с поэтапным изменением графа для Draw.io
    """
    # Создаём корневую структуру XML
    mxfile = ET.Element(
        "mxfile", host="app.diagrams.net", version="21.0.0", type="device"
    )
    diagram = ET.SubElement(
        mxfile, "diagram", name="Топологическая сортировка", id="topo_sort"
    )
    mxGraphModel = ET.SubElement(
        diagram,
        "mxGraphModel",
        dx="1200",
        dy="800",
        grid="1",
        gridSize="10",
        guides="1",
        tooltips="1",
        connect="1",
        arrows="1",
        fold="1",
        page="1",
        pageScale="1",
        pageWidth="827",
        pageHeight="1169",
    )
    root = ET.SubElement(mxGraphModel, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    # Граф из документа: 7 вершин (0-6)
    # Рёбра: 0→1, 0→2, 0→3, 1→3, 2→3, 2→5, 4→1, 4→3, 5→3, 5→6
    node_positions = {
        "0": (100, 150),
        "1": (250, 80),
        "2": (250, 150),
        "3": (400, 150),
        "4": (100, 80),
        "5": (400, 220),
        "6": (550, 220),
    }

    edges = [
        ("0", "1"),
        ("0", "2"),
        ("0", "3"),
        ("1", "3"),
        ("2", "3"),
        ("2", "5"),
        ("4", "1"),
        ("4", "3"),
        ("5", "3"),
        ("5", "6"),
    ]

    # F-значения из документа
    f_values = {"0": 14, "1": 13, "2": 12, "3": 11, "4": 10, "5": 5, "6": 4}

    # Шаги визуализации DFS
    steps = [
        {
            "title": "Шаг 0: Исходный граф",
            "desc": "Граф с 7 вершинами. Применяем DFS для топологической сортировки",
            "visited": [],
            "processing": None,
            "finished": [],
            "current_edges": [],
        },
        {
            "title": "Шаг 1: Посещаем вершину 0 (D[0]=1)",
            "desc": "Начинаем DFS с вершины 0. Вершина окрашена в серый (в процессе)",
            "visited": ["0"],
            "processing": "0",
            "finished": [],
            "current_edges": [],
        },
        {
            "title": "Шаг 2: Посещаем вершину 1 (D[1]=2)",
            "desc": "Из 0 идём в 1. Исследуем смежные вершины",
            "visited": ["0", "1"],
            "processing": "1",
            "finished": [],
            "current_edges": [("0", "1")],
        },
        {
            "title": "Шаг 3: Посещаем вершину 3 (D[3]=3)",
            "desc": "Из 1 идём в 3. Вершина 3 не имеет непосещённых смежных",
            "visited": ["0", "1", "3"],
            "processing": "3",
            "finished": [],
            "current_edges": [("0", "1"), ("1", "3")],
        },
        {
            "title": "Шаг 4: Завершаем вершину 3 (F[3]=4)",
            "desc": "Вершина 3 обработана полностью. F[3]=4, добавляем в начало результата",
            "visited": ["0", "1", "3"],
            "processing": None,
            "finished": ["3"],
            "current_edges": [("0", "1"), ("1", "3")],
        },
        {
            "title": "Шаг 5: Завершаем вершину 1 (F[1]=5)",
            "desc": "Вершина 1 обработана. F[1]=5. Возврат к вершине 0",
            "visited": ["0", "1", "3"],
            "processing": None,
            "finished": ["3", "1"],
            "current_edges": [("0", "1"), ("1", "3")],
        },
        {
            "title": "Шаг 6: Посещаем вершину 2 (D[2]=6)",
            "desc": "Из 0 идём в 2. Исследуем смежные: 3 (уже посещена), 5",
            "visited": ["0", "1", "3", "2"],
            "processing": "2",
            "finished": ["3", "1"],
            "current_edges": [("0", "1"), ("1", "3"), ("0", "2")],
        },
        {
            "title": "Шаг 7: Посещаем вершину 5 (D[5]=7)",
            "desc": "Из 2 идём в 5. Исследуем смежные: 3 (посещена), 6",
            "visited": ["0", "1", "3", "2", "5"],
            "processing": "5",
            "finished": ["3", "1"],
            "current_edges": [("0", "1"), ("1", "3"), ("0", "2"), ("2", "5")],
        },
        {
            "title": "Шаг 8: Посещаем вершину 6 (D[6]=8)",
            "desc": "Из 5 идём в 6. Вершина 6 не имеет непосещённых смежных",
            "visited": ["0", "1", "3", "2", "5", "6"],
            "processing": "6",
            "finished": ["3", "1"],
            "current_edges": [
                ("0", "1"),
                ("1", "3"),
                ("0", "2"),
                ("2", "5"),
                ("5", "6"),
            ],
        },
        {
            "title": "Шаг 9: Завершаем вершины 6, 5, 2, 0",
            "desc": "F[6]=11, F[5]=12, F[2]=13, F[0]=14. Возврат из рекурсии",
            "visited": ["0", "1", "3", "2", "5", "6"],
            "processing": None,
            "finished": ["3", "1", "6", "5", "2", "0"],
            "current_edges": [
                ("0", "1"),
                ("1", "3"),
                ("0", "2"),
                ("2", "5"),
                ("5", "6"),
            ],
        },
        {
            "title": "Шаг 10: Посещаем вершину 4 (D[4]=9)",
            "desc": "Новый запуск DFS для несвязного компонента. Вершина 4",
            "visited": ["0", "1", "3", "2", "5", "6", "4"],
            "processing": "4",
            "finished": ["3", "1", "6", "5", "2", "0"],
            "current_edges": [
                ("0", "1"),
                ("1", "3"),
                ("0", "2"),
                ("2", "5"),
                ("5", "6"),
            ],
        },
        {
            "title": "Шаг 11: Завершаем вершину 4 (F[4]=10)",
            "desc": "Смежные 1 и 3 уже посещены. F[4]=10. DFS завершён",
            "visited": ["0", "1", "3", "2", "5", "6", "4"],
            "processing": None,
            "finished": ["3", "1", "6", "5", "2", "0", "4"],
            "current_edges": [
                ("0", "1"),
                ("1", "3"),
                ("0", "2"),
                ("2", "5"),
                ("5", "6"),
                ("4", "1"),
                ("4", "3"),
            ],
        },
        {
            "title": "Шаг 12: Результат - Топологический порядок 0→2→5→6→4→1→3",
            "desc": "Порядок по убыванию F[v]: F[0]=14, F[2]=13, F[5]=12, F[6]=11, F[4]=10, F[1]=5, F[3]=4",
            "visited": ["0", "1", "3", "2", "5", "6", "4"],
            "processing": None,
            "finished": ["0", "2", "5", "6", "4", "1", "3"],
            "current_edges": edges,
        },
    ]

    # Генерируем элементы для каждого шага
    for step_idx, step in enumerate(steps):
        y_offset = step_idx * 330

        # Заголовок шага
        title_id = f"ts_title_{step_idx}"
        ET.SubElement(
            root,
            "mxCell",
            id=title_id,
            value=step["title"],
            style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=13;fontStyle=1",
            vertex="1",
            parent="1",
        )
        ET.SubElement(
            root[-1],
            "mxGeometry",
            x="50",
            y=str(y_offset + 10),
            width="700",
            height="25",
            **{"as": "geometry"},
        )

        # Описание шага
        desc_id = f"ts_desc_{step_idx}"
        ET.SubElement(
            root,
            "mxCell",
            id=desc_id,
            value=step["desc"],
            style="text;html=1;strokeColor=none;fillColor=#f5f5f5;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=10",
            vertex="1",
            parent="1",
        )
        ET.SubElement(
            root[-1],
            "mxGeometry",
            x="50",
            y=str(y_offset + 40),
            width="650",
            height="25",
            **{"as": "geometry"},
        )

        # Узлы (вершины графа)
        node_ids = {}
        for node_name, (x, y) in node_positions.items():
            node_id = f"ts_node_{step_idx}_{node_name}"
            node_ids[node_name] = node_id

            # Определяем цвет и метку вершины
            if node_name in step["finished"]:
                color = "#d5e8d4"  # Зелёный - обработано
                label = f"{node_name}\nF={f_values[node_name]}"
            elif node_name == step["processing"]:
                color = "#fff2cc"  # Жёлтый - в процессе
                label = f"{node_name}\nпроцесс"
            elif node_name in step["visited"]:
                color = "#dae8fc"  # Голубой - посещено
                label = node_name
            else:
                color = "#f5f5f5"  # Серый - не посещено
                label = node_name

            ET.SubElement(
                root,
                "mxCell",
                id=node_id,
                value=label,
                style=f"ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor={color};strokeColor=#000000;fontSize=11;fontStyle=1",
                vertex="1",
                parent="1",
            )
            ET.SubElement(
                root[-1],
                "mxGeometry",
                x=str(x),
                y=str(y_offset + y),
                width="60",
                height="60",
                **{"as": "geometry"},
            )

        # Рёбра графа
        for edge_idx, (source, target) in enumerate(edges):
            edge_id = f"ts_edge_{step_idx}_{edge_idx}"

            # Определяем цвет и толщину ребра
            if (source, target) in step["current_edges"]:
                color = "#82b366"  # Зелёный - активное
                width = 3
            else:
                color = "#666666"  # Серый - неактивное
                width = 1

            ET.SubElement(
                root,
                "mxCell",
                id=edge_id,
                value="",
                style=f"rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={color};strokeWidth={width};endArrow=classic;",
                edge="1",
                parent="1",
                source=node_ids[source],
                target=node_ids[target],
            )
            ET.SubElement(root[-1], "mxGeometry", relative="1", **{"as": "geometry"})

    # Сохраняем XML в файл
    xml_str = prettify_xml(mxfile)
    output_path = "output/topological_sort.drawio"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml_str)

    print(f"✓ Файл создан: {output_path}")
    print(f"  Всего шагов: {len(steps)}")
    print(f"  Вершин в графе: {len(node_positions)}")
    print(f"  Рёбер в графе: {len(edges)}")

    return output_path


# Запускаем генерацию
result_path = create_topological_sort()
print(f"\n✅ Топологическая сортировка готова!")
print(f"📁 Файл сохранён: {result_path}")
