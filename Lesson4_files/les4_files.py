with open("greeting.txt", "w", encoding="utf-8") as file:
    file.write("Hello, automated tests!")
    file.write("Second line")


#file = open(........)
#file.close()

#"r" - read
# "w" - write - создает файл или перезаписывает его (стирает и показывает последний вызов)
# "a" - append - дозапись, пописывает не меняя
# "r+" - read & write - для программистов
# "rb", "wb" - pdf, screenshots

def log_test_result(test_name, status):
    with open("test_run.log", "w", encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")

log_test_result("test_login", "PASSED")
log_test_result("test_registration", "FAILED")
log_test_result("test_logout", "PASSED")