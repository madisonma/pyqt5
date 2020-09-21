import configparser, os, socket
def get(section,option):
    rootDir = os.path.split(os.path.realpath(__file__))[0]
    configFilePath = os.path.join(rootDir, 'config.ini')
    """
    根据传入的section获取对应的value
    :param section: ini配置文件中用[]标识的内容
    :return:
    """
    config = configparser.ConfigParser()
    config.read(configFilePath)
    # return config.items(section=section)
    return config.get(section=section, option=option)
def set(section,option,value):
    rootDir = os.path.split(os.path.realpath(__file__))[0]
    configFilePath = os.path.join(rootDir, 'config.ini')
    config = configparser.ConfigParser()
    config.read(configFilePath)
    # 创建一个组：LILY
    # config.add_section("LILY")
    # 给LILY组添加一个属性name=lily
    config.set(section,option,value)
    # 写入 config.ini
    # r:读，r+:读写，w:写，w+:写读，a:追加，a+:追加读写
    # 写读和读写的区别：读写，文件已经存在；写读，创建新的文件
    config.write(open(configFilePath, 'w+'))
    # return config.items(section=section)
def get_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip