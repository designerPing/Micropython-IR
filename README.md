# Micropython-IR
调用函数 send_id(out_signal, pin_name) 对外发送信号
out_signal是发送信号的二进制编码， pin_name是IO接口

调用 read_id(pin_name)读取识别到的红外信号，通过微秒级的快速读取数据获得原始数据，对照数字0、1出现的频率加以分析，最终会解析成二进制。
pin_name是IO接口

＊＊更多问题可以微信联系soping10
