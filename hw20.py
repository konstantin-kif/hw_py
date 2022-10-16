# Напишите программу, удаляющую из текста все слова, содержащие "абв".

txt = ('У моих детей, конечно, будет компьютер. Но первым делом они получат книги'.split())
print(txt)
result = filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, txt)
print(*result)

