"""
    @File: Md5modify.py
    @Type: class -> (custom)
    @Description: 自定义的Md5加密方法

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

# 引入math模块，因为要用到sin函数
import math




class Md5modify:
    # 定义常量，用于初始化128位变量，注意字节顺序，文中的A=0x01234567，这里低值存放低字节，即01 23 45 67，所以运算时A=0x67452301，其他类似。
    # 这里用字符串的形势，是为了和hex函数的输出统一，hex(10)输出为'0xA',注意结果为字符串。
    A = '0x45672301'
    B = '0xcdefab89'
    C = '0xba98dcfe'
    D = '0x32105476'
    Ti_count=0
    # 由于类调用方法时默认传入self，在此添加self（猜）
    # 定义每轮中用到的函数。L为循环左移，注意左移之后可能会超过32位，所以要和0xffffffff做与运算，确保结果为32位。
    F = lambda self, x, y, z: ((x & y) | ((~x) & z))
    G = lambda self, x, y, z: ((x & z) | (y & (~z)))
    H = lambda self, x, y, z: (x ^ y ^ z)
    I = lambda self, x, y, z: (y ^ (x | (~z)))
    L = lambda self, x, n: (((x << n) | (x >> (32 - n))) & (0xffffffff))

    # 定义每轮中循环左移的位数，这里用4个元组表示,用元组是因为速度比列表快。
    shi_1 = (7, 12, 17, 22) * 4
    shi_2 = (5, 9, 14, 20) * 4
    shi_3 = (4, 11, 16, 23) * 4
    shi_4 = (6, 10, 15, 21) * 4

    # 定义每轮中用到的M[i]次序。
    m_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    m_2 = (1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12)
    m_3 = (5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2)
    m_4 = (0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9)


    # 定义函数，用来产生常数T[i]，常数有可能超过32位，同样需要&0xffffffff操作。注意返回的是十进制的数。
    def T(self, i):
        result = (int(4294967296 * abs(math.sin(i)))) & 0xffffffff
        return result


    # 定义函数，用来将列表中的元素循环右移。原因是在每轮操作中，先运算A的值，然后是D，C，B，16轮之后右恢复原来顺序，所以只要每次操作第一个元素即可。
    def shift(self, shift_list):
        shift_list = [shift_list[3], shift_list[0], shift_list[1], shift_list[2]]
        return shift_list


    # 定义主要的函数，参数为当做种子的列表，每轮用到的F，G，H，I，生成的M[]，以及循环左移的位数。该函数完成一轮运算。
    def fun(self, fun_list, f, m, shi):
        count = 0

        # T(i)是从1到64循环的。
        while count < 16:
            xx = int(fun_list[0], 16) + f(int(fun_list[1], 16), int(fun_list[2], 16), int(fun_list[3], 16)) + int(m[count], 16) + self.T(self.Ti_count)
            xx = xx & 0xffffffff
            ll = self.L(xx, shi[count])
            fun_list[0] = hex((int(fun_list[1], 16) + ll) & (0xffffffff))[:-1]
            # 最后的[:-1]是为了去除类似'0x12345678L'最后的'L'
            fun_list = self.shift(fun_list)
            count += 1
            self.Ti_count += 1
            # print(fun_list)

        return fun_list


    # 该函数生成每轮需要的M[]，最后的参数是为了当有很多分组时，进行偏移。
    def genM16(self, order, ascii_list, f_offset):
        ii = 0
        m16 = [0] * 16
        f_offset = f_offset * 64
        for i in order:
            i = i * 4
            m16[ii] = '0x' + ''.join((ascii_list[i + f_offset] + ascii_list[i + 1 + f_offset] + ascii_list[
                i + 2 + f_offset] + ascii_list[i + 3 + f_offset]).split('0x'))
            ii += 1
        for c in m16:
            ind = m16.index(c)
            m16[ind] = self.reverse_hex(c)
        return m16


    # 翻转十六进制数的顺序：'0x01234567' => '0x67452301'
    def reverse_hex(self, hex_str):
        hex_str = hex_str[2:]
        hex_str_list = []
        for i in range(0, len(hex_str), 2):
            hex_str_list.append(hex_str[i:i + 2])
        hex_str_list.reverse()
        hex_str_result = '0x' + ''.join(hex_str_list)
        return hex_str_result


    # 显示结果函数，将最后运算的结果列表进行翻转，合并成字符串的操作。
    def show_result(self, f_list):
        result = ''
        f_list1 = [0] * 4
        for i in f_list:
            f_list1[f_list.index(i)] = self.reverse_hex(i)[2:]
            result = result + f_list1[f_list.index(i)]
        return result

    def getMd5(self, string):
        # 程序主循环

        abcd_list = [self.A, self.B, self.C, self.D]
        self.Ti_count = 1

        input_m = string

        # 对每一个输入先添加一个'0x80'，即'10000000'
        ascii_list = list(map(hex, map(ord, input_m)))
        msg_lenth = len(ascii_list) * 8
        ascii_list.append('0x80')

        # 补充0
        while (len(ascii_list) * 8 + 64) % 512 != 0:
            ascii_list.append('0x00')

        # 最后64为存放消息长度，注意长度存放顺序低位在前。
        # 例如，消息为'a'，则长度为'0x0800000000000000'
        msg_lenth_0x = hex(msg_lenth)[2:]
        msg_lenth_0x = '0x' + msg_lenth_0x.rjust(16, '0')
        msg_lenth_0x_big_order = self.reverse_hex(msg_lenth_0x)[2:]
        msg_lenth_0x_list = []
        for i in range(0, len(msg_lenth_0x_big_order), 2):
            msg_lenth_0x_list.append('0x' + msg_lenth_0x_big_order[i:i + 2])
        ascii_list.extend(msg_lenth_0x_list)
        # print("len:>>",len(ascii_list))


        # 对每个分组进行4轮运算
        for i in range(0, int(len(ascii_list) / 64)):
            # 将最初128位种子存放在变量中，
            aa, bb, cc, dd = abcd_list

            # 根据顺序产生每轮M[]列表
            order_1 = self.genM16(self.m_1, ascii_list, i)
            order_2 = self.genM16(self.m_2, ascii_list, i)
            order_3 = self.genM16(self.m_3, ascii_list, i)
            order_4 = self.genM16(self.m_4, ascii_list, i)

            # 主要四轮运算，注意打印结果列表已经被进行过右移操作！
            abcd_list = self.fun(abcd_list, self.F, order_1, self.shi_1)
            # print('--------------------------------------')
            abcd_list = self.fun(abcd_list, self.G, order_2, self.shi_2)
            # print('--------------------------------------')
            abcd_list = self.fun(abcd_list, self.H, order_3, self.shi_3)
            # print('--------------------------------------')
            abcd_list = self.fun(abcd_list, self.I, order_4, self.shi_4)
            # print('--------------------------------------')

            # 将最后输出与最初128位种子相加，注意，最初种子不能直接使用abcd_list[0]等，因为abcd_list已经被改变
            output_a = hex((int(abcd_list[0], 16) + int(aa, 16)) & 0xffffffff)[:-1]
            output_b = hex((int(abcd_list[1], 16) + int(bb, 16)) & 0xffffffff)[:-1]
            output_c = hex((int(abcd_list[2], 16) + int(cc, 16)) & 0xffffffff)[:-1]
            output_d = hex((int(abcd_list[3], 16) + int(dd, 16)) & 0xffffffff)[:-1]

            # 将输出放到列表中，作为下一次128位种子
            abcd_list = [output_a, output_b, output_c, output_d]

            # 将全局变量Ti_count恢复，一遍开始下一个分组的操作。
            self.Ti_count = 1

            # print("{}message{}".format(i, self.show_result(abcd_list)))
        # 最后调用函数，格式化输出
        return self.show_result(abcd_list)


if __name__ == '__main__':
    # getMd5()将指定字符变成Md5
    print(Md5modify().getMd5("Aa12345678"))
