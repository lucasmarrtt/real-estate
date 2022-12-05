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


class Category(models.Model):
	name = models.CharField('Nome da categoria', max_length=255)
	ICON_CHOICES = (
		('icon-1', 'residencial'),
		('icon-2', 'comercial'),
		('icon-3', 'industrial'),
		('icon-4', 'rural'),
		)
	icon = models.CharField('Icone', max_length=255, choices=ICON_CHOICES)



class Property(models.Model):
	agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
	title = models.CharField('Título', max_length=255)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True)
	image_01 = StdImageField('Imagem', upload_to='Property', null=True, blank=True, variations={'thumb': {'width': 770, 'height': 520, 'crop': True }}) 
	image_02 = StdImageField('Imagem', upload_to='Property', null=True, blank=True, variations={'thumb': {'width': 770, 'height': 520, 'crop': True }})
	image_03 = StdImageField('Imagem', upload_to='Property', null=True, blank=True, variations={'thumb': {'width': 770, 'height': 520, 'crop': True }})
	image_04 = StdImageField('Imagem', upload_to='Property', null=True, blank=True, variations={'thumb': {'width': 770, 'height': 520, 'crop': True }})
	image_05 = StdImageField('Imagem', upload_to='Property', null=True, blank=True, variations={'thumb': {'width': 770, 'height': 520, 'crop': True }})
	content = models.TextField()
	price = models.IntegerField() 
	address = models.TextField()
	rooms = models.IntegerField('Quartos',)
	bathrooms = models.IntegerField('Banheiros',)
	garage_size = models.IntegerField('Vagas na garagem',)
	area = models.IntegerField('Área', )
	TYPE_CHOICES = (
		('sale', 'Venda'),
		('rent', 'Aluguel'),
		)
	type_property = models.CharField('Venda ou Aluguel?', max_length=255, choices=TYPE_CHOICES)
	plant = StdImageField('Planta', upload_to='Plant', null=True, blank=True, variations={'thumb': {'width': 439, 'height': 337, 'crop': True }})
	city = models.CharField('Cidade', max_length=255)
	state = models.CharField('Estado', max_length=255)
	zipcode = models.CharField('CEP', max_length=255)
	google_maps = models.TextField()

	def save(self, *args, **kwargs):
		value = self.title 
		self.slug = slugify(value, allow_unicode=False)
		super().save(*args, **kwargs)

	def get_display_price(self):
		return '{0:.2f}'.format(self.price / 100)
		

