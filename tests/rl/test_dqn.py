import unittest
import torch
from src.rl.dqn_agent import DQN

class TestDQN(unittest.TestCase):
    def test_network_shape(self):
        net = DQN()
        input = torch.randn(1, 4)
        self.assertEqual(net(input).shape, (1, 2))

if __name__ == "__main__":
    unittest.main()
    