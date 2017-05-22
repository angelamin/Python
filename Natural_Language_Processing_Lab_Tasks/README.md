

CRF++
Linux版本的安装方法是：
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


下面我讲一下我的思路：

由于Task2根目录下的_CRFPP.so没有引入
所以正常能运行的是文件夹Task2_B-I下的内容，此文件夹下对词语分类只有B I两种

首先我用msr_training.utf8 通过python程序 make_crf_train_data.py转化成训练语料需要的格式，即tag_train_data.utf8,
然后我开始训练模型，得到model 再利用CRF自带的python工具包，对输入文本分词，具体实现是通过python程序 crf_segment.py ,
最后就将msr_test.utf8 分词得到 crf_tag_result.utf8.