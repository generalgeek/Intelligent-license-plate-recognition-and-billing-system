import sys
import cv2
import pygame
import time
import matplotlib.pyplot as plt
import const
import button
import ocrutil
import data_process

# 月收入统计分析界面开关
income_switch = False
cam = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption('智能停车场车牌识别计费系统')
ic_launcher = pygame.image.load('../file/icon.png')
pygame.display.set_icon(ic_launcher)
screen = pygame.display.set_mode(const.size)
screen.fill(const.BG)


def text0(screen: pygame.surface):
    pygame.draw.rect(screen, const.BG, (650, 2, 350, 640))
    # 绘制横线
    pygame.draw.aaline(screen, const.GREEN, (662, 50), (980, 50), 1)
    # 绘制信息矩形框
    pygame.draw.rect(screen, const.GREEN, (650, 350, 342, 85), 1)
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 15)
    # 重新开始按钮
    textstart = xtfont.render('信息：', True, const.GREEN)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 675
    text_rect.centery = 365
    # 绘制内容
    screen.blit(textstart, text_rect)
    ret = data_process.sql_exec("select * from car order by entry_time limit 0,1")
    if len(ret) > 0:
        longcar = ret[0][0]
        # 使用系统字体
        xtfont = pygame.font.SysFont('SimHei', 15)
        # 转换当前时间 2022-04-14 13:00
        localtime = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        # htime = timeutil.DtCalc(cartime,localtime)
        # 重新开始按钮
        textscar = xtfont.render('停车时间最长车辆：' + str(longcar), True, const.RED)
        # texttime = xtfont.render("已停车：" + str(htime) + '小时', True, RED)
        # 获取文字图像位置
        text_rect1 = textscar.get_rect()
        # text_rect2 = texttime.get_rect()
        # 设置文字图像中心点
        text_rect1.centerx = 820
        text_rect1.centery = 320
        # text_rect2.centerx = 820
        # text_rect2.centery = 335
        # 绘制内容
        screen.blit(textscar, text_rect1)
        # screen.blit(texttime, text_rect2)
        pass


def text1(screen: pygame.surface):
    ret = data_process.sql_exec("select total_space,remain_space from parkinglot;")
    total, remain = ret[0][0], ret[0][1]
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 20)
    # 重新开始按钮
    textstart = xtfont.render('共有车位：' + str(total) + '  剩余车位：' + str(remain), True, const.WHITE)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 30
    # 绘制内容
    screen.blit(textstart, text_rect)


def text2(screen: pygame.surface):
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 15)
    # 重新开始按钮
    textstart = xtfont.render('  车号       时间    ', True, const.WHITE)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 70
    # 绘制内容
    screen.blit(textstart, text_rect)
    pass


def text3(screen: pygame.surface):
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 12)
    # 获取文档表信息
    cars = data_process.sql_exec("select * from car;")
    # 页面就绘制10辆车信息
    # 动态绘制y点变量
    n = 0
    # 循环文档信息
    for car in cars:
        n += 1
        # 车辆车号 车辆进入时间
        textstart = xtfont.render(str(car[0]) + '   ' + str(car[1]), True, const.WHITE)
        # 获取文字图像位置
        text_rect = textstart.get_rect()
        # 设置文字图像中心点
        text_rect.centerx = 820
        text_rect.centery = 70 + 20 * n
        # 绘制内容
        screen.blit(textstart, text_rect)
    pass


# 历史信息 满预警信息
def text4(screen, txt1, txt2, txt3):
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 15)
    texttxt1 = xtfont.render(txt1, True, const.GREEN)
    # 获取文字图像位置
    text_rect = texttxt1.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 355 + 20
    # 绘制内容
    screen.blit(texttxt1, text_rect)

    texttxt2 = xtfont.render(txt2, True, const.GREEN)
    # 获取文字图像位置
    text_rect = texttxt2.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 355 + 40
    # 绘制内容
    screen.blit(texttxt2, text_rect)

    texttxt3 = xtfont.render(txt3, True, const.GREEN)
    # 获取文字图像位置
    text_rect = texttxt3.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 355 + 60
    # 绘制内容
    screen.blit(texttxt3, text_rect)
    pass


# 收入统计
def text5(screen):
    # 计算总收入
    current_year = time.localtime().tm_year
    sql = "select annual_income from income where year = " + str(current_year)
    ret = data_process.sql_exec(sql)
    sum_income = ret[0][0]
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 20)
    # 重新开始按钮
    textstart = xtfont.render('共计收入：' + str(int(sum_income)) + '元', True, const.WHITE)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 1200
    text_rect.centery = 30
    # 绘制内容
    screen.blit(textstart, text_rect)
    # 加载图像
    image = pygame.image.load('../file/income.png')
    # 设置图片大小
    image = pygame.transform.scale(image, (390, 430))
    # 绘制月收入图表
    screen.blit(image, (1000, 50))


