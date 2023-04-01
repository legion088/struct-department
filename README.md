# Сайт
### Задачи:
В разделе Backlog выложены основные подразделы сайта, которые необходимо реализовать.
#### 8. Структура факультета
* Departments - кафедры
		(id, 
		name, 
		descritption, 
		history, 
		persons, 	Persons-FK
		labs, 	 	Labs-FK
		events,  	Events-FK
		projects 	Projects-FK
) 

* Program types 
		(id, 
		name, 
		description) - типы направлений подготовки

* Programs - направления подготовки
		(id,
		name, 
		description, 
		program_type, 	Program types-FK
		duration, 
		partners		Partners - FK) 


* Disciplines   - дисциплины
		(id, 
		name, 
		description, 
		tags,
		mooc_url, 
		tags,
		projects,  Projects-FK
		persons,   Persons-FK
		course_num, 
		has_exam, 
		has_mark, 
		has_course_work, 
		lectures_hrs_num, 
		practice_hrs_num, 
		total_hrs_num)
![home](https://github.com/legion088/struct-department/blob/main/desc/struct.png)
