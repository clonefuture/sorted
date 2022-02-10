def sorter_file():
    import os
    text_dict = {}
    for root, dirs, files in os.walk("."):
        for filename in files:
            if '.txt' in filename:
                with open(filename, encoding='utf-8') as f:
                    text_list = []
                    cnt_line = 0
                    for line in f:
                        text_list.append(line.strip())
                        cnt_line += 1
                    text_dict[filename] = text_list

    sorted_list = sorted(text_dict.values(), key=len)
    sorted_dict = {}

    for lt in sorted_list:
        for k, v in text_dict.items():
            if v == lt:
                sorted_dict[k] = lt

    lines = []
    for k, v in sorted_dict.items():
        lines.append(k)
        lines.append(str(len(v)))
        for val in v:
            lines.append(val)

    with open('sorted.txt', 'w', encoding='utf-8') as doc:
        for line in lines:
            doc.write(line + '\n')


sorter_file()
