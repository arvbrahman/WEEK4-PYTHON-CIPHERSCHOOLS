# with open('love_story.txt', 'r', encoding='utf-8') as f:
#      print(f.encoding)
#      data = f.raed()
#      print(data) 


with open('files.txt', 'r') as f:
    data = f.read(100)
    while len(data) > 0:
        print(data)        
    data = f.read(100) 