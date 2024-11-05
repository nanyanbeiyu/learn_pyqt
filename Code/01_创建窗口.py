from PyQt5.QtWidgets import QApplication,QWidget
import sys

# 1.创建应用程序
app = QApplication(sys.argv)

# 2.创建窗口
w = QWidget()

# 2.1设置窗口标题
w.setWindowTitle("Hello PyQt5")

# 2.2设置窗口大小

w.resize(1280,720)

#2.3 指定窗口的位置
# w.move(400,100)

#2.4 指定窗口位置和大小
w.setGeometry(400,100,1280,720)

# 3.显示窗口
w.show()

# 4.等待窗口停止
sys.exit(app.exec())