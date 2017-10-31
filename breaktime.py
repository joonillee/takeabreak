import time
import webbrowser

total_breaks = 3
break_count = 0

print ("program started on "+ time.ctime())

while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PLTkU01h2I4vt0F5LCB8Ybb3QTQOI8PgAH")
    break_count = break_count + 1
    print (" The video was played: " + str(break_count) + " times")

print ("See it? It's good to take a break!")

