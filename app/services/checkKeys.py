def check_keys(obj, required_keys):
    try:
        for key in required_keys:
            _ = obj[key] # Attempt to access the key
    except KeyError as e:
        print(f"Missing key: {e}")
        return False
    return True

# # Example usage
# my_dict = {"name": "John", "age": 30}
# required_keys = ["name", "age"]

# if check_keys(my_dict, required_keys):
#     print("All required keys are present.")
# else:
#     print("Some required keys are missing.")

# from abc import ABC, abstractmethod

# class MyInterface(ABC):
#     @abstractmethod
#     def method1(self):
#         pass

#     @abstractmethod
#     def method2(self, arg1):
#         pass
    
# class MyClass(MyInterface):
#     def method1(self):
#         print("Implementing method1")

#     def method2(self, arg1):
#         print(f"Implementing method2 with arg: {arg1}")

# # This will work fine
# try:
#     my_instance = MyClass()
#     my_instance.method1('yo')
#     my_instance.method2("Hello")
# except Exception as e:
#     print(e)
    
# exit(1)
