#coding=utf-8

from wordcloud import WordCloud
import matplotlib.pyplot as plt



#wordcloud = WordCloud().generate(text)


# data processing

# def processing():
#     text = open('D:/zgx/zgx/pycharm_project/text3.txt').read()
#     adict = {}
#     for i in text.strip('').replace('\n', '').split(' '):
#         if i not in adict.keys():
#             adict[i] = 1
#         else:
#             adict[i] += 1
#     return adict


def processing2():
    text1 = open('C:/Users/zhanggx/Desktop/text.txt', encoding='utf-8').readlines()
    adict = {}
    for line in text1:
        tag, weight = line.replace(' ', '').replace('\n', '').split('\t')
        if len(weight) == 0:
            adict[tag] = 0
        else:
            adict[tag] = float(weight)
    return adict

# create wordclout
def creatWordCloud(adict):
    font_path = 'D:/Downloads/msyh.ttf'
    wc = WordCloud(max_words=200,
                   mask=None,
                   font_path=font_path,
                   )
    wc.generate_from_frequencies(adict)
    return wc

# plt
def plotWC(wc):
    plt.figure()
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    #plt.savefig('D:/zgx/zgx/pycharm_project/text.jpg')
    wc.to_file('D:/zgx/zgx/pycharm_project/text.jpg')



if __name__ == '__main__':
    adict = processing2()
    wc = creatWordCloud(adict)
    plotWC(wc)
    print(adict)





#
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
#
#
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.savefig('D:/zgx/zgx/pycharm_project/text.jpg')
#


#print(sort_by_value(adict))


