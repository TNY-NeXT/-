from multiprocessing import Process, Manager

def f(d, l, n):
    d['1'] = '2'
    d['name'] = 'yanhuo'
    d[n] = '3'
    l.append(n) # 这步是为了在 子进程中给主进程的列表添加数据，以验证进程间可以共享数据

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() # 这个字典进程间可以共享
        l = manager.list(range(5)) #l = list(range(5)) 是创建列表，用 manager.list(range())创建的列表就可以实现进程间共享数据了
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p_list.append(p)
            p.start()
        for i in p_list:
            i.join()

        print(d)
        print(l)

# 要想实现进程间共享信息或数据，就一定要利用manager来创建字典或列表等存储信息的容器，这样才能实现数据共享。
