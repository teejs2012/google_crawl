from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"Car",
             # 'prefix_keywords':'japanese,chinese,singapore,korean',
             # 'prefix_keywords':'korean',
             "limit":5000,
             "print_urls":False,
             "output_directory":"./Images",
#              "color_type":"full-color"
#              "type":"face",
             "size":">640*480",
             "color_type":"full-color",
             "chromedriver":"./chromedriver.exe",
            } 
response.download(arguments)