import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import transforms, utils
import matplotlib.pyplot as plt

import models
import SqueezeNet
train_img_data = torchvision.datasets.ImageFolder('data/flower_photos',
                                            transform=transforms.Compose([
                                                transforms.Resize(256),
                                                transforms.CenterCrop(224),
                                                transforms.ToTensor()])
                                            )
train_data_loader = torch.utils.data.DataLoader(train_img_data, batch_size=4,shuffle=True)

# model = models.Net()
model = SqueezeNet.SqueezeNet(num_classes=5)
'定义损失函数及优化方法'
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)  # 注意参数
for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(train_data_loader, 0):
        # get the inputs
        inputs, labels = data
        # print('*'*20)
        # print(inputs.size())

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()

        optimizer.step()#优化器更新权值

        # print statistics
        # print('*'*20)
        # print(" loss type")
        # print(type(running_loss))
        running_loss += loss.item()#item(),将torch数据转成python数据（数据只有一个元素）
        # running_loss += loss

        if i % 10 == 9:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