# 游戏循环帧率设置
clock = pygame.time.Clock()
# 主线程
Running = True
while Running:
    success, img = cam.read()
    cv2.imwrite('../file/test.png', img)
    image = pygame.image.load('../file/test.png')
    image = pygame.transform.scale(image, (640, 480))
    # 绘制视频画面
    screen.blit(image, (2, 2))
    # 背景文字图案
    text0(screen)
    # 停车位信息
    text1(screen)
    # 停车场信息表头
    text2(screen)
    # 停车场车辆信息
    text3(screen)
    # 提示信息
    text4(screen, const.txt1, const.txt2, const.txt3)
    # 创建识别按钮
    button_go = button.Button(screen, (640, 480), 150, 60, const.BLUE, const.WHITE, "识别", 25)
    # 绘制创建的按钮
    button_go.draw_button()
    # 创建分析按钮
    button_go1 = button.Button(screen, (990, 480), 100, 40, const.RED, const.WHITE, "收入统计", 18)
    # 绘制创建的按钮
    button_go1.draw_button()
    # 判断是否开启了收入统计按钮
    if income_switch:
        # 开启时候绘制页面
        text5(screen)
        pass
    else:
        pass
    for event in pygame.event.get():
        # 关闭页面游戏退出
        if event.type == pygame.QUIT:
            # 退出
            pygame.quit()
            # 关闭摄像头
            cam.release()
            sys.exit()
        # 判断点击
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 输出鼠标点击位置
            print(str(event.pos[0]) + ':' + str(event.pos[1]))
            # 判断是否点击了收入统计按钮位置
            # 收入统计按钮
            if 890 <= event.pos[0] <= 990 \
                    and 440 <= event.pos[1] <= 480:
                print('分析统计按钮')
                if income_switch:
                    income_switch = False
                    # 设置窗体大小
                    size = 1000, 484
                    screen = pygame.display.set_mode(size)
                    screen.fill(const.BG)
                else:
                    income_switch = True
                    # 设置窗体大小
                    size = 1400, 484
                    screen = pygame.display.set_mode(size)
                    screen.fill(const.BG)
                    attr = ['1月', '2月', '3月', '4月', '5月',
                            '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                    current_year = time.localtime().tm_year
                    sql = "select * from income where year = " + str(current_year)
                    ret = data_process.sql_exec(sql)
                    shouru = list(ret[0])
                    v1 = shouru[3:]
                    # 设置字体可以显示中文
                    plt.rcParams['font.sans-serif'] = ['SimHei']
                    # 设置生成柱状图图片大小
                    plt.figure(figsize=(3.9, 4.3))
                    # 设置柱状图属性 attr为x轴内容 v1为x轴内容相对的数据
                    plt.bar(attr, v1, 0.5, color="green")
                    # 设置数字标签
                    for a, b in zip(attr, v1):
                        plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=7)
                    # 设置柱状图标题
                    graph_title = str(current_year) + "年度月收入统计"
                    plt.title(graph_title)
                    # 设置y轴范围
                    plt.ylim((0, max(v1) + 50))
                    # 生成图片
                    plt.savefig('../file/income.png')
                pass
            # 判断是否点击了识别按钮位置
            # 识别按钮
            if 492 <= event.pos[0] <= 642 and 422 <= event.pos[1] <= 482:
                print('点击识别')
                try:
                    # 获取车牌
                    carnumber = ocrutil.get_car_number()
                    # 转换当前时间 2018-12-11 16:18
                    localtime = time.strftime('%Y-%m-%d %H:%M', time.localtime())
                    # 获取车牌号列数据
                    ret = data_process.sql_exec("select car_number from car;")
                    carnumber_list = [e[0] for e in ret]
                    # 判断当前识别得车是否为停车场车辆
                    if carnumber in carnumber_list:
                        const.txt1 = '车牌号：' + carnumber
                        # 驶出情况，识别成功后要把驶出时间设置一下
                        s_sql = "update car set departure_time = " + "'" + localtime + "'" + \
                                " where car_number = " + "'" + carnumber + "'" + ';'
                        data_process.sql_exec(s_sql)
                        # 车辆驶出，删除停车表中对应的信息
                        d_sql = "delete from car where car_number = " + "'" + carnumber + "'" + ";"
                        data_process.sql_exec(d_sql)
                        fee_sql = "select fee from record where car_number = " + \
                                  "'" + carnumber + "'" + "order by entry_time desc limit 0,1"
                        fee_ret = data_process.sql_exec(fee_sql)
                        fee = fee_ret[0][0]
                        const.txt2 = '停车费：' + str(fee) + '元'
                        const.txt3 = '出停车场时间：' + localtime
                    else:
                        in_sql = "insert into car values " \
                                 "(" + "'" + carnumber + "'" + ',' + "'" + localtime + "'" + ',' + "null)" + ';'
                        data_process.sql_exec(in_sql)
                        # 有停车位提示信息
                        const.txt1 = '车牌号： ' + carnumber
                        const.txt2 = '有空余车辆，可以进入停车场'
                        const.txt3 = '进停车场时间：' + localtime
                except Exception as e:
                    print("错误原因:", e)
                    continue
                pass
    # 更新界面
    pygame.display.flip()
    # 控制最大帧率为60
    clock.tick(const.FPS)
# 关闭摄像头
cam.release()
