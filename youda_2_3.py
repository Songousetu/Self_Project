# -*- encoding: utf-8 -*-

from numpy import *

class NeuralNetwork():
    def __init__(self):
       #使用seed 确保程序每次运行时 都能生成相同的数字

        random.seed(1)

        # 我们建造一个单层神经网络，用三个输入的连接和一个输出的连接
        # 随机分配一个在-1到1之间的数 作为权重，为一个3*1 （三行，一列）的矩阵，均值为0
        self.synaptic_weights = 2*random.random((3,1)) -1

    #控制输出结果在0到1之间
    def __sigmoid(self,x):
        return 1/(1+exp(-x))

    #计算S曲线的斜率，衡量现有权重的可信度
    def __sigmoid_derivative(self,x):
        return x*(1-x)


    def train(self,training_set_inputs,training_set_outputs,number_of_training_iterations):
        for iteration in range(number_of_training_iterations):

            output = self.predict(training_set_inputs) # 使用predict函数将训练集在神经网络上传递，预测结果

            # 计算误差,我们希望通过训练尽量减小这一误差，通过反复跟新权重来实现这一点
            error = training_set_outputs - output

            # 通过计算输入的转置矩阵和差值的点积，再乘以S型曲线的梯度，算出必要的调整系数,梯度下降
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output)) #derivative:导数

            # 调整权重
            self.synaptic_weights += adjustment


    def predict(self,inputs):
        #我们将在predict函数中直接使用 __sigmoid 函数
        #将输入作为参数 并通过我们的神经元传递这些参数
        weights = self.synaptic_weights

        result1 = dot(inputs, weights)

        result = self.__sigmoid(result1)
        #return self.__sigmoid(dot(inputs,self.synaptic_weights))#  计算输入和权重的点积
        return result




if __name__ == "__main__":
    #创建一个单层神经元网络
    neural_network = NeuralNetwork()

    print ('Random starting synaptic weights:')
    print (neural_network.synaptic_weights)

    #训练数据有四组样本，每个样本中有三个值
    #有一个标签
    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    #训练神经网络 用训练数据
    #训练10000 次
    neural_network.train(training_set_inputs,training_set_outputs,10000)

    print ('New synaptic weights after training:')
    print (neural_network.synaptic_weights)

    #测试训练好的神经网络
    print ('predicting')
    print (neural_network.predict(array))