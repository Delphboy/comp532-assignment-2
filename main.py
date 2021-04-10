import gym
import torch
import matplotlib.pyplot as plt
import numpy as np

# Hyper Params

# Initalise Envirnoment
env = gym.make('Breakout-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()