#原神抽卡模拟器

#导入随机模块
import random as r

#变量初始化
choude = 0
qian_zong = 0
qian_6 = 1
qian_30 = 1
qian_98 = 1
qian_198 = 1
qian_328 = 1
qian_648 = 1
x5_geshu = 0
x4_geshu = 0
x3_geshu = 0
g5_changzhu_jia = 1
g4_changzhu_jia = 1
c5_changzhu = 0
c4_changzhu = 0
g5_wuqi_jia = 1
g4_wuqi_jia = 1
c5_wuqi = 0
c4_wuqi = 0
g5_up_jia = 1
g4_up_jia = 1
c5_up = 0
c4_up = 0
x5_wai = r.randint(0, 1)
x4_wai = r.randint(0, 1)
x4_wai_wuqi = r.randint(0, 1)
x5_wai_geshu = 0
x5_dinggui = 0
chenhui_wuzhu = 0
chenhui_shiluo = 0
shiluo_fenqui = 0
shiluo_lanqui = 0
dinggui_shangci = -1
x5_tongji = []

#卡池数据
x5_changzhu = ["迪卢克", "七七", "刻晴", "琴", "莫娜", "提纳里", "迪希雅", "天空之翼",
               "天空之傲", "天空之卷", "天空之脊", "天空之刃", "风鹰剑", "狼的末路",
               "喵原典", "和璞鸢", "阿莫斯之弓"]
x5_changzhu_shuliang = len(x5_changzhu)

x4_changzhu = ["凯亚", "安柏", "丽莎", "砂糖", "珐露珊", "早柚", "凝光", "迪奥娜",
               "五郎", "诺艾尔", "云堇", "北斗", "菲谢尔", "雷泽", "九岐忍", "多莉",
               "九条裟罗", "瑶瑶", "柯莱", "卡维", "琦良良", "行秋", "米卡", "重云",
               "坎蒂丝", "香菱", "托马", "烟绯", "辛焱", "班尼特", "罗莎莉亚",
               "莱依拉", "芭芭拉", "鹿野院平藏", "琳妮特",
               "匣里龙吟", "笛剑", "西风剑", "祭礼剑", "西风大剑", "雨裁", "钟剑",
               "祭礼大剑", "绝弦", "祭礼弓", "弓藏", "西风猎弓", "匣里灭辰",
               "西风长枪", "西风秘典", "流浪乐章", "祭礼残章", "昭心"]
x4_changzhu_shuliang = len(x4_changzhu)

x3_changzhu = ["冷刃", "黑缨枪", "白缨枪", "翡玉法球", "飞天大御剑", "暗铁剑", "旅行剑",
               "钢轮弓", "吃鱼虎刀", "沾染龙血的剑", "以理服人", "异世界行记",
               "甲级宝钰"]
x3_changzhu_shuliang = len(x3_changzhu)

#获取UP池信息
x5_up_up1 = input("输入本期角色池1 5星up(回车设为默认):")
if x5_up_up1 == '':
    x5_up_up1 = "up1"

x5_up_up2 = input("输入本期角色池2 5星up(回车设为默认):")
if x5_up_up2 == '':
    x5_up_up2 = "up2"

x4_up_up1 = input("输入本期角色池 4星up(回车设为默认):")
if x4_up_up1 == '':
    x4_up_up1 = "up1"

x4_up_up2 = input("输入本期角色池 4星up(回车设为默认):")
if x4_up_up2 == '':
    x4_up_up2 = "up2"

x4_up_up3 = input("输入本期角色池 4星up(回车设为默认):")
if x4_up_up3 == '':
    x4_up_up3 = "up3"

x5_wuqi_up1 = input("输入本期武器池 5星up1(回车设为默认):")
if x5_wuqi_up1 == '':
    x5_wuqi_up1 = "up1"

x5_wuqi_up2 = input("输入本期武器池 5星up2(回车设为默认):")
if x5_wuqi_up2 == '':
    x5_wuqi_up2 = "up2"

x4_wuqi_up1 = input("输入本期武器池 4星up(回车设为默认):")
if x4_wuqi_up1 == '':
    x4_wuqi_up1 = "up1"

