import logging
import os.path
import time

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_path = os.path.join(base_path, 'logs')
if not os.path.exists(file_path):
    os.mkdir(file_path)


def load_log():
    # 创建log文件名
    logname = os.path.join(file_path, 'webauto{}.log'.format(time.strftime('%Y-%m-%d')))
    # 创建log记录器logger
    logger = logging.getLogger('log')
    # 设置日志级别level
    logger.setLevel(logging.DEBUG)
    # 创建日志格式器formater
    formater = logging.Formatter('[%(levelname)s][%(filename)s %(lineno)d][%(asctime)s]:[%(message)s]')
    if not logger.handlers:
        # 创建日志处理器filelogger
        filelogger = logging.FileHandler(logname, mode='a', encoding='utf-8')
        # 创建控制台处理器
        console = logging.StreamHandler()
        # 设置日志级别
        console.setLevel(logging.INFO)
        # 设置日志级别
        filelogger.setLevel(logging.INFO)
        # 将日志文件fielogger记录内容同formater格式器进行格式化
        filelogger.setFormatter(formater)
        # 将控制台内容格式化输出
        console.setFormatter(formater)

        logger.addHandler(console)
        logger.addHandler(filelogger)
    return logger


"""logger.setLevel() 用于设置 logger 的最低日志级别。这意味着严重程度低于指定级别的日志消息将被忽略。
例如，如果将级别设置为 logging.DEBUG，那么只会记录严重程度为 
DEBUG、INFO、WARNING、ERROR 或 CRITICAL 的日志消息。 

filelogger.setLevel() 用于设置 filelogger 处理程序的最低日志级别。这意味着严重程度低于指定级别的日志消息将被 
filelogger 处理程序忽略，但它们可能仍然由与 logger 
相关的其他处理程序记录。如果您想将某些消息记录到文件中，但不记录到控制台（或反之于是），则可以使用这种方法。 

在您发布的代码中，filelogger 和 console 处理程序都已将日志记录级别设置为 logging.DEBUG，因此它们将记录 logger 
发出的所有消息，而不管其严重程度。因此，在这种情况下，filelogger.setLevel() 调用是不必要的，可以删除。 
logger = logging.getLogger("log")
logger.setLevel(logging.DEBUG)  # Set the logger's minimum logging level to DEBUG

filelogger = logging.FileHandler(logfile, mode="a", encoding="UTF-8")
filelogger.setLevel(logging.INFO)  # Set the filelogger's minimum logging level to INFO

console = logging.StreamHandler()
console.setLevel(logging.WARNING)  # Set the console's minimum logging level to WARNING

logger.addHandler(filelogger)
logger.addHandler(console)

logger.debug("This is a debug message")  # This message will be logged to the file, but not to the console
logger.info("This is an info message")  # This message will be logged to the file and to the console
logger.warning("This is a warning message")  # This message will be logged to the file and to the console
logger.error("This is an error message")  # This message will be logged to the file and to the console
"""
