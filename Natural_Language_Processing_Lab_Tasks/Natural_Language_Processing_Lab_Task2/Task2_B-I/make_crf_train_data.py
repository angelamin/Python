#!/usr/bin/python
# -*- coding: utf-8 -*-
# make_crf_train_data.py
# 得到CRF++要求的格式的训练文件
# 用法：命令行--python dataprocess.py input_file output_file
import sys
import codecs


# 2 tags for character tagging: B I
def character_4tagging(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output_data.write(word + "\tB\n")
            else:
                output_data.write(word[0] + "\tB\n")
                for w in word[1:len(word) - 1]:
                    output_data.write(w + "\tI\n")
                output_data.write(word[len(word) - 1] + "\tI\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("Usage: python dataprocess.py inputfile outputfile")
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_4tagging(input_file, output_file)
