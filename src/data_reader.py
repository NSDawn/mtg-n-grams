import json
import tokenizer

def read_in_json(path: str) -> list[object]:
    with open(path) as f:
        d = json.load(f)
    return d

def write_out_json(data: any, path: str):
    with open(path, "w") as f:
        json.dump(data, f)
        

def slimify_data_object(obj: object) -> object:
    return {
        "id": obj.get("id", None),
        "name": obj.get("name", None),
        "oracle_text": obj.get("oracle_text", None),
    }

def slimify_data(data: list[object]) -> list[object]:
    return [slimify_data_object(obj) for obj in data]

def main():
    D = read_in_json("../data/oracle_cards_data.json")
    write_out_json(slimify_data(D), "../data/data.json")
    

if __name__ == "__main__":
    main()