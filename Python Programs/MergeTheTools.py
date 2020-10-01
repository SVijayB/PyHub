def merge_the_tools(string, k):
    num=int(len(string)/k)
    for idx in range(num):
        ti=string[(idx)*k:(idx+1)*k]
    
        ui="" 
        for i in ti:
            if i not in ui:
                ui+=i
        print(ui)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