x4_wuqi_up2 = input("输入本期武器池 4星up(回车设为默认):")
if x4_wuqi_up2 == '':
    x4_wuqi_up2 = "up2"

x4_wuqi_up3 = input("输入本期武器池 4星up(回车设为默认):")
if x4_wuqi_up3 == '':
    x4_wuqi_up3 = "up3"

x4_wuqi_up4 = input("输入本期武器池 4星up(回车设为默认):")
if x4_wuqi_up4 == '':
    x4_wuqi_up4 = "up4"

x4_wuqi_up5 = input("输入本期武器池 4星up(回车设为默认):")
if x4_wuqi_up5 == '':
    x4_wuqi_up5 = "up5"

x5_up = [x5_up_up1, x5_up_up2]  # 2个5星UP角色
x4_up = [x4_up_up1, x4_up_up2, x4_up_up3]  # 3个4星UP角色
x5_wuqi = [x5_wuqi_up1, x5_wuqi_up2]  # 2个5星UP武器
x4_wuqi = [x4_wuqi_up1, x4_wuqi_up2, x4_wuqi_up3, x4_wuqi_up4, x4_wuqi_up5]  # 5个4星UP武器

#获取玩家资源
yuanshi = input("输入你的原石数量:")
while yuanshi == '':
    yuanshi = input("输入原石数量:")
yuanshi = int(yuanshi)
while yuanshi < 0:  # 判断非负数
    yuanshi = int(input("请输入非负数:"))

lanqui = int(input("输入你的相遇之源数量:"))
while lanqui < 0:  # 判断非负数
    lanqui = int(input("请输入非负数:"))

fenqui = int(input("输入你的纠缠之源数量:"))
while fenqui < 0:  # 判断非负数
    fenqui = int(input("请输入非负数:"))

