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

    def partition(self, low, high):
        i = (low-1)
        pivot = self.start_list[high]
    
        for j in range(low, high):
            if self.start_list[j] <= pivot:

                i = i+1
                self.start_list[i], self.start_list[j] = self.start_list[j], self.start_list[i]
                self.draw.draw(self.start_list)
    
        self.start_list[i+1], self.start_list[high] = self.start_list[high], self.start_list[i+1]
        self.draw.draw(self.start_list)
        return (i+1)
        
        
    def quick_sort(self, low, high):
        if len(self.start_list) == 1:
            return self.start_list
        if low < high:
            pi = self.partition(low, high)

            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def pigeonhole_sort(self):
        my_min = min(self.start_list)
        my_max = max(self.start_list)
        size = my_max - my_min + 1
    
        holes = [0]*size
    
        
        for x in self.start_list:
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1

        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                self.start_list[i] = count + my_min
                self.draw.draw(self.start_list)
                i += 1

    def cycle_sort(self):
        writes = 0

        for cycleStart in range(0, len(self.start_list) - 1):
            item = self.start_list[cycleStart]
            pos = cycleStart

            for i in range(cycleStart + 1, len(self.start_list)):
                if self.start_list[i] < item:
                    pos += 1
            if pos == cycleStart:
                continue

            while item == self.start_list[pos]:
                pos += 1
            self.start_list[pos], item = item, self.start_list[pos]
            self.draw.draw(self.start_list)
            writes += 1

            while pos != cycleStart:
                pos = cycleStart
                for i in range(cycleStart + 1, len(self.start_list)):
                    if self.start_list[i] < item:
                        pos += 1

                while item == self.start_list[pos]:
                    pos += 1
                self.start_list[pos], item = item, self.start_list[pos]
                self.draw.draw(self.start_list)
                writes += 1

        return writes