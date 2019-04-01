from multiprocessing import Process, Pipe
#进程间是不能共享信息的，线程可以，所以需要借助pipe或manager来为进程间共享信息和数据
from multiprocessing import Process, Pipe


def f(conn):
    conn.send('he 1')
    conn.send('he 2')
    conn.send('he 3')
    print(conn.recv())
    conn.close()


if __name__ == '__main__':

    parent_conn, child_conn = Pipe()  # 这里不能分步创建，只能这样创建 Pipe() 的对象
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send('chi_recv')
    p.join()


