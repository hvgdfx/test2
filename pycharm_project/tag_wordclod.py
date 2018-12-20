#coding=utf-8

from wordcloud import WordCloud
import matplotlib.pyplot as plt



#wordcloud = WordCloud().generate(text)


# data processing

# def processing1():
#     text1 = open('C:/Users/zhanggx/Desktop/text.txt', encoding='utf-8').readlines()
#     adict = {}
#     for line in text1:
#         tag, weight = line.replace(' ', '').replace('\n', '').split('\t')
#         if len(weight) == 0:
#             adict[tag] = 0
#         else:
#             adict[tag] = float(weight)
#     return adict


def processing2():
    text1 = open('D:/zgx/zgx/pycharm_project/text3.txt', encoding='utf-8').readlines()
    adict = {}
    for line in text1:
        tag_score  = line.replace(' ', '').replace('\n', '').split('\t')
        if len(tag_score) == 2:
            adict[tag_score[0]] = float(tag_score[1])
        else:
            adict[tag_score[0]] = 0
    return adict


# create wordclout
def creatWordCloud(adict):
    font_path = 'D:/Downloads/msyh.ttf'
    wc = WordCloud(max_words=200,
                   mask=None,
                   width = 600,
                   height = 600,
                   max_font_size = 68,
                   min_font_size = 4,
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


