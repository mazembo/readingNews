import os



def all(path):
    filenames = next(os.walk(path))[2]
    return filenames
def allHtml(path):
    filenames = all(path)
    filenames_html = [f for f in filenames if f.endswith(".html")]
    return filenames_html
def allImages(path):
    filenames = all(path)
    filenames_images = [f for f in filenames if f.endswith((".jpg", ".jpeg", ".gif", "png"))]
    return filenames_images
def allYaml(path):
    filenames = all(path)
    filenames_yaml = [f for f in filenames if f.endswith((".yml", ".yaml"))]
    return filenames_yaml
def allVideos(path):
    filenames = all(path)
    filenames_videos = [f for f in filenames if f.endswith(".mp4")]
    return filenames_videos
def allHtmlByDate(path, date):
    filenames = all(path)
    filenames_html = [f for f in filenames if f.endswith(".html")]
    filenames_html_date = [f for f in filenames_html if f.startswith(date)]
    return filenames_html_date
def allImagesByDate(path, date):
    filenames = all(path)
    filenames_images = [f for f in filenames if f.endswith((".jpg", ".jpeg", ".gif", "png"))]
    filenames_images_date = [f for f in filenames_images if f.startswith(date)]
    return filenames_images_date
def allYamlByDate(path, date):
    filenames = all(path)
    filenames_yaml = [f for f in filenames if f.endswith((".yml", ".yaml"))]
    filenames_yaml_date = [f for f in filenames_yaml if f.startswith(date)]
    return filenames_yaml_date
def allVideosByDate(path, date):
    filenames = all(path)
    filenames_videos = [f for f in filenames if f.endswith(".mp4")]
    filenames_videos_date = [f for f in filenames_videos if f.startswith(date)]
    return filenames_videos_date
def allHtmlByMonth(path, month):
    filenames = all(path)
    filenames_html = [f for f in filenames if f.endswith(".html")]
    filenames_html_month = [f for f in filenames_html if f.startswith(month)]
    return filenames_html_month
def allImagesByMonth(path, month):
    filenames = all(path)
    filenames_images = [f for f in filenames if f.endswith((".jpg", ".jpeg", ".gif", "png"))]
    filenames_images_month = [f for f in filenames_images if f.startswith(month)]
    return filenames_images_month
def allYamlByMonth(path, month):
    filenames = all(path)
    filenames_yaml = [f for f in filenames if f.endswith((".yml", ".yaml"))]
    filenames_yaml_month = [f for f in filenames_yaml if f.startswith(month)]
    return filenames_yaml_month
def allVideosByMonth(path, month):
    filenames = all(path)
    filenames_videos = [f for f in filenames if f.endswith(".mp4")]
    filenames_videos_month = [f for f in filenames_videos if f.startswith(month)]
    return filenames_videos_month
def allHtmlByYear(path, year):
    filenames = all(path)
    filenames_html = [f for f in filenames if f.endswith(".html")]
    filenames_html_year = [f for f in filenames_html if f.startswith(year)]
    return filenames_html_year
def allImagesbyYear(path, year):
    filenames = all(path)
    filenames_images = [f for f in filenames if f.endswith((".jpg", ".jpeg", ".gif", "png"))]
    filenames_images_year = [f for f in filenames_images if f.startswith(year)]
    return filenames_images_year

def allYamlByYear(path, year):
    filenames = all(path)
    filenames_yaml = [f for f in filenames if f.endswith((".yml", ".yaml"))]
    filenames_yaml_year = [f for f in filenames_yaml if f.startswith(year)]
    return filenames_yaml_year
def allVideosByYear(path, year):
    filenames = all(path)
    filenames_videos = [f for f in filenames if f.endswith(".mp4")]
    filenames_videos_year = [f for f in filenames_videos if f.startswith(year)]
    return filenames_videos_year
