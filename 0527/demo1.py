# 实现short排序
class Insertionsort():
    def insertion_sort(self,Array):
        # 便利array的长度从1到。。
        for i in range(1,len(Array)):

            # print(key)
            # j = 1-1,2-1,3-1....10-1
            j = i - 1
            key = Array[i]
            # j>=0永远成立 判断A[0,1,2,3,4,5,6,7,8]是否大于原来的A[1，2，3，4，5]
            while j >= 0 and Array[j] > key:
                # j =0,1,2,3,4,5
                # j+1 = 0+1,1+1,1+2
                Array[j+1] = Array[j]
                j -= 1
            Array[j+1] = key
            print(key)
        return Array

sort = Insertionsort()
a = [1, 6, 5, 7, 9, 2, 4, 3, 8, 10]
print(sort.insertion_sort(a))