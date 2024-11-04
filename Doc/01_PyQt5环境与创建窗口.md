## 通过pip安装PyQt5

- `pip install PyQt5`			安装`PyQt5`
- `pip install PyQt5-tools`	安装`Qt`工具软件
- `pip install PyQt5-stubs`	安装PyQt5语法检测包（可选）



## 第一个PyQt窗口

```python
from PyQt5.QtWidgets import QApplication,QWidget
import sys

# 1.创建应用程序
app = QApplication(sys.argv)

# 2.创建窗口
w = QWidget()

# 3.显示窗口
w.show()

# 4.等待窗口停止
sys.exit(app.exec())
```

