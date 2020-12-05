from BaiduImagesDownload.crawler import Crawler

# original为True代表优先下载原图
net, num, urls = Crawler.get_images_url('商铺门牌',2000, original=True)
Crawler.download_images(urls)
