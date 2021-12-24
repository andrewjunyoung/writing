import yaml

file_path = 'IPA_symbols.yaml'

def main():
    print(get_symbol_string())

def get_symbol_string():
    with open(file_path, 'r') as file:
        symbol_dict = yaml.safe_load(file)

    symbol_list = list(get_nested_values(symbol_dict))
    flat_symbol_list = flatten_list(symbol_list)
    symbol_string = "".join(flat_symbol_list)
    return symbol_string

def flatten_list(l: list):
    return [
        item
        for sublist in l
        for item in sublist
    ]



def get_nested_values(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from get_nested_values(v)
    else:
      yield v

if __name__ == '__main__':
    main()
