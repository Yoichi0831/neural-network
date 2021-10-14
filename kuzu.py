# kuzu.py


from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F

class NetLin(nn.Module):
    # linear function followed by log_softmax
    def __init__(self， input):
        super(NetLin, self).__init__()
        # INSERT CODE HERE
        self.hidden = torch.nn.Linear(input)

    def forward(self, input):
        output = F.log_softmax(self.hidden(input))
        return output

class NetFull(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFull, self).__init__()
        # INSERT CODE HERE

    def forward(self, x):
        return 0 # CHANGE CODE HERE

class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax
    def __init__(self):
        super(NetConv, self).__init__()
        self.conv1 = nn.sequential( # (1,28,28)
            nn.conv2d(
                in_channels=1,      # 输入图片的维度
                out_channels=16,     # 输出的维度
                kernel_size=5,      # filter的大小
                stride=1,           # 步伐的大小
                padding=2           # if stride = n, padding = (kernel-n)/2
            )                       # -> (16,28,28)
            nn.ReLU()               # -> (16,28,28)
            nn.MaxPool2d(kernel_size=2), # -> (16,14,14)
        )
        self.out = nn.Linear(16 * 14 * 14, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output
