from heartpole import HeartPole

do_nothing = 0
drink_coffee = 1
drink_beer = 2
sleep = 3

def vadim(env, max_iter=1000):
    """A reference strategy based on a certain PhD student named Vadim"""

    env.reset()
    total_reward = 0
    i = 0

    def step(action):
        nonlocal total_reward
        nonlocal i

        _, reward, _, _ = env.step(action)
        total_reward += reward
        i += 1

    while i < max_iter:
        step(drink_coffee)
        
        for work_idx in range(31):
            step(do_nothing)

        step(sleep)

    return total_reward

heartpole = HeartPole()
attempts = 20

print(sum(vadim(heartpole) for att in range(attempts)) / attempts)