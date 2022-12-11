print("务必如实回答以下问题，将按照您的个人情况和实际需求提供破解Classin专注学习模式的方法")
a = int(input("您使用什么设备：1电脑   2平板   3手机（输入序号回答）"))
if a == 1:
    b = int(input("您的设备系统类型：1 Windows8及更早   2 Windows10及更晚    3 Mac   4 Linux（输入序号回答）"))
    if b == 1:
        u = int(input("您是否有计算机基础：1有   2没有（输入序号回答）"))
        if u == 2:
            print("建议您使用Turbo Top，具体使用方法如下")
            print("请前往http://www.savardsoftware.com/downloads/ttsetup.exe 下载该软件")
            print("按照指示安装，打开")
            print("查看你的系统托盘，单击Turbo Top")
            print("此时，你可以强制让非教室窗口保持在最上层")
        if u == 1:
            print("建议您使用classin mover，具体使用方法如下")
            print("请前往https://github.com/CarlGao4/ClassIn-Mover  在右侧找到 releases ")
            print("在 latest 版本下面的 assets 中下载zip压缩文件")
            print("解压后找到exe文件并双击打开，随后正常进入教室，专注学习模式已经完全被忽略")
            print("欲获得详细操作方法，请访问https://www.bilibili.com/read/cv20399787")
    if b == 3:
        print("您应当不需要我的帮助")
    if b == 4:
        print("您的系统在家用电脑中不常用，且由于没有设备进行测试，故暂未发现解决方法，请见谅")
    if b == 2:
        c = int(input("您是否有计算机基础：1有   2没有（输入序号回答）"))
        if c == 1:
            print("建议您使用classin mover，具体使用方法如下")
            print("请前往https://github.com/CarlGao4/ClassIn-Mover  在右侧找到 releases ")
            print("在 latest 版本下面的 assets 中下载zip压缩文件")
            print("解压后找到exe文件并双击打开，随后正常进入教室，专注学习模式已经完全被忽略")
            print("欲获得详细操作方法，请访问https://www.bilibili.com/read/cv20399787")
        if c == 2:
            print("建议您使用Windows任务视图，具体使用方法如下")
            print("按下Windows徽标键+Tab或在触控板（如有）三指上划，进入Windows视图")
            print("点击新建桌面，将classin教室窗口拖放至桌面二（假设）")
            print("然后，你可以按下Windows徽标键+Tab或在触控板（如有）四指侧划在多个桌面之间切换")
            print("此时，桌面一（假设）不受专注学习模式影响，且教师不会知道你在多个桌面之间切换")
            print("欲获得详细操作方法，请访问https://www.bilibili.com/read/cv16538990")


if a == 2:
    d = int(input("您的设备系统类型：1 EMUI   2 MagicUI    3 HarmonyOS   4 其他（输入序号回答）"))
    if d == 1 or 2 or 3:
        print("建议您使用电脑模式")
        print("下拉屏幕，点击电脑模式")
        print("在电脑模式中进入教室，尽管使用体验不那么好，但这似乎是目前唯一的办法了")
    if d == 4:
        print("由于没有设备进行测试，故暂未发现解决方法，请见谅")


if a == 3:
    print("由于没有设备进行测试，故暂未发现解决方法，请见谅")


z = input("键入任意值退出")
