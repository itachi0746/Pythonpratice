class Singleton:
    """使用字典实现单例模式"""
    _singletons = {}

    def __new__(cls):  # cls是一个类对象
        if not cls._singletons.get(cls):  # 如果还没任何实例
            cls._singletons[cls] = object.__new__(cls)  # 创建实例
        return cls._singletons[cls]  # 返回


class Singleton2(object):
    """使用__new__方法"""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton2, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


def singleton3(cls, *args, **kwargs):
    """装饰器版本"""
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton3
class Singleton4:
    pass


if __name__ == '__main__':
    a = Singleton4()
    b = Singleton4()
    print(id(a), id(b))

