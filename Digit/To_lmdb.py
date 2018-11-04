< pre


class ="python" name="code" >  # !/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs


set - e

EXAMPLE = My_Files / Build_lmdb  # 生成模型训练数据文件夹，即create_imagenet.sh所在文件夹
DATA = My_Files / Data_Test  # python脚本处理数据路径，即生成的文件列表.txt文件所在文件夹
TOOLS = build / tools  # caffe的工具库，不用更改

TRAIN_DATA_ROOT = < span
style = "font-size:14px;" > / home / sgg / workspace / caffe_learn / scr / Data_Test / < / span >  # 待处理的训练数据
VAL_DATA_ROOT = < span
style = "font-size:14px;" > / home / sgg / workspace / caffe_learn / scr / Data_Test / < / span >  # 待处理的验证数据

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE = true  # 是否需要对图片进行resize
if $RESIZE; then
RESIZE_HEIGHT = 256
RESIZE_WIDTH = 256
else
RESIZE_HEIGHT = 0
RESIZE_WIDTH = 0
fi

if [ ! -d "$TRAIN_DATA_ROOT"]; then
echo
"Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
echo
"Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
"where the ImageNet training data is stored."
exit
1
fi

if [ ! -d "$VAL_DATA_ROOT"]; then
echo
"Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
echo
"Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
"where the ImageNet validation data is stored."
exit
1
fi

echo
"Creating train lmdb..."

rm - rf $EXAMPLE / train_lmdb
rm - rf $EXAMPLE / val_lmdb  # 删除已存在的lmdb格式文件，若在已存在lmdb格式的文件夹下再添加lmdb文件，会出现错误

GLOG_logtostderr = 1 $TOOLS / convert_imageset \
                      - -resize_height =$RESIZE_HEIGHT \
                                         - -resize_width =$RESIZE_WIDTH \
                                                           - -shuffle \
    $TRAIN_DATA_ROOT \
    $DATA / train.txt \
    $EXAMPLE / train_lmdb

echo
"Creating val lmdb..."

GLOG_logtostderr = 1 $TOOLS / convert_imageset \
                      - -resize_height =$RESIZE_HEIGHT \
                                         - -resize_width =$RESIZE_WIDTH \
                                                           - -shuffle \
    $VAL_DATA_ROOT \
    $DATA / val.txt \
    $EXAMPLE / val_lmdb

echo
"Done."