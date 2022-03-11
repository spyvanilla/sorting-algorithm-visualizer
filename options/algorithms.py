from options.draw import Draw

class Algorithms:

    def __init__(self,window,start_list):
        self.window = window
        self.start_list = start_list
        self.draw = Draw(self.window)

    def bubble_sort(self):
        end = len(self.start_list)

        while end > 1:
            traded = False
            index = 0
            
            while index < end-1:
                if self.start_list[index] > self.start_list[index+1]:
                    traded = True
                    temp = self.start_list[index]
                    self.start_list[index] = self.start_list[index+1]
                    self.start_list[index+1] = temp
                    self.draw.draw(self.start_list)
                index += 1

            if not traded:
                break
            end -= 1

    def insertion_sort(self):
        for i in range(1, len(self.start_list)):
            j = i-1
            nxt_element = self.start_list[i]

            while self.start_list[j] > nxt_element and j >= 0:
                self.start_list[j+1] = self.start_list[j]
                self.draw.draw(self.start_list)
                j=j-1

            self.start_list[j+1] = nxt_element
        self.draw.draw(self.start_list)

    def shell_sort(self):
        n = len(self.start_list)
        gap = n//2

        while gap > 0:
    
            for i in range(gap,n):
                temp = self.start_list[i]
                j = i

                while  j >= gap and self.start_list[j-gap] >temp:
                    self.start_list[j] = self.start_list[j-gap]
                    self.draw.draw(self.start_list)
                    j -= gap

                self.start_list[j] = temp
                self.draw.draw(self.start_list)
            gap //= 2