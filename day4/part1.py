with open("inputs/full") as file:
    papers: int = 0
    stuck: int = 0
    lines = [line.rstrip() for line in file]
    counter = [[0] * len(lines[0]) for _ in range(len(lines))]
    for i, v in enumerate(lines):
        for j, c in enumerate(v):
            if c != "@":
                continue
            papers += 1
            for dr, dc in [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]:
                ni, nj = i + dr, j + dc
                if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]):
                    if lines[ni][nj] == "@":
                        counter[ni][nj] += 1
                        if counter[ni][nj] == 4:
                            stuck += 1

    print(str(papers - stuck))
