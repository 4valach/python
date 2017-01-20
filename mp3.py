# -*- coding: utf-8 -*-
import eyed3 
import datetime
import MySQLdb





con = MySQLdb.connect("localhost","avlanch4","","c9" )
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS musica(id int, titulo varchar(50),artista varchar(50), duracion time, genero varchar(20))")


def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. add una nueva cancion a la base de datos")
    print ("2. listar todos los estilos de los que tenemos alguna cancion")
    print ("3. listar todas las canciones de un interprete")
    print ("4. listar todas las canciones de un estilo")
    print ("5. listar todas las canciones de la base de datos")
    print ("6. eliminar una cancion de la base de datos dado el tıtulo y el interprete")
    print ("7. salir")
    print (67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-7]: ")
     
    if choice==1:     
        print ("Menu 1 has been selected")
        bd = raw_input("Introduce el nombre del mp3, recuerda que tiene que estar en el mismo directorio: ")
        audiofile = eyed3.load(bd)
        
        print ("titulo: " + audiofile.tag.title)
        titulo = audiofile.tag.title
        
        print ("artista: " + audiofile.tag.artist)
        artista = audiofile.tag.artist
        
        print ("duracion: " + str(datetime.timedelta(seconds=audiofile.info.time_secs)))
        duracion = str(datetime.timedelta(seconds=audiofile.info.time_secs))
        
        print ("genero: " + audiofile.tag.genre.name)
        genero = audiofile.tag.genre.name
        
        add_cancion = ("INSERT INTO musica "
               "(titulo, artista, duracion, genero) "
               "VALUES (titulo, artista, duracion, genero)")
              
               
               
               
        cursor.execute(add_cancion)
        con.commit()
        cursor.close()
        con.close()
        print ("cancion añadida")
        
        
    elif choice==2:
        print ("Menu 2 has been selected")
        listar_est = ("SELECT distinct genero FROM musica ")
        cursor.execute(listar_est)
        result_set = cursor.fetchall()
        for row in result_set:
            print (row[0])
        
        con.commit()
        cursor.close()
        con.close()
	    
	    
    elif choice==3:
        print ("Menu 3 has been selected")
        n_artista = raw_input("Introduce el nombre del artista que buscas: ")
        listar_int = ("SELECT * FROM musica WHERE artista = n_artista ")
        cursor.execute(listar_int)
        rows = cursor.fetchall()
 
        print(cursor.rowcount)
        for row in rows:
            print(row)
       
            
        con.commit()
        cursor.close()
        con.close()
   
   
    elif choice==4:
        print ("Menu 4 has been selected")
        n_estilo = raw_input("Introduce el genero que buscas: ")
        listar_est = ("SELECT * FROM musica WHERE genero = n_estilo ")
        cursor.execute(listar_est)
        rows = cursor.fetchall()
 
        print(cursor.rowcount)
        for row in rows:
            print(row)
       
            
        con.commit()
        cursor.close()
        con.close()
   
    elif choice==5:
        print ("Menu 5 has been selected")
       
        listar_int = ("SELECT * FROM musica")
        cursor.execute(listar_int)
        rows = cursor.fetchall()
 
        print(cursor.rowcount)
        for row in rows:
            print(row)
       
            
        con.commit()
        cursor.close()
        con.close()
   
    elif choice==6:
        print ("Menu 6 has been selected")
        autorb = raw_input("Introduce el autor a borrar: ")
        cancionb = raw_input("Introduce la cancion del autor a borrar: ")
        borrar = ("DELETE * FROM musica WHERE autor = autorb and titulo = cancionb")
        cursor.execute(borrar)
        print ("elemento eliminado")
        
    elif choice==7:
        print ("Menu 7 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("error")