# UGC 2 JSON CONVERTER
# Version 1.1
#
# Created by Ruggery Iury Corrêa
# GitHub: https://github.com/ruggeryiury
#
# Get the latest version of this script through the
# UGC to JSON Converter GitHub Repository
# https://github.com/ruggeryiury/ugc2json_converter


import json
import os

script_path: str = os.path.dirname(__file__)


def type_key_value(key_value: str) -> str | int | float | bool:
    new_value: str | int | float | bool
    try:
        new_value = int(key_value)
    except ValueError:
        try:
            new_value = float(key_value)
        except ValueError:
            if key_value == "TRUE":
                new_value = True
            elif key_value == "FALSE":
                new_value = False
            else:
                if key_value[0] == '"':
                    new_value = key_value[1:-1]
                else:
                    new_value = key_value

    return new_value


def ugc_parser(file_name: str) -> None:
    operator = []
    root_list = False
    ugc_file = open(os.path.join(script_path, '{}.ugc'.format(
        file_name)), 'r', encoding='utf-8').readlines()
    new_file = open(os.path.join(
        script_path, '{}.json'.format(file_name)), 'w', encoding='utf-8')
    new_json = {}
    for line in ugc_file:
        operator_index: int = len(operator) - 1
        line = line.lstrip().rstrip().split()

        # This will detect if line is empty
        if len(line) == 0:
            pass

        else:
            key_name = line[0]
            key_value = ' '.join(str(i) for i in line[1:])

            # This will detect if line is a comment
            if key_name == "##":
                pass

            # This will detect if the root type is a list
            elif key_name == '#declare':
                if key_value == 'list':
                    new_json = []
                    root_list = True

            # This will detect if line is declaring a new dict
            elif key_name == "#set":
                if operator_index == -1:
                    operator.append({
                        "name": key_value,
                        "type": "SET",
                        "content": {}
                    })
                    if operator_index == -1:
                        if root_list:
                            new_json.append({})
                        else:
                            new_json[key_value] = {}
                    else:
                        operator[operator_index]['content'][key_value] = {}
                else:
                    if operator[operator_index]['type'] == "LIST":
                        operator.append({
                            "name": None,
                            "type": "SET",
                            "content": {}
                        })
                    else:
                        operator.append({
                            "name": key_value,
                            "type": "SET",
                            "content": {}
                        })
                        if operator_index == -1:
                            new_json[key_value] = {}
                        else:
                            operator[operator_index]['content'][key_value] = {}
            elif key_name == "#endset":
                if operator[operator_index - 1]['type'] == "LIST":
                    operator[operator_index -
                             1]['content'].append(operator[operator_index]['content'])
                    operator.pop(operator_index)
                else:
                    if operator_index == 0:
                        if root_list:
                            new_json[len(new_json) -
                                     1] = operator[operator_index]['content']
                            operator.pop(operator_index)
                        else:
                            new_json[operator[operator_index]['name']
                                     ] = operator[operator_index]['content']
                            operator.pop(operator_index)
                    else:
                        operator[operator_index - 1]['content'][operator[operator_index]
                                                                ['name']] = operator[operator_index]['content']
                        operator.pop(operator_index)

            # This will detect if line is declaring a new list
            elif key_name == "#list":
                if operator_index == -1:
                    operator.append({
                        "name": key_value,
                        "type": "LIST",
                        "content": []
                    })
                    if operator_index == -1:
                        if root_list:
                            new_json.append([])
                        else:
                            new_json[key_value] = []
                    else:
                        operator[operator_index]['content'][key_value] = []
                else:
                    if operator[operator_index]['type'] == "LIST":
                        operator.append({
                            "name": None,
                            "type": "LIST",
                            "content": []
                        })
                    else:
                        operator.append({
                            "name": key_value,
                            "type": "LIST",
                            "content": []
                        })
                        if operator_index == -1:
                            new_json[key_value] = []
                        else:
                            operator[operator_index]['content'][key_value] = []
            elif key_name == "#endlist":
                if operator_index == 0:
                    if root_list:
                        new_json[len(new_json) -
                                 1] = operator[operator_index]['content']
                        operator.pop(operator_index)
                    else:
                        new_json[operator[operator_index]['name']
                                 ] = operator[operator_index]['content']
                        operator.pop(operator_index)
                else:
                    if operator[operator_index - 1]['type'] == "LIST":
                        operator[operator_index -
                                 1]['content'].append(operator[operator_index]['content'])
                        operator.pop(operator_index)
                    else:
                        if operator_index == 0:
                            new_json[operator[operator_index]['name']
                                     ] = operator[operator_index]['content']
                            operator.pop(operator_index)
                        else:
                            operator[operator_index - 1]['content'][operator[operator_index]
                                                                    ['name']] = operator[operator_index]['content']
                            operator.pop(operator_index)

            # Else (generally meaning this is a line with key/value entries)
            else:

                # This will detect where the key/value will be placed
                if operator_index == -1:
                    if root_list:
                        # Will be placed on the root list
                        new_json.append(type_key_value(key_name))
                    else:
                        # Will be placed on the root dict
                        new_json[key_name] = type_key_value(key_value)
                else:
                    # Will be placed on the last object on operator list

                    # Checking type
                    if operator[operator_index]['type'] == "SET":
                        operator[operator_index]['content'][key_name] = type_key_value(
                            key_value)
                    elif operator[operator_index]['type'] == "LIST":
                        key_value = ' '.join(str(i) for i in line)
                        operator[operator_index]['content'].append(
                            type_key_value(key_value))

    json.dump(new_json, new_file, ensure_ascii=False, indent=4)
    new_file.close()


def init() -> None:
    """
    Main function: UGC to JSON Converter.
    """
    for root, dirs, files in os.walk(script_path):
        for file in files:
            if file.endswith(".ugc"):
                file_name = file[:-4]
                ugc_parser(file_name)


init()