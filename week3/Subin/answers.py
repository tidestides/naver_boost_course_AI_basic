#1
import numpy as np

arr1 = np.arange(1,16).reshape(5,3) #1부터 15까지 5x3 배열
arr2 = np.arange(17,23).reshape(3,2) #17부터 22까지 3x2 배열

dot = arr1.dot(arr2)  #dot 함수를 사용해 행열곱 연산 진행


print(dot, dot.shape) # arr1과 arr2의 행열곱 연산 결과 및 결과값의 shape 반환



#2
import numpy as np

arr1 = np.array([[5,7], [9,11]], float) #행1엔 5와 7, 행2엔 9와 11이 있는 2차원 2x2 array 형성
arr2 = np.array([[2,4], [6,8]], float) #행1엔 2와 4, 행2엔 6과 8이 있는 2차원 2x2 array 형성

concat_1 = np.concatenate((arr1, arr2), axis=0) #열(axis=0)을 기준으로 arr1과 arr2를 concatenate 실행
concat_2 = np.concatenate((arr1, arr2), axis=1) #행(axis=1)을 기준으로 arr1과 arr2를 concatenate 실행

print(concat_1)
print(concat_2)
#각각의 결과값을 순서대로 반환



#3 예시답안
import numpy as np
xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

print(x_train, x_train.shape)
print(y_train, y_train.shape)



#4 예시답안
beta_gd = np.random.rand(1)
bias = np.random.rand(1)



#5 예시답안
import numpy as np
xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

print(x_train, x_train.shape)
print(y_train, y_train.shape)

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.001

for i in range(1000):
    pred = (x_train * beta_gd) + bias
    error = ((pred - y_train) ** 2).mean()

    gd_w = ((pred - y_train) * 2 * x_train).mean()
    gd_b = ((pred - y_train) * 2).mean()

    beta_gd -= learning_rate * gd_wbias -= learning_rate * gd_b
    
    if i % 100 == 0:
        print('Epoch ({:10d}/1000) cost: {:10f}, W: {:10f}, b:{:10f}'.format(i, error, beta_gd.item(), bias.item()))
