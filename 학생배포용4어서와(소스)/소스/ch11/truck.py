# 일반적인 운송수단을 나타내는 클래스이다. 
class Vehicle:
	def __init__(self, make, model, color,  price):
		self.make = make		# 메이커
		self.model = model	# 모델
		self.color = color		# 자동차의 색상
		self.price = price		# 자동차의 가격

	def setMake(self, make):	# 설정자 메소드 
		self.make = make

	def getMake(self):		# 접근자 메소드
		return self.make

	# 차량에 대한 정보를 문자열로 요약하여서 반환한다.
	def getDesc(self):
		return "차량 =("+str(self.make)+","+\
                                        str(self.model)+","+\
                                        str(self.color)+","+\
                                        str(self.price)+")"
class Truck(Vehicle) :				# ①
	def __init__(self, make, model, color, price, payload):
		super().__init__(make, model, color, price)	# ②
		self.payload=payload			# ③

	def setPayload(self, payload):	# 설정자 메소드 
		self.payload=payload

	def getPayload(self):		# 접근자 메소드 
		return self.payload
def main():						# main() 함수 정의
	myTruck = Truck("Tisla", "Model S", "white", 10000, 2000)	# 객체 생성
	myTruck.setMake("Tesla")				# 설정자 메소드 호출
	myTruck.setPayload(2000)				# 설정자 메소드 호출
	print(myTruck.getDesc())				# 트럭 객체를 문자열로 출력

main()
