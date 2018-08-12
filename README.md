# PyCraft_API
[PyCraft](https://github.com/Egnima/Pycraft.git ) API 입니다.

## 사용법
```python
from PyCraftAPI import API # PyCraftAPI.py 파일과 같은 디렉토리 안에서만 사용 가능합니다.

```

## 예제
```python
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
```