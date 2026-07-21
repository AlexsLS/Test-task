import json
import sys
def fill_values(node, values_map):
    if "id" in node:
        test_id = node["id"]
        if test_id in values_map:
            node["value"] = values_map[test_id]
    for key in ("tests", "values"):
        if key in node:
            for child in node[key]:
                fill_values(child, values_map)
def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py values.json tests.json report.json")
        return
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    with open(values_file, "r") as f:
        values_data = json.load(f)
    values_map = {item["id"]: item["value"] for item in values_data["values"]}
    with open(tests_file, "r") as f:
        tests_data = json.load(f)
    fill_values(tests_data, values_map)
    with open(report_file, "w") as f:
        json.dump(tests_data, f, indent=4)
    print("Готово. report.json сформирован.")
if __name__ == "__main__":
    main()
