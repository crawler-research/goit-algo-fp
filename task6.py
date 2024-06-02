def greedy_algorithm(items, budget):
    # сортування за співвідношенням ціни до калорійності
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    result = []
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            result.append(item)
    return result

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    for i in range(1, budget + 1):
        for item, info in items.items():
            if info['cost'] <= i:
                dp[i] = max(dp[i], dp[i - info['cost']] + info['calories'])
    result = []
    i = budget
    while i > 0:
        for item, info in items.items():
            if info['cost'] <= i and dp[i] == dp[i - info['cost']] + info['calories']:
                result.append(item)
                i -= info['cost']
                break
    return result

# Test
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))
