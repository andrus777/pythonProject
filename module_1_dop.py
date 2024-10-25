grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_rating = {} # Создаем пустой словарь
list_name = list(students) # Преобразуем множество в список
list_name.sort() # Сортируем список имен по алфавиту

# Перебираем элементы списка с оценками
i_ = 0
for m in grades:
    student_rating.update({list_name[i_]: sum(m)/ len(m)}) # Добавляем Ключ (Имя) + Значение (среднее по списку оценок)
    i_ = i_+1
print(student_rating) # Выводим итоговый словарь