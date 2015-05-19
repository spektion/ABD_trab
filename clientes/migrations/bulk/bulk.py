from clientes.models import cliente, categoria, crm_cliente

def run():
	print("Existem registos nas talelas - este ficheiro reinicializa todos os dados.\\n Tem a certeza que pretende continuar (S/N)?")
	choice = raw_input().lower()

	if choice == "N":
		return

	cliente.objects.all().delete()

	cliente.objects.bulk_create([
		cliente(nome = "vitor", nacionalidade = Portugal, bi= 12345678, telemovel= 982987323)
		cliente(nome = "luis", nacionalidade = Portugal, bi= 19832313, telemovel= 934654231)
		cliente(nome = "goncalo", nacionalidade = Portugal, bi= 57623872, telemovel= 934543534)
		])


    categoria.objects.all().delete()

    categoria.objects.bulk_create([
    categoria(name = "foto"),
    categoria(name = "imagem som"),
    categoria(name = "burotica e telecom"),
    categoria(name = "livros")
    categoria(name = "dvd")
    ])

   #   categoria.objects.all().delete()

    #categoria.objects.bulk_create([
    #categoria(cod_categoria = categoria.objects.filter(name = "foto")[0], \
      #  des_categoria = Game.objects.filter(id = 1)[0], movie_location = "youtube"),
    #Movie(movie_type = MovieType.objects.filter(name = "TV")[0], \
     #   game = Game.objects.filter(id = 2)[0], movie_location = "youtube"),
    #Movie(movie_type = MovieType.objects.filter(name = "TV")[0], \
       # game = Game.objects.filter(id = 3)[0], movie_location = "youtube"),
   # Movie(movie_type = MovieType.objects.filter(name = "test")[0], \
    #    game = Game.objects.filter(id = 1)[0], movie_location = "youtube")
    #])

    print ("done!")
