import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "app", "blueprints")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "merged_postman_collection.json")


def load_collections():
    collections = []

    for root, _, files in os.walk(INPUT_DIR):
        for file_name in sorted(files):
            if not file_name.endswith(".json"):
                continue

            path = os.path.join(root, file_name)
            print(f"Checking: {path}")

            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                if "info" in data and "item" in data:
                    collections.append(
                        {"file_name": file_name, "path": path, "data": data}
                    )
                    print(f"Loaded valid collection: {path}")
                else:
                    print(f"Skipped invalid Postman collection: {path}")

            except Exception as e:
                print(f"Skipped unreadable JSON: {path} -> {e}")

    return collections


def merge_items(collections):
    merged_items = []
    folder_map = {}

    for col in collections:
        for item in col["data"].get("item", []):
            if isinstance(item, dict) and "item" in item:
                name = item.get("name", "Unnamed Folder")

                if name not in folder_map:
                    folder_copy = {"name": name, "item": list(item["item"])}
                    folder_map[name] = folder_copy
                    merged_items.append(folder_copy)
                else:
                    folder_map[name]["item"].extend(item["item"])
            else:
                merged_items.append(item)

    return merged_items


def main():
    if not os.path.exists(INPUT_DIR):
        raise RuntimeError(f"Directory not found: {INPUT_DIR}")

    collections = load_collections()

    if not collections:
        raise RuntimeError("No valid collections found.")

    base = collections[0]["data"]

    merged = {
        "info": {
            **base.get("info", {}),
            "name": f"{base.get('info', {}).get('name', 'Merged Collection')} - Combined",
        },
        "item": merge_items(collections),
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2)

    print(f"Merged {len(collections)} collections into {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
