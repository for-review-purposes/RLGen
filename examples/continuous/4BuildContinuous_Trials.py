# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:22:43 2022

@author: Anonymous
"""


import scripts.GMEnv as sim
import scripts.Tester as test
import unittest


class TestSum(unittest.TestCase):
    simRandom = 0 
    simCustom = 0 
    simOptimal = 0 
    
    simRandomIter = 100
    simCustomIter = 100
    simOptimalIter = 100
    testingIter = 1000
    
   
    trainingIter = 1000
    learningAlgorithm = "PPO"
    learningLoggingInterval = 500
    
    learningOptimal = 0
    learningParams = 0
    dtGologOptimal = 0.47599999999999987
    
    def setUp(self):
        self.env = sim.GMEnv("./examples/continuous/4BuildContinuous.pl")
        self.env.setDebug(False)
        self.env.setSeed(123)
        self.t = test.TestIt(self.env)
        self.t.debug = False
        self.inFeasiblePenalty = self.env.getInfeasiblePenalty()
                
    def tearDown(self):
        self.env.closeQE()

    def test_semiRandonSim(self):
        """
        A simulation based on a crude policy that assumes certain success of actions.

        Returns
        -------
        None.

        """
        result = self.t.simulate(self.simCustomIter,[0,2])
        TestSum.simCustom = result
            
    def test_randonSim(self):
        """
        A random policy (actions are picked randomly)

        Returns
        -------
        None.

        """
        result = self.t.simulate(self.simRandomIter)
        TestSum.simRandom = result
    
    
    def test_learning(self):
        """
        Training and testing an RL agent

        Returns
        -------
        None.

        """
        result, params = self.t.test_learning(self.trainingIter,self.testingIter, logging = self.learningLoggingInterval, algo = self.learningAlgorithm)
        TestSum.learningOptimal = result
        TestSum.learningParams = params
            

    @classmethod
    def tearDownClass(cls):
        print('DT-Golog - calculated policy reward: {}'.format(cls.dtGologOptimal))
        #print('DT-Golog - simulated policy reward : {}'.format(cls.simOptimal))
        print('Partially optimal policy reward....: {}'.format(cls.simCustom))
        print('Random policy reward.............. : {}'.format(cls.simRandom))
        print('Learned policy reward..............: {}'.format(cls.learningOptimal))
        print('--> Learning Parameters: \n {}'.format(cls.learningParams))



    # def test_simulation(self):
    #     result = self.t.simulate(10000,[0,2])
    #     TestSum.simOptimal = result
    #     self.assertAlmostEqual(result,
    #               self.dtGologOptimal, 
    #               places = 1,
    #               msg = "\n Wrong simulaton result status: {} expected, {} observed".format(TestSum.dtGologOptimal,result))
        

    # def test_randomSim(self):
    #     result = self.t.simulate(10000)
    #     TestSum.simRandom = result


    # def test_learning(self):
    #     result, params = self.t.test_learning(100000,1000,logging = 1000,algo = "DQN")
    #     TestSum.learningOptimal = result
    #     TestSum.learningParams = params
    #     self.assertAlmostEqual(result,
    #                       self.dtGologOptimal, 
    #                       places = 1,
    #                       msg = "\n Learning failed: {} expected, {} observed".format(TestSum.dtGologOptimal,result))
        

    # @classmethod
    # def tearDownClass(cls):
    #     print('DT-Golog - calculated policy reward: {}'.format(cls.dtGologOptimal))
    #     print('DT-Golog - simulated policy reward.:  {}'.format(cls.simOptimal))
    #     print('Random simulated policy reward.....:  {}'.format(cls.simRandom))
    #     print('Learned policy reward..............: {}'.format(cls.learningOptimal))
    #     print('--> Learning Parameters: \n {}'.format(cls.learningParams))


        
if __name__ == '__main__':
    unittest.main()
    


# env = sim.GoalModel("./Examples/3Build.pl")
# env.setDebug(True)
# env.setSeed(123)
# t = test.TestIt(env)
# t.debug = False
# a,b,c,d,e = t.performAction(0)
# a,b,c,d,e = t.performAction(0)
# a,b,c,d,e = t.performAction(1)
# a,b,c,d,e = t.performAction(2)
# a,b,c,d,e = t.performAction(2)
# a,b,c,d,e = t.performAction(3)
# a,b,c,d,e = t.performAction(1)
# a,b,c,d,e = t.performAction(0)
# a,b,c,d,e = t.performAction(2)
# a,b,c,d,e = t.performAction(3)
# env.reset()
# env.setSeed(15)
# a,b,c,d,e = t.performAction(1)
# a,b,c,d,e = t.performAction(1)
# a,b,c,d,e = t.performAction(0)
# a,b,c,d,e = t.performAction(2)
# a,b,c,d,e = t.performAction(3)
# a,b,c,d,e = t.performAction(3)
# a,b,c,d,e = t.performAction(2)
# a,b,c,d,e = t.performAction(1)
# a,b,c,d,e = t.performAction(0)
# a,b,c,d,e = t.performAction(2)
# a,b,c,d,e = t.performAction(3)
