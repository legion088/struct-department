from django.db import models


class Persons(models.Model):
    pass


class Labs(models.Model):
    pass


class Events(models.Model):
    pass


class Projects(models.Model):
    pass


class Partners(models.Model):
    pass


class Tag(models.Model):
    pass


class Department(models.Model):
    name = models.CharField(db_index=True, max_length=200, unique=True)
    description = models.CharField(max_length=400, blank=True)
    history = models.TextField()
    persons = models.ForeignKey(Persons, on_delete=models.CASCADE, blank=True, null=True)
    labs = models.ForeignKey(Labs, on_delete=models.CASCADE, blank=True, null=True)
    events = models.ForeignKey(Events, on_delete=models.CASCADE, blank=True, null=True)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'


class TypeProgram(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=200)
    description = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_program'


class Programs(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=100)
    description = models.CharField(max_length=200, blank=True)
    duration = models.IntegerField()
    type_program = models.ForeignKey(TypeProgram, on_delete=models.CASCADE, related_name='type_program')
    partners = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name='type_program', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'program'


class Disciplines(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=100)
    description = models.CharField(max_length=200, blank=True)
    mooc_url = models.URLField(blank=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True)
    persons = models.ForeignKey(Persons, on_delete=models.CASCADE, blank=True, null=True)
    course_name = models.IntegerField()
    has_exam = models.BooleanField()
    has_mark = models.BooleanField()
    has_course_work = models.BooleanField()
    lectures_hrs_num = models.IntegerField()
    practice_hrs_num = models.IntegerField()
    total_hrs_num = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'discipline'
