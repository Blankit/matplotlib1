1.transform的ToTensor()要加括号  
`transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])#均值，方差`  
>torchvision datasets的输出是 PILImage图像，取值区间是[0, 1].需要将它转换到[-1, 1]，需要取的均值和方差均为0.5

2.最后一个全连接层要加self

- …or create a new repository on the command line  

    echo "# matplotlib" >> README.md  
    git init  
    git add README.md  
    git commit -m "first commit"  
    git remote add origin https://github.com/Blankit/matplotlib1.git  
    git push -u origin master  


- …or push an existing repository from the command line    
    git remote add origin https://github.com/Blankit/matplotlib1.git     
    git push -u origin master  


   
