import os



python ='/home/peter/anaconda3/envs/py36/bin/python'

demopy='/home/peter/extra/Workspace/codes/alphapose.torch/demo.py'
py = '/home/peter/extra/Workspace/codes/tiah/tiah_module/VideoResize.py'

inpath = '/home/peter/tmp/lighttrack'
outpath = '/home/peter/tmp/lighttrack/vga'
#inpath = '/home/peter/extra/Workspace/codes/lighttrack/outputdir'


for idx, vv in enumerate(os.listdir(inpath)):
    command ='%s %s --video %s --size vga --output %s --fixed'%(python, py, os.path.join(inpath,vv), outpath)
    print(idx, os.path.join(inpath,vv), outpath)
    os.system(command)
