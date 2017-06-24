# CRF++
## Linux版本的安装方法是：
                         i.              解压到某目录下
                        ii.              打开控制台，将当前目录切换到解压目录
                       iii.              依次输入命令：
./configure  
make  
su  
make install  
                            注：需要root权限才能成功安装。

由于这里使用 python 工具包进行训练和测试，需要安装 python 工具包。进入 python 文件夹，运行以下命令安装：  
python setup.py build  
sudo python setup.py install  


## 下面我讲一下我的思路：

由于Task2根目录下的_CRFPP.so没有引入
所以正常能运行的是文件夹Task2_B-I下的内容，此文件夹下对词语分类只有B I两种

> 1)将人工标注好的文件转换为CRF++需要的格式

make_crf_train_data.py  
将msr_training.utf8转化成训练语料需要的格式，即tag_train_data.utf8,
> 2)开始训练模型

crf_learn -f 3 -c 4.0 template tag_train_data.utf8.utf8 model   
得到model    
> 3)从模型出发，有两种方法来进行分词

- a.通过手动处理需要测试的文件   
make_crf_test_data.py     
将需要测试的文件转换为需要的格式  
如下：
```
扬 B
帆 B
远 B
东 B
做 B
与 B  
```
得到划分结果    
crf_test -m model tag_test.utf8 > tag_result.utf8    

  ```
  扬 B   B
  帆 B   E
  远 B   B
  东 B   E
  做 B   S
  与 B   S
  ```

  最后将结果以分词的形式文字展示
make_word_data.py
```
扬帆  远东  做  与  中国  合作  的  先行
 希腊  的  经济  结构  较  特殊  。
 ```

 利用backoff2005的测试脚本来测一下这次分词的效果

- b.利用CRF自带的python工具包     
  crf_segment.py   
最后就将msr_test.utf8 分词得到 crf_tag_result.utf8.
