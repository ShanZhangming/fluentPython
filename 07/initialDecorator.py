# def debug(func):
# #     def wrapper():
# #         print("[DEBUG]: enter {}()".format(func.__name__))
# #         return func()
# #     return wrapper
# #
# # def say_hello():
# #     print("hello!")
# #
# # say_hello = debug(say_hello)
# # print(say_hello)
# # say_hello()

# def debug(func):
#     def wrapper(something):
#         print("[DEBUG]:enter {}()".format(func.__name__))
#         return func(something)
#     return wrapper
#
# @debug
# def say_hello(something):
#     print('hello {}'.format(something))
#
# #say_hello = debug(say_hello)
# say_hello('python')

# def debug(func):
#     def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
#         print("[DEBUG]: enter {}()".format(func.__name__))
#         print('Prepare and say...')
#         return func(*args, **kwargs)
#     return wrapper  # 返回
#
# @debug
# def say(something):
#     print("hello {}!".format(something))
# # say = debug(say)
# say('python')

# def logging(level):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             print("[{level}]: enter function {func}()".format(
#                 level=level,
#                 func=func.__name__))
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return wrapper
#
# @logging(level='INFO')
# def say(something):
#     print("say {}!".format(something))
#
# # 如果没有使用@语法，等同于
# # say = logging(level='INFO')(say)
#
# @logging(level='DEBUG')
# def do(something):
#     print("do {}...".format(something))
#
# if __name__ == '__main__':
#     say('hello')
#     do("my work")

def logging(level):
    def A(level2):
        def wrapper(func):
            def inner_wrapper(*args, **kwargs):
                print("[{level}]: enter function {func}()".format(
                    level=level,
                    func=func.__name__))
                return func(*args, **kwargs)
            return inner_wrapper
        return wrapper
    return A

def do(something):
    print("do {}...".format(something))
do = logging('DEBUG')(2)(do)
do('something')