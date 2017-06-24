# -*- coding: utf-8 -*-
# 夏敏
#
#!/usr/bin/env python
# 4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)

# 运行 python make_crf_test_data.py test.utf8 tag_test.utf8

import codecs
import sys

def character_split(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        print line
        for word in line.strip():
            print word
            word = word.strip()
            if word:
                output_data.write(word + "\tB\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "pls use: python make_crf_test_data.py input output"
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_split(input_file, output_file)
