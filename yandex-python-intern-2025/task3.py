N, circle_len, max_speed = map(int, input().strip().split())
taxi: dict[int, int] = {}
for _ in range(N):
    input_row = input().strip().split()
    object_type: str = input_row[0]
    timestamp = int(input_row[1])
    id = int(input_row[2])
    position = int(input_row[3])

    if object_type == "TAXI":
        taxi[id] = position
    else:
        order_time = int(input_row[4])
        taxi_ids: list[int] = []
        count = 0
        for taxi_id, taxi_position in taxi.items():
            distance = position - taxi_position
            if distance < 0:
                distance = circle_len - taxi_position + position
            if distance <= order_time * max_speed:
                count += 1
                taxi_ids.append(taxi_id)
            if count == 5:
                break
        if taxi_ids:
            print(*taxi_ids)
        else:
            print(-1)
