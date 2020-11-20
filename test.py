# # import time
# # from multiprocessing import Pool


# # def sum_square(number):
# #     s = 0
# #     for i in range(number):
# #         s += i * i
# #     return s


# # def sum_square_with_mp(numbers):

# #     start_time = time.time()
# #     p = Pool()
# #     result = p.map(sum_square, numbers)

# #     p.close()
# #     p.join()

# #     end_time = time.time() - start_time

# #     print(f"Processing {len(numbers)} numbers took {end_time} time using multiprocessing.")


# # def sum_square_no_mp(numbers):

# #     start_time = time.time()
# #     result = []

# #     for i in numbers:
# #         result.append(sum_square(i))
# #     end_time = time.time() - start_time

# #     print(f"Processing {len(numbers)} numbers took {end_time} time using serial processing.")


# # if __name__ == '__main__':
# #     numbers = range(1000)
# #     sum_square_with_mp(numbers)
# #     sum_square_no_mp(numbers)

from multiprocessing import Process
import smartMover
import random
import chess
import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

def func(new_board, n):
    # simulationSum = []
    # for num in range(n):
    #     simulationSum.append(smartMover.Player(board, color, time).runSimulation(board))
    # print(simulationSum)
    # m = 0
    # for i in range(n):
    #     m += i
    # global x
    # x += m
    children = list(new_board.legal_moves)
    while len(children) > 0:
        new_board.push(random.choice(list(new_board.legal_moves)))
        children = list(new_board.legal_moves)
    print(n)

if __name__ == '__main__':
    p = Process(target=func, args=(chess.Board, 2,))
    p1 = Process(target=func, args=(chess.Board, 5,))
    p2 = Process(target=func, args=(chess.Board, 3,))
    p3 = Process(target=func, args=(chess.Board, 4,))
    p.start()
    p1.start()
    p2.start()
    p3.start()
    p.join()
    p1.join()
    p2.join()
    p3.join()
