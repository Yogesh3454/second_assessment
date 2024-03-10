
def generate_output(input_dict):
    output = {}

    def traverse(dictionary, path=[]):
        for key, value in dictionary.items():
            new_path = path + [key]
            if isinstance(value, dict):
                traverse(value, new_path)
            else:
                current = output
                for item in new_path[:-1]:
                    if item not in current:
                        current[item] = []
                    current = current[item]
                current.append(new_path[-1])

    traverse(input_dict)
    return output

def format_output(output):
    formatted_output = {}
    for key, value in output.items():
        formatted_output[key] = []
        if isinstance(value, list):
            formatted_output[key] = value
        else:
            format_output(value)
            formatted_output[key].extend(value)

    return formatted_output

input_dict = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}
output = generate_output(input_dict)
formatted_output = format_output(output)
print(formatted_output)