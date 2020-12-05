from BaiduImagesDownload.crawler import Crawler

# rule设置允许的图片格式，默认为('.png', '.jpg')
# timeout为超时时间，默认为60(s)
net, num, urls = Crawler.get_images_url('店铺门头照', 5000)
Crawler.download_images(urls, rule=('.png', '.jpg'), timeout=5)
to_eval()

