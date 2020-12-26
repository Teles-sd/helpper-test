import os
clear = lambda: os.system('clear')
 
 
# ID:Client
clients = {}
idSet = set()

class Client:
	
	ID = 0
	name = ''
	email = ''
	cpf = ''
	phone = ''
	cep = ''
	logradouro = ''
	num = ''
	bairro = ''
	cidade = ''
	estado = ''
	
	def __init__(self, ID, name, email, cpf, phone, cep, logradouro, num, bairro, cidade, estado):
		self.ID = ID
		self.name = name
		self.email = email
		self.cpf = cpf
		self.phone = phone
		self.cep = cep
		self.logradouro = logradouro
		self.num = num
		self.bairro = bairro
		self.cidade = cidade
		self.estado = estado
	
	def display(self):
		print("\n\n\tID: {}\n\n\tNome: {}\n\te-mail: {}\n\tCPF ou CNPJ: {}\n\tTelefone: {}\n\tCEP: {}\n\tLogradouro: {}\n\tNúmero: {}\n\tBairro: {}\n\tCidade: {}\n\tEstado: {}".format(self.ID, self.name, self.email, self.cpf, self.phone, self.cep, self.logradouro, self.num, self.bairro, self.cidade, self.estado))


def cadastro():
	# ID
	if not bool(idSet):
		ID = 0
	else:
		ID = list(idSet)[-1] + 1
	
	clear()
	name = input('\n\tDigite seu nome: ')
	
	clear()
	email = input('\n\tDigite seu e-mail: ')
	
	clear()
	cpf =  input('\n\tDigite seu cpf: ')
	
	clear()
	phone = input('\n\tDigite seu telefone: ')
	
	clear()
	cep = input('\n\tDigite seu CEP: ')
	
	clear()
	logradouro = input('\n\tDigite seu logradouro: ')
	
	clear()
	num = input('\n\tDigite o Número: ')
	
	clear()
	bairro = input('\n\tDigite seu bairro: ')
	
	clear()
	cidade = input('\n\tDigite sua cidade: ')
	
	clear()
	estado = input('\n\tDigite seu Estado: ')
	
	clients[str(ID)] = Client( ID, name, email, cpf, phone, cep, logradouro, num, bairro, cidade, estado)
	idSet.add(ID)

def displayData():
	clear()
	
	if not bool(idSet):
		print("")
		input("\tNenhum cliente ainda, adicione alguem. (Enter para continuar.)")
		print("")
		
	else:
		print("")
		print("\tLista de Clientes:")
		print("")
		
		print("")
		print ("\t{:>5}\t{}".format("ID", "Nome"))
		print("")
		for ID,client in clients.items():
			print ("\t{:>5}\t{}".format(ID, client.name))
		
		print("")
		ans = input("\tQual cliente exibir informação? (digite o ID): ")
		
		clients[ans].display()
		print("")
		
		# wait
		input("(Enter para continuar.)")

def delClient():
	clear()
	
	if not bool(idSet):
		print("")
		input("\tNenhum cliente ainda, adicione alguem. (Enter para continuar.)")
		print("")
		
	else:
		print("")
		print("\tLista de Clientes:")
		print("")
		
		print("")
		print ("\t{:>5}\t{}".format("ID", "Nome"))
		print("")
		for ID,client in clients.items():
			print ("\t{:>5}\t{}".format(ID, client.name))
		
		print("")
		ans = input("\tQual cliente deseja excluir? (digite o ID): ")
		
		clients.pop(ans)
		idSet.discard(ans)


#################

running = True

while running:
	clear()
	
	print("")
	print("\tNovo Cliente:\t\t [N]")
	print("\tListar Dados de Cliente: [L]")
	print("\tExcluir Cliente:\t [E]")
	print("\tSair:\t\t\t [S]")
	print("")
	
	ans = str(input('\t:')).upper()
	
	if ans == "N":
		cadastro()
		
	elif ans == "L":
		displayData()
		
	elif ans == "E":
		delClient()
		
	elif ans == "S":
		running = False

















