from bs4 import BeautifulSoup
import requests 
from newspaper import Article
from urllib.parse import urlparse
import difflib

class Noticia:
	"""Classe para a coleta de dados de uma notícia"""

	def __init__(self, url):
		self.url = url
		self.titulo = self.pegaTitulo() 
		self.autores = self.pegaAutores() #true or false
		self.maiusculo = self.pegaMaiusculo() #true or false
		self.hostname = self.pegaHostname()
		self.request = self.apiRequest()
		self.nota = float(self.request['response'][0]['page_rank_decimal']) / 10
		self.rank =  1 - float(self.request['response'][0]['rank']) / 3000000000

	def pegaTitulo(self):
		"""Retorna o título da página"""

		r = requests.get(self.url) #faz o request a url informada
		pagina = r.text #transforma a pagina web do request em texto

		soup = BeautifulSoup(pagina, "html5lib") #cria um objeto beautifulsoup para ser analisado


		tituloDaPagina = str(soup.title.string) #passa para a variável o título da página
		print('Titulo: \t' + tituloDaPagina)

		return tituloDaPagina

	def pegaAutores(self):
		"""Retorna 1 se tiver autor e 0 se não tiver autor"""

		article = Article(self.url)
		article.download()
		article.parse()

		print("Autores:\t", article.authors)

		if not article.authors:
			return 0
		else:
			return 1

		#return article.authors

	def pegaMaiusculo(self):
		"""Retorna 1 se o título está em minúsculo
		e 0 para se o título estver em maiúsculo"""

		if(self.titulo.isupper()):
			return 0
		else:
			return 1
        
	def pegaHostname(self):
		"""Retorna o hostname da url"""
		host = urlparse(self.url)
		result = host.netloc
		print("Hostname: \t" + result)
		return result

	def apiRequest(self):
		"""Faz o request para a api do open page rank"""
		import requests
		headers = {'API-OPR':'w0gswkcgcwcgs04o4kkcko0oo04k480co0gwg00k'}
		domain = self.hostname
		url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
		request = requests.get(url, headers=headers)
		return request.json()
		print(result['response'][0]['page_rank_decimal'], result['response'][0]['rank'])

class Pesquisa:
	"""Essa classe é responsável por realizar a pesquisa de notícia similares"""
	@staticmethod
	def pesquisa(termo):
		"""Recebe uma string com o título da notícia como parâmetro, faz uma pesquisa no google
		e retorna uma lista com os links das notícias similares"""

		url = "https://www.google.com/search?q={0}".format(termo) #insere a pesquisa na url do google

		request = requests.get(url) #faz o request da página de resultados
		soup = BeautifulSoup(request.text, 'html5lib') #cria um objeto com a página html
		headlines = soup.find_all('h3', class_='r') #retira todos os textos dentro das tags h3 da classe r

		resultados = [] #lista para os resultados

		for h in headlines: #for para pegar o link de todos os resultados 
			links = h.a.get('href')
			a = links.split('&')
			resultados.append(a[0].replace("/url?q=","")) #filtra a url tirando as partes do google

		return resultados

	@staticmethod
	def getSimilares(noticia):
		"""Recebe um objeto notícia como parâmetro, realiza uma comparação entre os resultados
		da pesquisa e retorna as notícias que possuem similaridade no título superior a 60%"""
		
		similares = [] #lista para por as noticias semelhantes
		for p in Pesquisa.pesquisa(noticia.titulo): #for nos resultados da pesquisa
			try:
				a = Noticia(p) #cria um objeto notícia com um resultado da pesquisa

				#pega a porcentagem de caracteres iguais entre dois titulos
				sequence = difflib.SequenceMatcher(isjunk=None, a=a.titulo, b=noticia.titulo)
				difference = sequence.ratio()*100
				difference = round(difference,1)
				print(str(difference) + "% match")

				if float(difference) > 60: #seleciona as noticias somente com mais de 60% de igualdade
					similares.append(a)
			except:
				print('')
			
		return similares
		
		
	@staticmethod 
	def contanoticias(similares):
        #contagem do total de notícias semelhantes
		contaNoticias = 0
		for p in similares: 
			print(p.titulo + "\n")
			contaNoticias+=1

		return contaNoticias
    
	@staticmethod
	def rankSimilares(listapesquisa,similares):
		"""Recebe a lista de similares como parâmetro e busca fazer uma média simples entre os
		ranks e notas dos sites que possuem a similaridade."""

		if similares == 0:
			return 0
		else:
			somarank=0
			for p in listapesquisa:
				somarank+=p.rank
			return somarank/similares

	@staticmethod   
	def notaSimilares(listapesquisa,similares):

		if similares == 0:
			return 0
		else:
			somanota=0
			for p in listapesquisa:
				somanota+=p.nota
			return somanota/similares

print('Digite o link da noticia')
link = str(input())
noticia = Noticia(link) #cria um objeto noticia
lista = Pesquisa.getSimilares(noticia)
similares = Pesquisa.contanoticias(lista)
print(similares)
mediarank = Pesquisa.rankSimilares(lista,similares)
medianota = Pesquisa.notaSimilares(lista,similares)

print('/******INFORMAÇÕES PARA A MODELAGEM*******/')
print('Titulo: ', noticia.titulo)
print('Tem autor: ', noticia.autores)
print('Está em maiusculo: ', noticia.maiusculo)
print('Nota do site: ', noticia.nota)
print('Ranking complementar: ', noticia.rank)
print('Noticias similares: ', similares / 10)

vetor = [noticia.autores, noticia.nota,
	noticia.rank, similares/10, mediarank, medianota]

print(vetor)

porcentagem = 0

for p in vetor:
	porcentagem += p/6

print(porcentagem)
#print('\n[{}, {}, {}, {}, {}, {}, {}]'.format(noticia.autores, noticia.maiusculo, noticia.nota, noticia.rank, similares/10, mediarank, medianota))
