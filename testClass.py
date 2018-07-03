from threading import Thread

class mythread(Thread):
    def __init__(self,saying):
        super(mythread, self).__init__()
        self.saying = saying
        self.__init = True

    def run(self):
        if not self.__init:
            print "init failed"
            exit(0)
        
        print self.saying
fi = open('user.txt','r')
for p in fi.readlines():
    th = mythread(p)
    th.start()

fi.close()

