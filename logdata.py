import codecs

def get_webinfo(path):
    web_info = {}
    config = open(path)
    for line in config:
        result = [ele.strip() for ele in line.split('=')]
        web_info.update(dict[result])
    return web_info

if __name__ == '__main__':
    info = get_webinfo('webinfo.txt')
    for key in info:
        print(key,info[key])