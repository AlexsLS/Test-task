import sys
def read_ellipse(filename):
    with open(filename, "r") as f:
        xc, yc = map(float, f.readline().split())
        a, b = map(float, f.readline().split())
    return xc, yc, a, b
def read_points(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.split())
                points.append((x, y))
    return points
def classify_point(x, y, xc, yc, a, b):
    val = ((x - xc)**2) / (a*a) + ((y - yc)**2) / (b*b)
    if abs(val - 1.0) < 1e-12:
        return 0
    elif val < 1.0:
        return 1
    else:
        return 2
def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py ellipse.txt points.txt")
        return
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    xc, yc, a, b = read_ellipse(ellipse_file)
    points = read_points(points_file)
    for x, y in points:
        print(classify_point(x, y, xc, yc, a, b))
if __name__ == "__main__":
    main()
