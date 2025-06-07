import torch
import torch.nn as nn

class DQN(nn.Module):
    def __init__(self, state_size=4, action_size=2):
        super().__init__()
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class ReplayBuffer:
    def __init__(self, capacity=10000):
        self.buffer = []
        self.capacity = capacity
        # 在dqn_agent.py中添加
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.q_network = DQN(state_size, action_size)
        self.target_network = DQN(state_size, action_size)
        self.optimizer = torch.optim.Adam(self.q_network.parameters())
        
    def update_target(self):
        self.target_network.load_state_dict(self.q_network.state_dict())
        # 在test_dqn.py中添加
def test_target_update(self):
    agent = DQNAgent(4, 2)
    old_weights = agent.target_network.fc1.weight.clone()
    agent.update_target()
    self.assertFalse(torch.equal(old_weights, agent.target_network.fc1.weight))
        