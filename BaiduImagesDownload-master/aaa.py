import logging
from BaiduImagesDownload.crawler import logger

# 设置日志的等级为DEBUG
# 默认为INFO
logger.setLevel(logging.DEBUG)

# 设置输出到文件
file_handler = logging.FileHandler('BaiduImagesDownload.log')
file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')) # 设置输出格式
logger.addHandler(file_handler)