#主循环
while True:
    print(f"输入(1:抽{x5_up_up1}, 2:抽{x5_up_up2}, 3:抽武器池, 4:抽常驻池, 5:商城, 6:查询数值, 7:退出):", end='')
    caidan = input()  # 选择
    
    # 处理非数字输入
    if not caidan.isdigit():
        print("请输入数字选项")
        continue
    
    caidan = int(caidan)
    
    if caidan in [1, 2]:  # 抽up池
        # 计算可抽次数
        max_choushu = fenqui + yuanshi // 160
        if max_choushu <= 0:
            print("不够一抽")
            continue
        
        choushu = int(input("抽几发:"))  # 输入抽数
        while choushu < 0:
            choushu = int(input("请输入非负数:"))
        
        # 调整实际抽数
        if choushu > max_choushu:
            print(f"资源不足，只能抽{max_choushu}发")
            choushu = max_choushu
        
        # 扣除资源
        if fenqui >= choushu:
            fenqui -= choushu
        else:
            remaining = choushu - fenqui
            fenqui = 0
            yuanshi -= remaining * 160
        
        choude += choushu  # 计数
        
        for i in range(choushu):  # 开始抽
            chou_345 = r.randint(1, 1000)
            
            # 保底机制
            if g5_up_jia > 73:  # 五星到73时每抽概率加6%
                c5_up += 60
            if g4_up_jia > 8:  # 四星到8时每抽概率加51%
                c4_up += 510
            
            if chou_345 <= 6 + c5_up:  # 五星概率0.6%
                if x5_wai == 0:  # 歪
                    chou_ing = r.randint(0, x5_changzhu_shuliang - 1)
                    print(f"  ⭐⭐⭐⭐⭐ {x5_changzhu[chou_ing]} ({g5_up_jia}) (歪)")
                    x5_wai = 1
                    x5_wai_geshu += 1
                else:  # 没歪
                    print(f"  ⭐⭐⭐⭐⭐ {x5_up[caidan - 1]} ({g5_up_jia}) ⭐⭐⭐⭐⭐")
                    x5_wai = r.randint(0, 1)
                
                x5_tongji.append(g5_up_jia)
                chenhui_wuzhu += 10  # 5星给10星辉
                x5_geshu += 1
                g4_up_jia = 1
                g5_up_jia = 1
                c5_up = 0
            
            elif 6 + c5_up < chou_345 <= 57 + c5_up + c4_up:  # 四星概率5.1%
                if x4_wai == 0:  # 歪
                    chou_ing = r.randint(0, x4_changzhu_shuliang - 1)
                    print(f"  ⭐⭐⭐⭐ {x4_changzhu[chou_ing]}")
                    x4_wai = 1
                else:  # 没歪
                    chou_ing = r.randint(0, 2)
                    print(f"  ⭐⭐⭐⭐ {x4_up[chou_ing]}")
                    x4_wai = r.randint(0, 1)
                
                chenhui_wuzhu += 2  # 4星给2星辉
                x4_geshu += 1
                g4_up_jia = 1
                g5_up_jia += 1
                c4_up = 0
            
            else:  # 三星
                chou_ing = r.randint(0, x3_changzhu_shuliang - 1)
                print(f"  ⭐⭐⭐ {x3_changzhu[chou_ing]}")
                x3_geshu += 1
                g4_up_jia += 1
                g5_up_jia += 1
                chenhui_shiluo += 15  # 3星给15星尘
        
        print(f"剩余{yuanshi}个原石, {fenqui}个纠缠之源, 一共{yuanshi // 160 + fenqui}抽")
    
    elif caidan == 3:  # 武器池
        print(f"选择定轨(1:{x5_wuqi_up1}, 2:{x5_wuqi_up2}, 3:不定轨, 4:上次选择的):", end='')
        dinggui_input = input()
        
        # 处理输入
        if dinggui_input == '4' and dinggui_shangci == -1:
            print("你没有选择过")
            dinggui = int(input("重新选择定轨(1:up1, 2:up2, 3:不定轨):"))
        elif dinggui_input == '4' and dinggui_shangci != -1:
            dinggui = dinggui_shangci
        else:
            dinggui = int(dinggui_input)
        
        while dinggui < 1 or dinggui > 4:
            dinggui = int(input("请在范围内输入(1-4):"))
        
        # 处理定轨更换
        if dinggui_shangci != -1 and dinggui_shangci != dinggui and x5_dinggui > 0:
            quiren = int(input("确定换定轨吗,命定值会清零(输入1确定,其他数字取消):"))
            if quiren == 1:
                x5_dinggui = 0
            else:
                continue
        
        # 计算可抽次数
        max_choushu = fenqui + yuanshi // 160
        if max_choushu <= 0:
            print("不够一抽")
            continue
        
        choushu = int(input("抽几发:"))  # 输入抽数
        while choushu < 0:
            choushu = int(input("请输入非负数:"))
        
        # 调整实际抽数
        if choushu > max_choushu:
            print(f"资源不足，只能抽{max_choushu}发")
            choushu = max_choushu
        
        # 扣除资源
        if fenqui >= choushu:
            fenqui -= choushu
        else:
            remaining = choushu - fenqui
            fenqui = 0
            yuanshi -= remaining * 160
        
        choude += choushu  # 计数
        
        for i in range(choushu):  # 开始抽
            chou_345 = r.randint(1, 1000)
            
            # 保底机制
            if 62 <= g5_wuqi_jia <= 72:  # 五星到63时每抽概率加7%
                c5_wuqi += 70
            elif g5_wuqi_jia >= 73:  # 五星到73时每抽概率加3.5%
                c5_wuqi += 35
            
            if g4_wuqi_jia == 7:  # 四星到8时概率6%+60%
                c4_wuqi += 600
            elif g4_wuqi_jia == 8:  # 四星到9时概率6%+90%
                c4_wuqi += 900
            elif g4_wuqi_jia >= 9:  # 四星10时概率6%+94%
                c4_wuqi += 940
            
            if chou_345 <= 7 + c5_wuqi:  # 五星概率0.7%
                if x5_dinggui == 0 or dinggui == 3:  # 定轨0,未定轨
                    dinggui_chou = r.randint(1, 3)
                    if dinggui_chou == 1:  # 歪常驻
                        chou_ing = r.randint(0, x5_changzhu_shuliang - 1)
                        print(f"  ⭐⭐⭐⭐⭐ {x5_changzhu[chou_ing]} ({g5_wuqi_jia}) (歪)")
                        x5_wai_geshu += 1
                        x5_dinggui = min(x5_dinggui + 1, 2)
                    elif dinggui_chou == 2:  # 歪另一把UP武器
                        other_up = 1 if dinggui == 2 else 0
                        print(f"  ⭐⭐⭐⭐⭐ {x5_wuqi[other_up]} ({g5_wuqi_jia}) (歪)")
                        x5_wai_geshu += 1
                        x5_dinggui = min(x5_dinggui + 1, 2)
                    else:  # 抽中定轨武器
                        print(f"  ⭐⭐⭐⭐⭐ {x5_wuqi[dinggui-1]} ({g5_wuqi_jia}) ⭐⭐⭐⭐⭐")
                        x5_dinggui = 0
                
                elif x5_dinggui == 1:  # 定轨1
                    if r.randint(0, 1) == 0:  # 歪另一把UP武器
                        other_up = 1 if dinggui == 1 else 0
                        print(f"  ⭐⭐⭐⭐⭐ {x5_wuqi[other_up]} ({g5_wuqi_jia}) (歪)")
                        x5_wai_geshu += 1
                        x5_dinggui = 2
                    else:  # 抽中定轨武器
                        print(f"  ⭐⭐⭐⭐⭐ {x5_wuqi[dinggui-1]} ({g5_wuqi_jia}) ⭐⭐⭐⭐⭐")
                        x5_dinggui = 0
                
                elif x5_dinggui == 2:  # 定轨2
                    print(f"  ⭐⭐⭐⭐⭐ {x5_wuqi[dinggui-1]} ({g5_wuqi_jia}) ⭐⭐⭐⭐⭐")
                    x5_dinggui = 0
                
                x5_tongji.append(g5_wuqi_jia)
                x5_geshu += 1
                g5_wuqi_jia = 1
                g4_wuqi_jia += 1
                c5_wuqi = 0
                chenhui_wuzhu += 10
            
            elif 7 + c5_wuqi < chou_345 <= 66 + c5_wuqi + c4_wuqi:  # 四星概率6%
                if x4_wai_wuqi == 0:  # 歪
                    chou_ing = r.randint(0, x4_changzhu_shuliang - 1)
                    print(f"  ⭐⭐⭐⭐ {x4_changzhu[chou_ing]}")
                    x4_geshu += 1
                    x4_wai_wuqi = 1
                else:  # 没歪
                    chou_ing = r.randint(0, 4)
                    print(f"  ⭐⭐⭐⭐ {x4_wuqi[chou_ing]}")
                    x4_geshu += 1
                    x4_wai_wuqi = r.randint(0, 1)
                
                g4_wuqi_jia = 1
                g5_wuqi_jia += 1
                c4_wuqi = 0
                chenhui_wuzhu += 2
            
            else:  # 三星
                chou_ing = r.randint(0, x3_changzhu_shuliang - 1)
                print(f"  ⭐⭐⭐ {x3_changzhu[chou_ing]}")
                x3_geshu += 1
                g4_wuqi_jia += 1
                g5_wuqi_jia += 1
                chenhui_shiluo += 15
        
        dinggui_shangci = dinggui
        if dinggui != 3:
            print(f"现在命定值是{x5_dinggui}")
        print(f"剩余{yuanshi}个原石, {fenqui}个纠缠之源, 一共{yuanshi // 160 + fenqui}抽")
    
    elif caidan == 4:  # 常驻池
        # 计算可抽次数
        max_choushu = lanqui + yuanshi // 160
        if max_choushu <= 0:
            print("不够一抽")
            continue
        
        choushu = int(input("抽几发:"))
        while choushu < 0:
            choushu = int(input("请输入非负数:"))
        
        # 调整实际抽数
        if choushu > max_choushu:
            print(f"资源不足，只能抽{max_choushu}发")
            choushu = max_choushu
        
        # 扣除资源
        if lanqui >= choushu:
            lanqui -= choushu
        else:
            remaining = choushu - lanqui
            lanqui = 0
            yuanshi -= remaining * 160
        
        choude += choushu
        
        for i in range(choushu):
            chou_345 = r.randint(1, 1000)
            
            # 保底机制
            if g5_changzhu_jia > 73:
                c5_changzhu += 60
            if g4_changzhu_jia > 8:
                c4_changzhu += 510
            
            if chou_345 <= 6 + c5_changzhu:  # 五星
                chou_ing = r.randint(0, x5_changzhu_shuliang - 1)
                print(f"  ⭐⭐⭐⭐⭐ {x5_changzhu[chou_ing]} ({g5_changzhu_jia}) ⭐⭐⭐⭐⭐")
                x5_tongji.append(g5_changzhu_jia)
                x5_geshu += 1
                g5_changzhu_jia = 1
                g4_changzhu_jia += 1
                c5_changzhu = 0
                chenhui_wuzhu += 10
            
            elif 6 + c5_changzhu < chou_345 <= 57 + c5_changzhu + c4_changzhu:  # 四星
                chou_ing = r.randint(0, x4_changzhu_shuliang - 1)
                print(f"  ⭐⭐⭐⭐ {x4_changzhu[chou_ing]}")
                x4_geshu += 1
                g4_changzhu_jia = 1
                g5_changzhu_jia += 1
                c4_changzhu = 0
                chenhui_wuzhu += 2
            
            else:  # 三星
                chou_ing = r.randint(0, x3_changzhu_shuliang - 1)
                print(f"  ⭐⭐⭐ {x3_changzhu[chou_ing]}")
                x3_geshu += 1
                g4_changzhu_jia += 1
                g5_changzhu_jia += 1
                chenhui_shiluo += 15
        
        print(f"剩余{yuanshi}个原石, {lanqui}个相遇之源, 一共{yuanshi // 160 + lanqui}抽")
    
    elif caidan == 5:  # 商城
        while True:
            print("输入(1:换无主的星辉, 2:换无主的星尘, 3:充值, 4:退出):", end='')
            shangcheng = input()
            
            if not shangcheng.isdigit():
                print("请输入数字选项")
                continue
                
            shangcheng = int(shangcheng)
            
            if shangcheng == 1:  # 换星辉
                if chenhui_wuzhu < 5:
                    print(f"无主的星辉不够，只有{chenhui_wuzhu}个")
                else:
                    print(f"你有{chenhui_wuzhu}个无主的星辉")
                    lanfen = int(input("换什么(1:换纠缠之源, 2:换相遇之源):"))
                    
                    if lanfen == 1:  # 换纠缠之源
                        max_exchange = chenhui_wuzhu // 5
                        huan = int(input(f"换几个(最多{max_exchange}个):"))
                        if huan > max_exchange:
                            huan = max_exchange
                            print(f"调整为{huan}个")
                        fenqui += huan
                        chenhui_wuzhu -= huan * 5
                        print(f"成功兑换{huan}个纠缠之源，剩余{chenhui_wuzhu}个星辉")
                    
                    elif lanfen == 2:  # 换相遇之源
                        max_exchange = chenhui_wuzhu // 5
                        huan = int(input(f"换几个(最多{max_exchange}个):"))
                        if huan > max_exchange:
                            huan = max_exchange
                            print(f"调整为{huan}个")
                        lanqui += huan
                        chenhui_wuzhu -= huan * 5
                        print(f"成功兑换{huan}个相遇之源，剩余{chenhui_wuzhu}个星辉")
                    
                    else:
                        print("无效选择")
            
            elif shangcheng == 2:  # 换星尘
                if chenhui_shiluo < 75:
                    print(f"无主的星尘不够，只有{chenhui_shiluo}个")
                else:
                    print(f"你有{chenhui_shiluo}个无主的星尘")
                    lanfen = int(input("换什么(1:换纠缠之源, 2:换相遇之源):"))
                    
                    if lanfen == 1:  # 换纠缠之源
                        max_exchange = min(chenhui_shiluo // 75, 5 - shiluo_fenqui)
                        if max_exchange <= 0:
                            print("本月已兑换上限")
                        else:
                            huan = int(input(f"换几个(本月还能换{max_exchange}个):"))
                            if huan > max_exchange:
                                huan = max_exchange
                                print(f"调整为{huan}个")
                            fenqui += huan
                            chenhui_shiluo -= huan * 75
                            shiluo_fenqui += huan
                            print(f"成功兑换{huan}个纠缠之源，剩余{chenhui_shiluo}个星尘")
                    
                    elif lanfen == 2:  # 换相遇之源
                        max_exchange = min(chenhui_shiluo // 75, 5 - shiluo_lanqui)
                        if max_exchange <= 0:
                            print("本月已兑换上限")
                        else:
                            huan = int(input(f"换几个(本月还能换{max_exchange}个):"))
                            if huan > max_exchange:
                                huan = max_exchange
                                print(f"调整为{huan}个")
                            lanqui += huan
                            chenhui_shiluo -= huan * 75
                            shiluo_lanqui += huan
                            print(f"成功兑换{huan}个相遇之源，剩余{chenhui_shiluo}个星尘")
                    
                    else:
                        print("无效选择")
            
            elif shangcheng == 3:  # 充值
                print("充值选项: 0(取消), 6, 30, 98, 198, 328, 648")
                qian = int(input("充几元:"))
                
                if qian == 0:
                    pass
                elif qian == 6:
                    if qian_6 == 1:
                        print("首次双倍!")
                        yuanshi += qian * 20
                        qian_6 = 0
                    else:
                        yuanshi += qian * 10
                elif qian == 30:
                    if qian_30 == 1:
                        print("首次双倍!")
                        yuanshi += qian * 20
                        qian_30 = 0
                    else:
                        print("赠送30原石")
                        yuanshi += qian * 10 + 30
                elif qian == 98:
                    if qian_98 == 1:
                        print("首次双倍!")
                        yuanshi += qian * 20
                        qian_98 = 0
                    else:
                        print("赠送110原石")
                        yuanshi += qian * 10 + 110
                elif qian == 198:
                    if qian_198 == 1:
                        print("首次双倍!")
                        yuanshi += qian * 20
                        qian_198 = 0
                    else:
                        print("赠送260原石")
                        yuanshi += qian * 10 + 260
                elif qian == 328:
                    if qian_328 == 1:
                        print("首次双倍!")
                        yuanshi += qian * 20
                        qian_328 = 0
                    else:
                        print("赠送600原石")
                        yuanshi += qian * 10 + 600
                elif qian == 648:
                    if qian_648 == 1:
                        print("首次双倍!")
                        yuanshi += qian * 20
                        qian_648 = 0
                    else:
                        print("赠送1600原石")
                        yuanshi += qian * 10 + 1600
                else:
                    print("无效金额")
                    continue
                
                qian_zong += qian
                print(f"现有{yuanshi}原石")
            
            elif shangcheng == 4:  # 退出商城
                break
            
            else:
                print("无效选项")
    
    elif caidan == 6:  # 查询数值
        print("\n===== 玩家状态 =====")
        print(f"剩余原石: {yuanshi}")
        print(f"剩余纠缠之源: {fenqui}")
        print(f"剩余相遇之源: {lanqui}")
        print(f"剩余无主的星辉: {chenhui_wuzhu}")
        print(f"剩余无主的星尘: {chenhui_shiluo}")
        print(f"武器池命定值: {x5_dinggui}")
        
        print("\n===== 统计信息 =====")
        print(f"总抽数: {choude}")
        print(f"总充值: {qian_zong}元")
        print(f"五星数量: {x5_geshu}")
        print(f"四星数量: {x4_geshu}")
        print(f"三星数量: {x3_geshu}")
        print(f"歪的次数: {x5_wai_geshu}")
        
        if x5_tongji:
            avg = sum(x5_tongji) / len(x5_tongji)
            print(f"平均出金抽数: {avg:.2f}")
        else:
            print("尚未抽到五星")
        
        print("===================\n")
    
    elif caidan == 7:  # 退出
        break
    
    else:
        print("无效选项")

#结束游戏
print("\n游戏结束")
print(f"总抽数: {choude}抽")
print(f"总充值: {qian_zong}元")
print(f"五星数量: {x5_geshu}")
print(f"四星数量: {x4_geshu}")
print(f"三星数量: {x3_geshu}")
print(f"歪的次数: {x5_wai_geshu}")

if x5_tongji:
    avg = sum(x5_tongji) / len(x5_tongji)
    print(f"平均出金抽数: {avg:.2f}")
else:
    print("未出金")
