#  Trích xuất tên bài hát từ đường dẫn. Cho một chuỗi biểu thị đường dẫn đến tệp nhạc, ví dụ: `d:\\music\\muabui.m
def extract_filename(path):
    
    parts = path.split('\\')
    
    filename = parts[-1]
    return filename
def extract_song_name(path):

    filename = extract_filename(path)
    name_parts = filename.split('.')
    song_name = name_parts[0]
    return song_name
path = 'd:\\music\\muabui.mp3'
print(extract_filename(path))  
print(extract_song_name(path))  
