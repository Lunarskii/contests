def next_train(train_arrival_time, period, friends_arrival_time) -> int:
    if friends_arrival_time <= train_arrival_time:
        return train_arrival_time
    k: int = (friends_arrival_time - train_arrival_time + period - 1) // period
    return train_arrival_time + k * period


count_of_branches: int = int(input())
trains: list[tuple] = [tuple(map(int, input().split())) for _ in range(count_of_branches)]
count_of_requests: int = int(input())
branches: list[tuple] = [tuple(map(int, input().split())) for _ in range(count_of_requests)]


for branch_number, friends_arrival_time in branches:
    train_arrival_time, period = trains[branch_number - 1]
    print(next_train(train_arrival_time, period, friends_arrival_time))
