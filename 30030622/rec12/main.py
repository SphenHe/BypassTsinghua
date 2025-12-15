import random
init_value = 1
max_value = 3
fail_value = 0
win_rate = 2/3
repeat_times = 100000000
win_count = 0

import tqdm
for i in tqdm.tqdm(range(repeat_times)):
    init = init_value
    while(1):
        if init == fail_value:
            break
        elif init == max_value:
            win_count += 1
            break
        else:
            if random.random() < win_rate:
                init += 1
            else:
                init -= 1
print("win rate: ", win_count / repeat_times)
