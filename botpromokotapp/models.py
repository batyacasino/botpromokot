from django.db import models

class Campaigns(models.Model):
	id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ["name"]

	
	def __str__(self):
		return self.name


class Categories(models.Model):
	id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ["id"]

	
	def __str__(self):
		return self.name

class Types(models.Model):
	id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ["id"]

	
	def __str__(self):
		return self.name


class Cupons(models.Model):
	id = models.IntegerField(primary_key=True, unique=True)
	rating = models.FloatField()
	campaigns = models.ForeignKey(Campaigns, on_delete=models.CASCADE)
	goto_link = models.CharField(max_length=200)
	short_name = models.CharField(max_length=200)
	discount = models.CharField(max_length=200, null=True, blank=True)
	image = models.CharField(max_length=200)
	promocode = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
	types = models.ForeignKey(Types, on_delete=models.CASCADE)

		# Metadata
	class Meta:
		ordering = ["-rating"]

	
	def __str__(self):
		return self.campaigns
