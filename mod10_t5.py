from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    #return all_data


#files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time.time()
for filename in filenames:
    read_info(filename)
result = time.time() - start
print(f'Время выполнения линейного вызова: {result} секунд')

if __name__ == '__main__':
    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    result2 = time.time() - start_time
    print(f'Время выполнения многопроцессного вызова: {result2} секунд')
