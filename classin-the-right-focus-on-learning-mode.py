print("务必如实回答以下问题，将按照您的个人情况和实际需求提供抵抗Classin专注学习模式的方法")
a = int(input("您使用什么设备：1电脑   2平板   3手机（输入序号回答）"))
if a == 1:
    b = int(input("您的设备系统类型：1 Windows8及更早   2 Windows10及更晚    3 Mac   4 Linux（输入序号回答）"))
    if b == 1:
        print("请参照https://www.bilibili.com/read/cv16538990?spm_id_from=333.999.0.0中的方法二，使用Windows任务视图")
    if b == 3:
        print("您应当不需要我的帮助")
    if b == 4:
        print("您的系统在家用电脑中不常用，目前尚无解决办法")
    if b == 2:
        c = int(input("您是否有计算机基础：1有   2没有（输入序号回答）"))
        if c == 1:
            print("请参照https://www.bilibili.com/read/cv16538990?spm_id_from=333.999.0.0中的方法二，使用classin mover")
        if c == 2:
            print("请参照https://www.bilibili.com/read/cv16538990?spm_id_from=333.999.0.0中的方法二，使用Windows任务视图")


if a == 2:
    d = int(input("您的设备系统类型：1 EMUI   2 MagicUI    3 HarmonyOS   4 其他（输入序号回答）"))
    if d == 1 or 2 or 3:
        print("请使用电脑模式")
    if d == 4:
        print("暂无解决方法，等待您的探索")


if a == 3:
    print("暂无解决方法，等待您的探索")
z = input("键入任意值退出")
