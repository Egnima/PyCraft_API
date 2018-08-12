from PyCraftAPI import API

def main():
    api = API()
    for x in range(6):
        for z in range(6):
            api.addBlock((x, -1, -z))
            for y in range(6):
                api.addBlock((x, -2 - y, -z))


if __name__ == '__main__':
    main()