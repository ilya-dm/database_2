import json

from django.core.management.base import BaseCommand


from school.models import Teacher, Student

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', encoding='utf-8') as jsonfile:
            school = json.load(jsonfile)
            for line in school:
                if line['model'] == "school.teacher":
                    teacher = Teacher(name=line['fields']['name'],
                                      subject=line['fields']['subject'],
                                      id=line['pk'])
                    teacher.save()
                elif line['model'] == "school.student":
                    student = Student(name=line['fields']['name'],
                                      group=line['fields']['group'],
                                      id=line['pk'],
                                      )
                    student.teacher.add(line['fields']['teacher'])

                    student.save()



