from collections import Counter

def distance (word1, word2, ind1, ind2, dist):
    if (dist > 2):
        return 4
    if (len(word1) == ind1):
        dist += len(word2) - ind2
        if (dist <= 2) :
            return dist
        else:
            return 4
    if (len(word2) == ind2):
        dist += len(word1) - ind1
        if (dist <= 2) :
            return dist
        else:
            return 4
    if (word1[ind1] == word2[ind2]):
        return distance(word1, word2, ind1 + 1, ind2 + 1, dist)
    return min(distance(word1, word2, ind1 + 1, ind2, dist + 1), distance(word1, word2, ind1, ind2 + 1, dist + 1),
               distance(word1, word2, ind1 + 1, ind2 + 1, dist + 1))


def parse(s):
    ans = 0
    for i in range(len(s)):
        ans *= 10
        ans += ord(s[i]) - ord('0')
    return ans

text_file = open("brain143.txt", "r", encoding='utf-8')
dict_file = open("dict1.txt", "r")
ans13 = open("text_without_signs.txt", "w", encoding='utf-8')
ans2 = open("text_with_correction.txt", "w")

text = text_file.read()
text_copy = text
text = text.replace("?", "")
text = text.replace("!", "")
text = text.replace("»", "")
text = text.replace("«", "")
text = text.replace(":", "")
text = text.replace(";", "")
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("(", "")
text = text.replace(")", "")
text = text.lower()
text_list = text.split()
text_list.sort()
print(text_list, file=ans13)


kolich = Counter(text_list)

print("Количество словоформ: ", len(text_list))
print("Количество различных словоформ: ", len(kolich))

set_from_dict = set()
set_variety = dict()
set_unknown = set()
dict1 = dict_file.readlines()
for i in range(len(dict1)):
    pair = dict1[i].split(" ")
    set_variety[pair[0]] = pair[1]
    set_from_dict.add(pair[0])
# print(*set_from_dict)
frequency_slovoform = 0
for i in text_list:
    if (i in set_from_dict):
        frequency_slovoform += 1
    else:
        print(i)
        set_unknown.add(i)
print("количество словоформ присутствующих в словаре: ", frequency_slovoform)
print("количество словоформ не присутствующих в словаре:", len(text_list) - frequency_slovoform)

ans_dict = dict()
for i in set_unknown:
    key = 3
    chart = 0
    word1 = ""
    word2 = ""
    for u in range (len(i) - 1):
        s = i[:u]
        t = i[u:]
        print(s, t)
        if (len(s) > 0):
            for j in set_variety:
                value = distance(s, j, 0, 0, 1)
                if value != 4:
                    for h in set_variety:
                        value1 = distance(t, h, 0, 0, value)
                        if (value + value1 < key):
                            key = value + value1
                            word1 = j
                            word2 = h
                            chart = parse(set_variety[j] + set_variety[h])
                        elif (value + value1 == key):
                            if (parse(set_variety[j] + set_variety[h]) > chart):
                                chart = parse(set_variety[j] + set_variety[h])
                                word1 = j
                                word2 = h
        else:
            for h in set_variety:
                value = distance(t, h, 0, 0, 0)
                if (value < key):
                    key = value
                    word1 = ""
                    word2 = h
                    chart = parse(set_variety[h])
                elif (value == key):
                    if (parse(set_variety[h]) > chart):
                        chart = parse(set_variety[h])
                        word1 = ""
                        word2 = h
    if (word2 == ""):
        ans_dict[i] = -1
    else:
        ans_dict[i] = word1 + " " + word2
print(ans_dict)
text_copy_list = text_copy.split("\n")
for i in text_copy_list:
    i = i.split()
    for j in i:
        j_copy = j
        j = j.replace("(", "")
        j = j.replace(")", "")
        j = j.replace("!", "")
        j = j.replace("-", "")
        f = 0
        s = 0
        t = 0
        if (not (j in set_unknown)):
            print(j_copy, end=" ", file=ans2)
        elif ans_dict[j] == -1:
            #print(j)
            print(j_copy, end=" ", file=ans2)
        else:
            while(t < len(j_copy)):
                if (s < len(j) and j[s] == j_copy[t]):
                    print(ans_dict[j][f], end='', file=ans2)
                    s += 1
                    f += 1
                    t += 1
                    if (s == len(j) or f == len(ans_dict[j])):
                        print(ans_dict[j][f:], end='', file=ans2)
                        s = len(j)
                else:
                    print(j_copy[t], end='', file=ans2)
                    t += 1
            print(" ", end='', file=ans2)
    print('', file=ans2)

corrected = open("text_with_correction.txt", "r")
corrected_text = corrected.read()
corrected_text = corrected_text.replace("?", "")
corrected_text = corrected_text.replace("!", "")
corrected_text = corrected_text.replace("»", "")
corrected_text = corrected_text.replace("«", "")
corrected_text = corrected_text.replace(":", "")
corrected_text = corrected_text.replace(";", "")
corrected_text = corrected_text.replace(",", "")
corrected_text = corrected_text.replace(".", "")
corrected_text = corrected_text.replace("(", "")
corrected_text = corrected_text.replace(")", "")
corrected_text = corrected_text.lower()
corrected_text_list = corrected_text.split()

print("количество словоформ в исправленном тексте: ", len(corrected_text_list))
kolich1 = Counter(corrected_text_list)
print("количество различных словоформ в исправленном тексте: ", len(kolich1))
