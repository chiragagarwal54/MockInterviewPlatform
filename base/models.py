from django.db import models

def upload_TestCaseInput_location(instance, filename):
    file_path = '{ques}/{tcnumber}/input/{filename}'.format(
        ques=str(instance.question.id), tcnumber=str(instance.testcasenumber), filename=filename,
    )
    return file_path

def upload_TestCaseOutput_location(instance, filename):
    file_path = '{ques}/{tcnumber}/output/{filename}'.format(
        ques=str(instance.question.id), tcnumber=str(instance.testcasenumber), filename=filename,
    )
    return file_path

def upload_GeneratorFile_location(instance, filename):
    file_path = '{id}/generator/{filename}'.format(
        id=str(instance.id), filename=filename,
    )
    return file_path

class Company(models.Model):
    name = models.CharField(max_length=100)
    total_set = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class MockSet(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rounds = models.IntegerField(default=0)
    msnumber = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.company.name + ", Set: " + str(self.msnumber)

    def save(self, *args, **kwargs):
        super(MockSet, self).save(*args, **kwargs)
        if(not self.msnumber):
            total = MockSet.objects.filter(company=self.company).count()
            self.msnumber = total
            self.save()

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    quesnumber = models.IntegerField(null=True, blank=True)
    mockset = models.ForeignKey(MockSet, on_delete=models.CASCADE)
    constraints = models.TextField()
    example_input = models.TextField()
    example_output = models.TextField()
    solution = models.TextField()
    generatorfile = models.FileField(upload_to=upload_GeneratorFile_location)

    def __str__(self):
        return str(self.id) + ": " + self.title

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)
        if(not self.quesnumber):
            total = Question.objects.filter(mockset=self.mockset).count()
            self.quesnumber = total
            self.save()

class TestCase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    testcasenumber = models.IntegerField()
    input = models.FileField(upload_to=upload_TestCaseInput_location)
    output = models.FileField(upload_to=upload_TestCaseOutput_location)

    def __str__(self):
        return str(self.testcasenumber)
