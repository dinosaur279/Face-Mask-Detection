from bing_image_downloader import downloader
def get_image(key_search , limited , name_folder ,time_out):
	downloader.download(key_search, limit = limited, output_dir = name_folder,adult_filter_off=False, force_replace=False, timeout=time_out)
list_key_search = ["diễn viên hàn quốc","chụp ảnh đeo khẩu trang"]
limited = 10 
name_folder = "datasets"
time_out = 60 
for key_search in list_key_search:
	get_image(key_search, limited , name_folder , time_out)