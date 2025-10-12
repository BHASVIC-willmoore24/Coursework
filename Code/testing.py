from settings import Settings

test = Settings()

test.add("Directory", "TTTTT", "JJJJJJJ")
print(test.get("Directory", "TTTTT"))

test.set("Directory", "TTTTT", "kkkkkkk")
print(test.get("Directory", "TTTTT"))

test.add("test33", "test", "test9999")

