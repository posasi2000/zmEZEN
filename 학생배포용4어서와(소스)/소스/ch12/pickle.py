import pickle

myMovie = { "Superman vs Batman ": 9.8, "Ironman": "9.6" }

# 딕셔너리를 피클 파일에 저장
pickle.dump( myMovie, open( "save.p", "wb" ) )

# 피클 파일에 딕션너리를 로딩
myMovie = pickle.load( open( "save.p", "rb" ) )
print(myMovie)
