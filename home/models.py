from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from stdimage.models import StdImageField

# Create your models here.


class Agent(models.Model):
	image = StdImageField('Imagem', upload_to='Agent', null=True, blank=True, variations={'thumb': {'width': 70, 'height': 70, 'crop': True }})  
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('Nome do corretor', max_length=255)
	number = models.CharField('Telefone', max_length=255)
	facebook = models.URLField('Facebook',)
	instagram = models.URLField('Instagram',)
	whatsapp = models.URLField('WhatsApp',)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Corretor'
		verbose_name_plural = 'Corretores'	


class Category(models.Model):
	name = models.CharField('Nome da categoria', max_length=255)
	ICON_CHOICES = (
		('icon-1', 'residencial'),
		('icon-2', 'comercial'),
		('icon-3', 'industrial'),
		('icon-4', 'rural'),
		)
	icon = models.CharField('Icone', max_length=255, choices=ICON_CHOICES)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Categoria '
		verbose_name_plural = 'Categorias'


class State(models.Model):
	name = models.CharField('Estado', max_length=255)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = 'Estado'
		verbose_name_plural = 'Estados'
	

class City(models.Model):
	name = models.CharField('Cidade', max_length=255)
	state = models.ForeignKey(State, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name}, {self.state.name}' 

	class Meta:
		verbose_name = 'Cidade'
		verbose_name_plural = 'Cidades'	


class District(models.Model):
	name = models.CharField('Bairro', max_length=255)
	city = models.ForeignKey(City, on_delete=models.CASCADE)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = 'Bairro'
		verbose_name_plural = 'Bairros'		


class Property(models.Model):
	cover = StdImageField('Imagem', upload_to='cover', null=True, blank=True, variations={'thumb': {'width': 300, 'height': 350, 'crop': True }}) 
	agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
	title = models.CharField('Título', max_length=255)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True)
	content = models.TextField('Descrição', )
	price = models.IntegerField('Preço',) 
	address = models.TextField('Endereço',)
	NUMBER_CHOICES = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		)
	rooms =  models.CharField('Quartos', max_length=255, choices=NUMBER_CHOICES)
	bathrooms = models.CharField('Banheiros', max_length=255, choices=NUMBER_CHOICES)
	garage_size = models.CharField('Vagas', max_length=255, choices=NUMBER_CHOICES)
	area = models.IntegerField('Área', )
	TYPE_CHOICES = (
		('sale', 'Venda'),
		('rent', 'Aluguel'),
		)
	type_property = models.CharField('Venda ou Aluguel?', max_length=255, choices=TYPE_CHOICES)
	plant = StdImageField('Planta', upload_to='Plant', null=True, blank=True, variations={'thumb': {'width': 439, 'height': 337, 'crop': True }})
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	zipcode = models.CharField('CEP', max_length=255)
	google_maps = models.TextField()

	def save(self, *args, **kwargs):
		value = self.title 
		self.slug = slugify(value, allow_unicode=False)
		super().save(*args, **kwargs)

	def get_display_price(self):
		return '{0:.2f}'.format(self.price / 100)

	class Meta:
		verbose_name = 'Imóvel'
		verbose_name_plural = 'Imóveis'		
		

class Image(models.Model):
	property = models.ForeignKey(Property, on_delete=models.CASCADE)
	image = StdImageField('Imagem', upload_to='property', null=True, blank=True, variations={'thumb': {'width': 770, 'height': 520, 'crop': True }}) 