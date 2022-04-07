import os
import math
import jieba


def entropy_calculate(path, is_chara):
    files = os.listdir(path)
    data = []
    replace = '[a-zA-Z0-9’!"#$%&\'()*+,-./:：;「<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+\n\u3000 '
    for file in files:
        with open(path + '/' + file, 'r', encoding='ANSI') as f:
            t = f.read()
            for i in replace:
                t = t.replace(i, '')
            if is_chara:
                data.append(t)
            else:
                c = jieba.lcut(t)
                data.append(c)
        f.close()

    uni_chara = {}
    uni_count = 0
    for i in data:
        for j in range(len(i)):
            uni_chara[i[j]] = uni_chara.get(i[j], 0) + 1
            uni_count += 1

    bi_chara = {}
    bi_count = 0
    for i in data:
        for j in range(len(i)-1):
            bi_chara[(i[j], i[j+1])] = bi_chara.get((i[j], i[j+1]), 0) + 1
            bi_count += 1

    tri_chara = {}
    tri_count = 0
    for i in data:
        for j in range(len(i)-2):
            tri_chara[(i[j], i[j+1], i[j+2])] = tri_chara.get((i[j], i[j+1], i[j+2]), 0) + 1
            tri_count += 1

    uni_entropy = (sum(-(chara[1])*math.log2(chara[1]/uni_count) for chara in uni_chara.items()))/uni_count
    bi_entropy = (sum(-(chara[1])*math.log2((chara[1]/bi_count)/(uni_chara[chara[0][0]]/uni_count)) for chara in bi_chara.items()))/bi_count
    tri_entropy = (sum(-(chara[1])*math.log2((chara[1]/tri_count)/(bi_chara[(chara[0][0], chara[0][1])]/uni_count)) for chara in tri_chara.items()))/tri_count

    print(uni_entropy, bi_entropy, tri_entropy)


if __name__ == '__main__':
    path = "./data/"
    print("按字计算信息熵：一元模型   二元模型   三元模型")
    entropy_calculate(path, is_chara=True)
    print("按词计算信息熵：一元模型   二元模型   三元模型")
    entropy_calculate(path, is_chara=False)
