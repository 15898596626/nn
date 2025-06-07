# 快速开始指南

## 运行示例
```python
# src/main.py
import carla

def main():
    # 初始化Carla客户端
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    
    # 在这里添加你的神经网络代理代码
    print("成功连接到Carla服务器！")

if __name__ == "__main__":
    main()