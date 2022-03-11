from draw import draw

def bubble_sort(window,start_list):
    end = len(start_list)

    while end > 1:
        traded = False
        index = 0
        
        while index < end-1:
            if start_list[index] > start_list[index+1]:
                traded = True
                temp = start_list[index]
                start_list[index] = start_list[index+1]
                start_list[index+1] = temp
                draw(window,start_list)
            index += 1

        if not traded:
            break
        end -= 1

def insertion_sort(window,start_list):
    for i in range(1, len(start_list)):
        j = i-1
        nxt_element = start_list[i]

        while start_list[j] > nxt_element and j >= 0:
            start_list[j+1] = start_list[j]
            draw(window,start_list)
            j=j-1

        start_list[j+1] = nxt_element
    draw(window,start_list)