import pandas as pd 
import requests
import json



#Función para verificar si los datos obtenidos no están vacios o tienen valores nulos.
def check_if_valid_data(df: pd.DataFrame ) -> bool:
	if df.empty:
		print("No hay datos")
		return False

	if df.isnull().values.any():
		raise Exception("Se encontraron valores nulos")

	return True		


if __name__ == "__main__":

	#Descargar los datos
	r = requests.get("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow")
	data = r.json()	

	#Se crean listas en blanco para almacenar los datos que se requieren 
	Is_answered = []
	Owner = []
	Views = []
	Activity_date = []
	Link =[]	
	
	# Se extraen solamente los valores relevantes del objeto json 
	for i in data["items"]:
	    Is_answered.append(i['is_answered'])
	    Owner.append(i['owner']['reputation'])
	    Views.append(i['view_count'])
	    Activity_date.append(i['last_activity_date'])
	    Link.append(i['link'])	
	
	 #Se prepara un diccionario para que los datos se guarden en un dataFrame de pandas
	data_dict = {
	    'Is_answered' : Is_answered,
	    'Views' : Views,
	    'Activity_date' : Activity_date,
	    'Link' : Link
	    }	
	
	#Se guardan los valores en formato DataFrame pandas 
	df = pd.DataFrame(data_dict, columns = ["Is_answered" , "Views", "Activity_date", "Link"])	

	df_ower = pd.DataFrame(Owner, columns=["Owner"] )	

	df_resultado = pd.concat([df, df_ower], axis=1)	
	
	#Se hace una validacion antes de seguir
	if check_if_valid_data(df_resultado):
		print("Datos validos, Se prosigue")


	#Se obtiene el número de respuestas contestadas y no contestadas
	Trues = df_resultado['Is_answered'].value_counts()
	print("El numero de respuestas contestadas es: ", Trues[1])
	print("El numero de respuestas no contestadas es:", Trues[0])
	print("")
	#Se obtiene la respuesta con mayor owners
	Mayor_owner = df_resultado.loc[df_resultado["Owner"].idxmax()]
	print("La respuesta con mayor owners tiene %s y es es: " %Mayor_owner[4], Mayor_owner[3])
	print("")

	#Se obtiene la respuesta con menor número de vistas
	Min_views = df_resultado.loc[df_resultado["Views"].idxmin()]
	print("La respuesta con menor numero de vistas tiene %s y es: " %Min_views[1], Min_views[3])
	print("")


	# Se obtiene la respuesta más vieja y más actual
	newer_answ = df_resultado.loc[df_resultado["Activity_date"].idxmin()]
	older_answ = df_resultado.loc[df_resultado["Activity_date"].idxmax()]
	print("La respuesta más vieja  es: ",  older_answ[3])
	print("La respuesta más actual es: ", newer_answ[3])










