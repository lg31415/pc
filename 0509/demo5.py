from lxml import etree

def main():
    f = open("1.html",'r')

    result = etree.HTML(f.read())

    print(result)
    result = result.xpath("//a/text()")
    for i in result:
        print(i)

if __name__ == '__main__':
    main()