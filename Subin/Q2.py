import numpy as np

arr1 = np.array([[5,7], [9,11]], float) #행1엔 5와 7, 행2엔 9와 11이 있는 2차원 2x2 array 형성
arr2 = np.array([[2,4], [6,8]], float) #행1엔 2와 4, 행2엔 6과 8이 있는 2차원 2x2 array 형성

concat_1 = np.concatenate((arr1, arr2), axis=0) #열(axis=0)을 기준으로 arr1과 arr2를 concatenate 실행
concat_2 = np.concatenate((arr1, arr2), axis=1) #행(axis=1)을 기준으로 arr1과 arr2를 concatenate 실행

print(concat_1)
print(concat_2)
#각각의 결과값을 순서대로 반환
