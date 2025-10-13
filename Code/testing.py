from settings import Settings

test = Settings()

test.set("Directory", "Folder", "test")
test.set("Directory", "Folder", "test2")

print(test.get("Directory", "Folder"))

